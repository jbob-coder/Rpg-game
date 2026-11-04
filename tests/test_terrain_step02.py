"""Terrain Step 02: validate 16 local chunks, placement, seams, and exported assets.

Tests GLB geometry and manifest, NOT physics, Godot import, or gameplay.
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

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools" / "terrain"))
from build_step02_chunks import (  # noqa: E402
    CHUNK_SIZE_M, CHUNK_COORDINATES, GROUND_THICKNESS_M,
    WORLD_MIN_M, WORLD_MAX_M, build, chunk_id, chunk_mesh, chunk_records,
)


class TestTerrainStep02(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._temp = tempfile.TemporaryDirectory()
        cls.folder = Path(cls._temp.name)
        cls.manifest = build(cls.folder)
        cls.world = trimesh.load(cls.folder / "terrain_step02_full_64m.glb", force="scene")

    @classmethod
    def tearDownClass(cls) -> None:
        cls._temp.cleanup()

    def test_chunk_count_unique_identifiers_and_negative_grid(self) -> None:
        records = self.manifest["chunks"]
        self.assertEqual(len(records), 16)
        self.assertEqual(len({r["id"] for r in records}), 16)
        self.assertEqual({r["cx"] for r in records}, set(CHUNK_COORDINATES))
        self.assertEqual({r["cz"] for r in records}, set(CHUNK_COORDINATES))
        self.assertEqual(chunk_id(-2, 1), "terrain_cx-2_cz+1")

    def test_world_dimensions_and_exact_bounds(self) -> None:
        self.assertEqual(self.manifest["world_dimensions_xz_m"], [64, 64])
        self.assertEqual(self.manifest["world_bounds_xz_m"], [[-32, -32], [32, 32]])
        self.assertEqual(len(self.world.geometry), 16)
        np.testing.assert_allclose(self.world.bounds[0], [WORLD_MIN_M, -GROUND_THICKNESS_M, WORLD_MIN_M], atol=1e-6)
        np.testing.assert_allclose(self.world.bounds[1], [WORLD_MAX_M, 0.0, WORLD_MAX_M], atol=1e-6)

    def test_individual_chunk_local_origin_no_baked_world_offset(self) -> None:
        for record in self.manifest["chunks"]:
            loaded = trimesh.load(self.folder / "chunks" / record["filename"], force="scene")
            self.assertEqual(len(loaded.geometry), 1)
            np.testing.assert_allclose(loaded.bounds, [[0, -GROUND_THICKNESS_M, 0], [16, 0, 16]], atol=1e-6)
            self.assertEqual(record["origin_m"], [record["cx"] * 16, 0, record["cz"] * 16])

    def test_world_transforms_and_names_after_glb_reimport(self) -> None:
        by_id = {r["id"]: r for r in self.manifest["chunks"]}
        self.assertEqual(set(self.world.geometry.keys()), set(by_id))
        for node in self.world.graph.nodes_geometry:
            transform, geom_id = self.world.graph.get(node)
            record = by_id[geom_id]
            np.testing.assert_allclose(transform[:3, 3], record["origin_m"], atol=1e-6)

    def test_adjacent_chunks_have_no_gap_or_overlap_in_plan(self) -> None:
        records = {(r["cx"], r["cz"]): r for r in self.manifest["chunks"]}
        # Each adjacent pair shares exactly one boundary, same Y and edge span.
        comparisons = 0
        for (cx, cz), a in records.items():
            if (cx + 1, cz) in records:
                b = records[(cx + 1, cz)]
                self.assertEqual(a["world_bounds_xz_m"][1][0], b["world_bounds_xz_m"][0][0])
                self.assertEqual(a["world_bounds_xz_m"][0][1], b["world_bounds_xz_m"][0][1])
                self.assertEqual(a["world_bounds_xz_m"][1][1], b["world_bounds_xz_m"][1][1])
                comparisons += 1
            if (cx, cz + 1) in records:
                b = records[(cx, cz + 1)]
                self.assertEqual(a["world_bounds_xz_m"][1][1], b["world_bounds_xz_m"][0][1])
                self.assertEqual(a["world_bounds_xz_m"][0][0], b["world_bounds_xz_m"][0][0])
                self.assertEqual(a["world_bounds_xz_m"][1][0], b["world_bounds_xz_m"][1][0])
                comparisons += 1
        self.assertEqual(comparisons, 24)  # 12 E/W + 12 N/S

    def test_glbs_and_manifest_hashes_are_consistent(self) -> None:
        for record in self.manifest["chunks"]:
            data = (self.folder / "chunks" / record["filename"]).read_bytes()
            self.assertEqual(data[:4], b"glTF")
            self.assertEqual(int.from_bytes(data[4:8], "little"), 2)
            self.assertEqual(record["sha256"], hashlib.sha256(data).hexdigest())
            self.assertEqual(record["bytes"], len(data))
        combined_data = (self.folder / "terrain_step02_full_64m.glb").read_bytes()
        self.assertEqual(self.manifest["preview"]["sha256"], hashlib.sha256(combined_data).hexdigest())
        saved = json.loads((self.folder / "terrain_manifest.json").read_text())
        self.assertEqual(saved, self.manifest)

    def test_package_contains_all_components_once(self) -> None:
        with zipfile.ZipFile(self.folder / "terrain_step02_chunks.zip") as zf:
            names = zf.namelist()
            self.assertEqual(len(names), 18)
            self.assertEqual(len(set(names)), 18)
            self.assertIn("terrain_manifest.json", names)
            self.assertIn("terrain_step02_full_64m.glb", names)
            self.assertTrue(all(f"chunks/{r['filename']}" in names for r in self.manifest["chunks"]))
            self.assertIsNone(zf.testzip())

    def test_spatial_mapping_negative_coordinates_is_stable(self) -> None:
        self.assertEqual(chunk_id(-2, -2), "terrain_cx-2_cz-2")
        self.assertEqual(chunk_id(1, 1), "terrain_cx+1_cz+1")
        # Floor division, not truncation toward 0, selects correct negative cells.
        for x, cx in [(-32, -2), (-0.1, -1), (0, 0), (31.999, 1)]:
            self.assertEqual(int(x // CHUNK_SIZE_M), cx)


if __name__ == "__main__":
    unittest.main()
