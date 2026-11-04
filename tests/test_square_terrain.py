"""Self-contained offline checks for square terrain GLBs and chunk seams.

Runs against freshly generated artifacts in an isolated temporary directory.
This does not validate engine collision, water gameplay, or Android runtime.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
import zipfile

import numpy as np
import trimesh

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
# The source is published in GitHub tools/terrain and in ZIP source/.
TOOL_DIR = ROOT / "tools" / "terrain"
if not (TOOL_DIR / "generate_square_terrain.py").exists():
    TOOL_DIR = HERE.parent
sys.path.insert(0, str(TOOL_DIR))
from generate_square_terrain import (  # noqa: E402
    CHUNK, WORLD, build, floor_height, is_river, ATLAS_NAMES,
)


class TestSquareTerrain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.root = Path(cls.tmp.name)
        # Simulate private/unrelated files in a worktree; never include in kit.
        (cls.root / "local_secrets.txt").write_text("not an asset", encoding="utf-8")
        (cls.root / "__pycache__").mkdir()
        (cls.root / "__pycache__" / "junk.pyc").write_bytes(b"junk")
        cls.manifest, cls.bundle = build(cls.root)
        cls.assets = cls.root / "assets"

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def chunk(self, cx, cz):
        path = self.assets / "chunks" / f"terrain_cx{cx}_cz{cz}.glb"
        return trimesh.load(path, force="scene").geometry[f"terrain_cx{cx}_cz{cz}"]

    def test_glb_prefabs_are_real_binary_gltf2(self):
        self.assertEqual(len(self.manifest["tiles"]), 9)
        for item in self.manifest["tiles"]:
            p = self.assets / "tiles" / item["filename"]
            data = p.read_bytes()
            self.assertEqual(data[:4], b"glTF")
            self.assertEqual(int.from_bytes(data[4:8], "little"), 2)
            self.assertEqual(int.from_bytes(data[8:12], "little"), len(data))
            self.assertEqual(hashlib.sha256(data).hexdigest(), item["sha256"])
            self.assertIn(b"PNG", data)

    def test_prefab_geometric_dimensions_and_origin(self):
        for item in self.manifest["tiles"]:
            s = trimesh.load(self.assets / "tiles" / item["filename"], force="scene")
            lo, hi = s.bounds
            np.testing.assert_allclose(lo[[0, 2]], [0, 0], atol=1e-6)
            np.testing.assert_allclose(hi[[0, 2]], [1, 1], atol=1e-6)
            if item["tile"] == "water_surface":
                self.assertAlmostEqual(hi[1], 0.1, places=5)
            else:
                np.testing.assert_allclose([lo[1], hi[1]], [0, 1], atol=1e-6)
                self.assertEqual(len(s.geometry), 1)

    def test_terrain_prefabs_have_outward_surface_normals(self):
        mesh = trimesh.load(self.assets / "tiles" / "grass_1m.glb", force="mesh")
        np.testing.assert_allclose(mesh.face_normals[0], [0, 1, 0], atol=1e-6)
        np.testing.assert_allclose(mesh.face_normals[2], [0, -1, 0], atol=1e-6)
        self.assertTrue(np.isfinite(mesh.vertices).all())

    def test_sixteen_chunks_cover_world_without_overlap(self):
        chunks = self.manifest["chunks"]
        self.assertEqual(len(chunks), 16)
        self.assertEqual(len(set(c["id"] for c in chunks)), 16)
        coverage = set()
        for c in chunks:
            cx, cz = c["coord"]
            self.assertEqual(c["origin_m"], [cx * CHUNK, 0, cz * CHUNK])
            self.assertEqual(c["bounds_xz_m"], [[cx * CHUNK, cz * CHUNK], [(cx + 1) * CHUNK, (cz + 1) * CHUNK]])
            for x in range(cx * CHUNK, (cx + 1) * CHUNK):
                for z in range(cz * CHUNK, (cz + 1) * CHUNK):
                    self.assertNotIn((x, z), coverage)
                    coverage.add((x, z))
        self.assertEqual(len(coverage), WORLD * WORLD)
        self.assertEqual((min(x for x, _ in coverage), max(x for x, _ in coverage)), (-32, 31))
        self.assertEqual((min(z for _, z in coverage), max(z for _, z in coverage)), (-32, 31))

    def test_chunk_glbs_local_dimensions_and_hashes(self):
        for c in self.manifest["chunks"]:
            p = self.assets / "chunks" / c["filename"]
            data = p.read_bytes()
            self.assertEqual(data[:4], b"glTF")
            self.assertEqual(hashlib.sha256(data).hexdigest(), c["sha256"])
            mesh = trimesh.load(p, force="scene")
            lo, hi = mesh.bounds
            np.testing.assert_allclose(lo[[0, 2]], [0, 0], atol=1e-5)
            np.testing.assert_allclose(hi[[0, 2]], [16, 16], atol=1e-5)

    def test_combined_world_bounds(self):
        p = self.assets / self.manifest["preview"]["filename"]
        self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(), self.manifest["preview"]["sha256"])
        s = trimesh.load(p, force="scene")
        lo, hi = s.bounds
        np.testing.assert_allclose(lo[[0, 2]], [-32, -32], atol=1e-5)
        np.testing.assert_allclose(hi[[0, 2]], [32, 32], atol=1e-5)
        self.assertEqual(len([n for n in s.geometry if n.startswith("terrain_cx")]), 16)

    def test_river_snow_and_hills_are_nontrivial(self):
        cells = [(x, z) for x in range(-32, 32) for z in range(-32, 32)]
        self.assertGreater(sum(is_river(x, z) for x, z in cells), 100)
        heights = [floor_height(x, z) for x, z in cells]
        self.assertLessEqual(min(heights), -1)
        self.assertGreaterEqual(max(heights), 19)
        self.assertGreater(sum(h >= 17 for h in heights), 30)

    @staticmethod
    def vertical_segments(mesh, axis, plane):
        """Index unit-height wall quads by the coordinate across a shared boundary."""
        counts = {}
        for indices in mesh.faces:
            verts = mesh.vertices[indices]
            if not np.allclose(verts[:, axis], plane, atol=1e-6):
                continue
            other = 2 if axis == 0 else 0
            if not np.isclose(np.ptp(verts[:, 1]), 1, atol=1e-6):
                continue
            if not np.isclose(np.ptp(verts[:, other]), 1, atol=1e-6):
                continue
            a = int(round(min(verts[:, other])))
            y = int(round(min(verts[:, 1])))
            counts[(a, y)] = counts.get((a, y), 0) + 1
        return counts

    def test_all_24_internal_chunk_seams_have_required_cliff_walls(self):
        # Check all 12 vertical and all 12 horizontal seams, 16 cells each.
        meshes = {(cx, cz): self.chunk(cx, cz) for cx in range(-2, 2) for cz in range(-2, 2)}
        pairs = 0
        for cz in range(-2, 2):
            for cx in range(-2, 1):
                left, right = meshes[(cx, cz)], meshes[(cx + 1, cz)]
                a = self.vertical_segments(left, 0, 16)
                b = self.vertical_segments(right, 0, 0)
                for local_z in range(16):
                    z = cz * 16 + local_z
                    h1 = floor_height((cx + 1) * 16 - 1, z)
                    h2 = floor_height((cx + 1) * 16, z)
                    for y in range(min(h1, h2), max(h1, h2)):
                        self.assertEqual((a if h1 > h2 else b).get((local_z, y)), 2)
                pairs += 1
        for cx in range(-2, 2):
            for cz in range(-2, 1):
                near, far = meshes[(cx, cz)], meshes[(cx, cz + 1)]
                a = self.vertical_segments(near, 2, 16)
                b = self.vertical_segments(far, 2, 0)
                for local_x in range(16):
                    x = cx * 16 + local_x
                    h1 = floor_height(x, (cz + 1) * 16 - 1)
                    h2 = floor_height(x, (cz + 1) * 16)
                    for y in range(min(h1, h2), max(h1, h2)):
                        self.assertEqual((a if h1 > h2 else b).get((local_x, y)), 2)
                pairs += 1
        self.assertEqual(pairs, 24)

    def test_package_allowlist_and_archive_integrity(self):
        with zipfile.ZipFile(self.bundle) as z:
            names = set(z.namelist())
            self.assertIsNone(z.testzip())
            expected = {"README.md", "manifest.json", "assets/terrain_pixel_atlas.png", "assets/world_64m_terrain_preview.glb", "source/generate_square_terrain.py", "source/test_square_terrain.py"}
            expected |= {"assets/chunks/" + c["filename"] for c in self.manifest["chunks"]}
            expected |= {"assets/tiles/" + t["filename"] for t in self.manifest["tiles"]}
            self.assertEqual(names, expected)
            self.assertNotIn("local_secrets.txt", names)
            self.assertFalse(any("__pycache__" in n for n in names))
            self.assertEqual(json.loads(z.read("manifest.json")), self.manifest)


if __name__ == "__main__":
    unittest.main(verbosity=2)
