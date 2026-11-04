"""Geometry-level evidence for Step 01; does NOT replace engine/runtime tests."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
import sys

import numpy as np
import trimesh

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools" / "terrain"))
from build_scale_calibration import (  # noqa: E402
    EYE_HEIGHT_M, GROUND_SIZE_M, PATH_WIDTHS_M, PLAYER_HEIGHT_M,
    PLAYER_RADIUS_M, PLAYER_SPAWN_XZ_M, build_scene, write_glb,
)


class TestTerrainStep01(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.scene = build_scene()
        with tempfile.TemporaryDirectory() as folder:
            cls.output = Path(folder) / "scale.glb"
            write_glb(cls.output)
            cls.payload = cls.output.read_bytes()
            cls.reloaded = trimesh.load(cls.output, force="scene")

    def mesh(self, name: str) -> trimesh.Trimesh:
        # Geometry names are retained in glTF/GLB export.
        return self.reloaded.geometry[name]

    def assert_bounds(self, mesh_name: str, extents: tuple[float, float, float], tolerance: float = 0.001) -> None:
        np.testing.assert_allclose(self.mesh(mesh_name).extents, extents, atol=tolerance)

    def test_glb_header_and_reimport(self):
        self.assertEqual(self.payload[:4], b"glTF")
        self.assertEqual(int.from_bytes(self.payload[4:8], "little"), 2)
        self.assertEqual(int.from_bytes(self.payload[8:12], "little"), len(self.payload))
        self.assertGreaterEqual(len(self.reloaded.geometry), 8)

    def test_ground_is_16_square_with_zero_top(self):
        ground = self.mesh("Ground_16m_x_16m_TopY0")
        self.assert_bounds("Ground_16m_x_16m_TopY0", (GROUND_SIZE_M, 0.2, GROUND_SIZE_M))
        self.assertAlmostEqual(ground.bounds[1, 1], 0.0, delta=0.001)

    def test_lane_widths_and_usable_clearance(self):
        for width in PATH_WIDTHS_M:
            lane = self.mesh(f"Path_ClearWidth_{int(width)}m")
            self.assertAlmostEqual(lane.extents[0], width, delta=0.001)
            self.assertAlmostEqual(lane.extents[2], 14.0, delta=0.001)
            self.assertGreater(width, 2 * PLAYER_RADIUS_M)
        # Cross-section: 3 m path with .35 m radius proxy -> 2.3 m spare width.
        self.assertAlmostEqual(PATH_WIDTHS_M[0] - 2 * PLAYER_RADIUS_M, 2.3)

    def test_character_height_and_spawn_ground_contact(self):
        proxy = self.mesh("PlayerProxy_Capsule_1p8m")
        self.assertAlmostEqual(proxy.extents[1], PLAYER_HEIGHT_M, delta=0.005)
        self.assertAlmostEqual(proxy.bounds[0, 1], 0, delta=0.005)
        self.assertAlmostEqual((proxy.bounds[0, 0] + proxy.bounds[1, 0]) / 2, PLAYER_SPAWN_XZ_M[0], delta=0.001)
        self.assertAlmostEqual((proxy.bounds[0, 2] + proxy.bounds[1, 2]) / 2, PLAYER_SPAWN_XZ_M[1], delta=0.001)
        # Proxy fully inside the 3 m lane, not overlapping lane edge.
        lane = self.mesh("Path_ClearWidth_3m")
        self.assertGreaterEqual(proxy.bounds[0, 0], lane.bounds[0, 0] - 1e-3)
        self.assertLessEqual(proxy.bounds[1, 0], lane.bounds[1, 0] + 1e-3)

    def test_eye_marker_height_and_facing_direction(self):
        eye = self.mesh("EyeMarker_Y1p65m_FacingNorth")
        center = eye.centroid
        self.assertAlmostEqual(center[1], EYE_HEIGHT_M, delta=0.005)
        self.assertLess(center[2], PLAYER_SPAWN_XZ_M[1])  # negative Z is forward

    def test_reference_cube(self):
        self.assert_bounds("UnitCube_1m", (1.0, 1.0, 1.0))
        self.assertAlmostEqual(self.mesh("UnitCube_1m").bounds[0, 1], 0, delta=0.001)


if __name__ == "__main__":
    unittest.main()
