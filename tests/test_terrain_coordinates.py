"""GLB coordinate-contract tests using independent, real GLB fixtures.

These fixtures verify numeric placement and export/reimport, not the existing
procedural world generator or engine collision. Run from repository root:
    python -m unittest discover -s tests -p 'test_terrain_coordinates.py' -v
"""
from __future__ import annotations

import math
from pathlib import Path
import sys
import tempfile
import unittest

import numpy as np
import trimesh

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools' / 'terrain'))
from coordinates import (  # noqa: E402
    CHUNK_SIZE_M, cell_to_chunk, chunk_local_to_world, chunk_origin,
    shared_edge, world_to_cell, world_to_chunk,
)


def _quad(points: list[tuple[float, float, float]]) -> trimesh.Trimesh:
    return trimesh.Trimesh(
        vertices=np.array(points, dtype=np.float32),
        faces=np.array([[0, 1, 2], [0, 2, 3]], dtype=np.int32),
        process=False,
    )


def top_surface(x: float, z: float, y: float) -> trimesh.Trimesh:
    """Single 1m top face. Top elevation y, cell at [x,x+1]×[z,z+1]."""
    return _quad([(x, y, z), (x, y, z + 1),
                  (x + 1, y, z + 1), (x + 1, y, z)])


def cliff_wall_at_x(x: float, z: float, lower: int, upper: int) -> trimesh.Trimesh:
    return _quad([(x, lower, z), (x, lower, z + 1),
                  (x, upper, z + 1), (x, upper, z)])


def export_and_reload(path: Path, meshes: list[tuple[str, trimesh.Trimesh, tuple[float, float, float]]]):
    scene = trimesh.Scene()
    for name, mesh, translation in meshes:
        transform = np.eye(4)
        transform[:3, 3] = translation
        scene.add_geometry(mesh, geom_name=name, node_name=name, transform=transform)
    payload = scene.export(file_type='glb')
    assert payload[:4] == b'glTF'
    assert int.from_bytes(payload[4:8], 'little') == 2
    assert int.from_bytes(payload[8:12], 'little') == len(payload)
    path.write_bytes(payload)
    return trimesh.load(path, force='scene')


class TestTerrainCoordinateContract(unittest.TestCase):
    def test_world_origin_and_negative_coordinates(self):
        examples = {
            (0, 0): (0, 0, 0, 0),
            (15, 15): (0, 0, 15, 15),
            (16, 0): (1, 0, 0, 0),
            (-1, -1): (-1, -1, 15, 15),
            (-16, -16): (-1, -1, 0, 0),
            (-17, -17): (-2, -2, 15, 15),
        }
        for cell, expected in examples.items():
            self.assertEqual(cell_to_chunk(*cell), expected)
            self.assertEqual(world_to_chunk(cell[0] + 0.25, cell[1] + 0.25), expected)
            cx, cz, lx, lz = expected
            self.assertEqual(chunk_local_to_world(cx, cz, lx, lz), cell)
        self.assertEqual(world_to_cell(-0.01, -16), (-1, -16))
        self.assertEqual(chunk_origin(-2, 1), (-32, 0, 16))
        self.assertEqual(world_to_chunk(-32.0, 31.999), (-2, 1, 0, 15))

    def test_grid_input_rejections(self):
        with self.assertRaises(ValueError):
            chunk_local_to_world(0, 0, 16, 1)
        with self.assertRaises(TypeError):
            cell_to_chunk(0.5, 0)
        with self.assertRaises(ValueError):
            world_to_cell(math.nan, 1)
        with self.assertRaises(ValueError):
            world_to_chunk(math.inf, 0)
        with self.assertRaises(ValueError):
            shared_edge(0, 0, 1, 1)

    def test_equal_height_neighbors_glb_edge_alignment(self):
        # Two adjacent top surfaces at the same elevation, no cliff wall.
        self.assertEqual(shared_edge(0, 0, 1, 0), ('x', 1))
        with tempfile.TemporaryDirectory() as tmp:
            loaded = export_and_reload(Path(tmp)/'equal.glb', [
                ('left', top_surface(0, 0, 3), (0, 0, 0)),
                ('right', top_surface(1, 0, 3), (0, 0, 0)),
            ])
            self.assertEqual(len(loaded.geometry), 2)
            bounds = loaded.bounds
            np.testing.assert_allclose(bounds[0], [0, 3, 0])
            np.testing.assert_allclose(bounds[1], [2, 3, 1])
            edge_vertices = [
                sorted(map(tuple, mesh.vertices[np.isclose(mesh.vertices[:, 0], 1)][:, [1, 2]]))
                for mesh in loaded.geometry.values()
            ]
            self.assertEqual(edge_vertices[0], edge_vertices[1])
            self.assertEqual(edge_vertices[0], [(3., 0.), (3., 1.)])

    def test_different_elevation_neighbors_glb_cliff_is_contiguous(self):
        # Left top y=4, right top y=2: exposed wall spans exactly y=[2,4].
        with tempfile.TemporaryDirectory() as tmp:
            loaded = export_and_reload(Path(tmp)/'step.glb', [
                ('high', top_surface(0, 0, 4), (0, 0, 0)),
                ('low', top_surface(1, 0, 2), (0, 0, 0)),
                ('cliff', cliff_wall_at_x(1, 0, 2, 4), (0, 0, 0)),
            ])
            self.assertEqual(len(loaded.geometry), 3)
            wall = next(mesh for name, mesh in loaded.geometry.items()
                        if name.startswith('cliff'))
            np.testing.assert_allclose(wall.bounds, [[1, 2, 0], [1, 4, 1]])
            self.assertEqual(shared_edge(0, 0, 1, 0), ('x', 1))

    def test_neighbor_chunks_glb_global_transform_once(self):
        # Reimport two locally authored chunks at cx=-1 and cx=0.
        self.assertEqual(chunk_origin(-1, 0), (-16, 0, 0))
        self.assertEqual(chunk_origin(0, 0), (0, 0, 0))
        left_local = top_surface(CHUNK_SIZE_M - 1, 0, 4)
        right_local = top_surface(0, 0, 4)
        with tempfile.TemporaryDirectory() as tmp:
            loaded = export_and_reload(Path(tmp)/'chunks.glb', [
                ('terrain_cx-1_cz0', left_local, chunk_origin(-1, 0)),
                ('terrain_cx0_cz0', right_local, chunk_origin(0, 0)),
            ])
            np.testing.assert_allclose(loaded.bounds, [[-1, 4, 0], [1, 4, 1]])
            self.assertEqual(cell_to_chunk(-1, 0), (-1, 0, 15, 0))
            self.assertEqual(cell_to_chunk(0, 0), (0, 0, 0, 0))
            # Transformations are preserved in the GLB scene nodes.
            positions = sorted(round(loaded.graph.get(n)[0][0, 3])
                               for n in loaded.graph.nodes_geometry)
            self.assertEqual(positions, [-16, 0])


if __name__ == '__main__':
    unittest.main(verbosity=2)
