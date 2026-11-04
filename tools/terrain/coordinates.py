"""Engine-independent integer-grid coordinates for the square terrain GLB kit.

All distances are in meters, +Y up, +X east, -Z north. A world grid cell
(x, z) occupies [x, x+1) × [z, z+1). Chunk indices use floor division,
including negative positions. Standalone chunk GLBs are LOCAL; their manifest
origin must be applied exactly once when assembling the world.
"""
from __future__ import annotations

import math

TILE_SIZE_M = 1
CHUNK_SIZE_M = 16


def _integer(value: int, label: str) -> int:
    if type(value) is not int:
        raise TypeError(f"{label} must be an integer grid coordinate")
    return value


def chunk_origin(cx: int, cz: int) -> tuple[int, int, int]:
    """Minimum X/Z (northwest) corner, in world-space meters."""
    return (_integer(cx, 'cx') * CHUNK_SIZE_M, 0,
            _integer(cz, 'cz') * CHUNK_SIZE_M)


def cell_to_chunk(x: int, z: int) -> tuple[int, int, int, int]:
    """Integer grid cell -> (cx, cz, local_x, local_z); locals in [0, 15]."""
    x, z = _integer(x, 'x'), _integer(z, 'z')
    cx, cz = x // CHUNK_SIZE_M, z // CHUNK_SIZE_M
    return cx, cz, x - cx * CHUNK_SIZE_M, z - cz * CHUNK_SIZE_M


def world_to_cell(x_m: float, z_m: float) -> tuple[int, int]:
    """Continuous world XZ -> occupied grid cell; half-open boundaries."""
    if any(isinstance(v, bool) or not isinstance(v, (int, float)) or
           not math.isfinite(v) for v in (x_m, z_m)):
        raise ValueError("World coordinates must be finite real numbers")
    return (math.floor(x_m / TILE_SIZE_M), math.floor(z_m / TILE_SIZE_M))


def world_to_chunk(x_m: float, z_m: float) -> tuple[int, int, int, int]:
    return cell_to_chunk(*world_to_cell(x_m, z_m))


def chunk_local_to_world(cx: int, cz: int, lx: int, lz: int) -> tuple[int, int]:
    """Local grid cell -> world XZ integer origin; reject spill across chunks."""
    _integer(lx, 'lx'); _integer(lz, 'lz')
    if not (0 <= lx < CHUNK_SIZE_M and 0 <= lz < CHUNK_SIZE_M):
        raise ValueError('Local cell must be in [0, 15] on both axes')
    ox, _, oz = chunk_origin(cx, cz)
    return ox + lx, oz + lz


def shared_edge(a_x: int, a_z: int, b_x: int, b_z: int) -> tuple[str, int]:
    """For adjacent grid cells, return common vertical edge axis/coordinate.

    E.g. cells (0,0) and (1,0) share ('x', 1); cells (0,0) and
    (0,-1) share ('z', 0). Reject non-neighbors and diagonals.
    """
    for label, v in [('a_x',a_x),('a_z',a_z),('b_x',b_x),('b_z',b_z)]:
        _integer(v, label)
    if abs(a_x - b_x) + abs(a_z - b_z) != 1:
        raise ValueError('Cells must be orthogonally adjacent')
    return ('x', max(a_x, b_x)) if a_z == b_z else ('z', max(a_z, b_z))
