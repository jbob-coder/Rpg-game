"""Generate reusable square voxel terrain GLBs and an assembled 64x64 m blockout.

Reference: user's terrain concept screenshot. Assets are an interpretation, not
image-to-mesh reconstruction. 1 unit = 1 meter; X east, Y up, -Z north.

Usage: python source/generate_square_terrain.py --out .
Dependencies: numpy, pillow, trimesh.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import json
import math
from pathlib import Path
import random
import zipfile

import numpy as np
from PIL import Image, ImageDraw
import trimesh
from trimesh.visual.texture import TextureVisuals
from trimesh.visual.material import PBRMaterial

TILE = 1.0
CHUNK = 16
WORLD = 64
SEED = 73918
ATLAS_CELL = 16
ATLAS_COLS = 4
ATLAS_ROWS = 4
COLOR = {
    "grass_top": (105, 189, 61),
    "grass_side": (113, 138, 65),
    "dirt_top": (157, 104, 54),
    "dirt_side": (137, 93, 56),
    "stone_top": (137, 142, 142),
    "stone_side": (117, 127, 135),
    "snow_top": (228, 239, 248),
    "snow_side": (205, 225, 243),
    "sand_top": (213, 193, 131),
    "sand_side": (190, 165, 108),
    "mossy_rock": (112, 132, 109),
    "river_top": (42, 156, 220),
    "waterfall": (70, 176, 244),
    "bedrock": (89, 95, 104),
    "gravel": (153, 143, 119),
    "grass_dark": (76, 154, 53),
}
ATLAS_NAMES = list(COLOR)


def colorspace_blend(base, delta):
    return tuple(max(0, min(255, int(v + delta))) for v in base)


def atlas_image():
    rng = random.Random(SEED)
    atlas = Image.new("RGBA", (ATLAS_COLS * ATLAS_CELL, ATLAS_ROWS * ATLAS_CELL))
    for idx, material in enumerate(ATLAS_NAMES):
        ox = idx % ATLAS_COLS * ATLAS_CELL
        oy = idx // ATLAS_COLS * ATLAS_CELL
        base = COLOR[material]
        for row in range(ATLAS_CELL):
            for col in range(ATLAS_CELL):
                noise = rng.choice([-15, -9, -5, 0, 0, 4, 8, 13])
                rgb = colorspace_blend(base, noise)
                if material == "grass_side":
                    rgb = colorspace_blend(COLOR["grass_dark"],noise) if row < 4 + rng.randrange(0,3) else colorspace_blend(COLOR["dirt_side"],noise)
                elif material == "snow_side":
                    rgb = colorspace_blend(COLOR["snow_top"],noise) if row < 6 else colorspace_blend(COLOR["stone_side"],noise)
                elif material == "mossy_rock" and row < 3:
                    rgb = colorspace_blend(COLOR["grass_dark"],noise)
                elif material == "river_top":
                    if (row + 2 * col) % 13 < 2: rgb = colorspace_blend(base,35)
                elif material == "waterfall":
                    if (col + 3 * row) % 10 < 3: rgb = colorspace_blend(base,42)
                elif material in ("stone_top","stone_side","bedrock"):
                    if (col // 5 + row // 6) % 2: rgb = colorspace_blend(rgb, 9)
                atlas.putpixel((ox+col, oy+row), (*rgb, 255))
    return atlas


def uv_region(kind):
    idx = ATLAS_NAMES.index(kind)
    cx, cy = idx % ATLAS_COLS, idx // ATLAS_COLS
    half = 0.32  # inset to prevent atlas bleeding at edges
    u0 = (cx*ATLAS_CELL+half)/(ATLAS_COLS*ATLAS_CELL)
    u1 = ((cx+1)*ATLAS_CELL-half)/(ATLAS_COLS*ATLAS_CELL)
    v1 = 1 - (cy*ATLAS_CELL+half)/(ATLAS_ROWS*ATLAS_CELL)
    v0 = 1 - ((cy+1)*ATLAS_CELL-half)/(ATLAS_ROWS*ATLAS_CELL)
    return [(u0,v0),(u1,v0),(u1,v1),(u0,v1)]


@dataclass
class Faces:
    verts: list
    tris: list
    uvs: list

    def __init__(self):
        self.verts, self.tris, self.uvs = [], [], []

    def quad(self, positions, tex):
        """Positions CCW as viewed from exposed face."""
        n=len(self.verts)
        self.verts.extend(positions)
        self.tris.extend(((n,n+1,n+2),(n,n+2,n+3)))
        self.uvs.extend(uv_region(tex))

    def mesh(self, texture, name, *, transparent=False):
        if not self.verts:
            return None
        mat = PBRMaterial(name=("pixelwater" if transparent else "pixelterrain"),
                          baseColorTexture=texture,
                          metallicFactor=0.0,roughnessFactor=1.0,
                          doubleSided=transparent,
                          alphaMode=("BLEND" if transparent else "OPAQUE"),
                          baseColorFactor=[255,255,255,195 if transparent else 255])
        mesh=trimesh.Trimesh(vertices=np.asarray(self.verts,dtype=np.float32),
                            faces=np.asarray(self.tris,dtype=np.int32),
                            process=False,validate=False)
        mesh.visual=TextureVisuals(uv=np.asarray(self.uvs,dtype=np.float32),material=mat)
        mesh.metadata["name"]=name
        return mesh


def put_top(f,x,y,z,mat):
    f.quad([(x,y,z),(x,y,z+1),(x+1,y,z+1),(x+1,y,z)],mat)

def put_bottom(f,x,y,z,mat):
    f.quad([(x,y,z),(x+1,y,z),(x+1,y,z+1),(x,y,z+1)],mat)

def put_xminus(f,x,y,z,mat):
    f.quad([(x,y,z),(x,y,z+1),(x,y+1,z+1),(x,y+1,z)],mat)

def put_xplus(f,x,y,z,mat):
    f.quad([(x+1,y,z+1),(x+1,y,z),(x+1,y+1,z),(x+1,y+1,z+1)],mat)

def put_zminus(f,x,y,z,mat):
    f.quad([(x+1,y,z),(x,y,z),(x,y+1,z),(x+1,y+1,z)],mat)

def put_zplus(f,x,y,z,mat):
    f.quad([(x,y,z+1),(x+1,y,z+1),(x+1,y+1,z+1),(x,y+1,z+1)],mat)


def block_surface(kind):
    """Reusable 1 x 1 x 1 m terrain block, local lower corner (0,0,0)."""
    mapping={
        "grass":("grass_top", "grass_side", "dirt_side"),
        "dirt":("dirt_top","dirt_side","dirt_side"),
        "stone":("stone_top","stone_side","stone_side"),
        "bedrock":("bedrock","bedrock","bedrock"),
        "snow":("snow_top","snow_side","stone_side"),
        "sand":("sand_top","sand_side","sand_side"),
        "gravel":("gravel","gravel","stone_side"),
        "mossy_stone":("mossy_rock","stone_side","stone_side"),
    }
    a,side,bottom = mapping[kind]
    f=Faces()
    put_top(f,0,1,0,a)
    put_bottom(f,0,0,0,bottom)
    put_xminus(f,0,0,0,side)
    put_xplus(f,0,0,0,side)
    put_zminus(f,0,0,0,side)
    put_zplus(f,0,0,0,side)
    return f


def river_x(z):
    # Winds from the back-left to the foreground-right.
    return -13.5 + 0.51 * (z+32) + 4.3 * math.sin((z+27)*0.12)


def is_river(x,z):
    return abs(x+0.5-river_x(z+0.5)) <= 2.45


def peak(x,z, px,pz,height,sx,sz):
    return height*math.exp(-0.5*((x-px)/sx)**2-0.5*((z-pz)/sz)**2)


def base_terrain_height(x,z):
    xx=x+0.5;zz=z+0.5
    h = 4.0 + 0.95*math.sin(xx*0.21)+0.9*math.cos(zz*0.18)+0.43*math.cos(xx*0.4+zz*0.23)
    h += peak(xx,zz,-23,-18,9,9,11)
    h += peak(xx,zz,23,-7,8.0,12,15)
    h += peak(xx,zz,-8,-28,9,10,12)
    h += peak(xx,zz,6,-29,18,7.5,8)
    h += peak(xx,zz,17,-26,15,8,9)
    h += peak(xx,zz,-30,19,6.0,12,13)
    h += peak(xx,zz,29,19,4,11,13)
    return max(2,min(28,int(round(h))))


def floor_height(x,z):
    if is_river(x,z):
        return 1 if z<0 else -1
    return base_terrain_height(x,z)


def top_material(x,z,h):
    xx=x+0.5;zz=z+0.5
    if is_river(x,z):
        return "gravel"
    # Snow is concentrated on the upper peaks and far northern ridge.
    if h>=17 and zz<-10: return "snow_top"
    if h>=12 and zz<-5: return "stone_top" if (x*7+z*11)%5!=0 else "mossy_rock"
    if abs(xx-river_x(zz))<4.7 and h<=5 and zz>0: return "sand_top"
    if h>8 and (x*31+z*13)%7==0: return "stone_top"
    return "grass_top"


def side_material(x,z,top_level,current_y,top_mat):
    distance=top_level-current_y
    if current_y<0 or distance>3: return "bedrock" if current_y<0 else "stone_side"
    if top_mat == "snow_top" and distance < 1: return "snow_side"
    if top_mat in ("stone_top","mossy_rock") and distance <=2: return "stone_side"
    if top_mat=="sand_top": return "sand_side" if distance<2 else "stone_side"
    if top_mat=="gravel": return "stone_side"
    return "grass_side" if distance < 1 else "dirt_side"


def column_sample(cx,cz, heights):
    return heights.get((cx,cz), 0)


def terrain_chunk(cx,cz,heights,texture):
    """Chunk geometry in [0..16] local XZ, section position in node transform."""
    f=Faces()
    start_x=cx*CHUNK;start_z=cz*CHUNK
    for j in range(CHUNK):
        for i in range(CHUNK):
            x=start_x+i; z=start_z+j
            h=column_sample(x,z,heights)
            material=top_material(x,z,h)
            put_top(f,i,h,j,material)
            # Only faces externally exposed after comparing neighbors globally.
            for direction,neighbor,fun in [
                ("xm",(x-1,z),put_xminus),
                ("xp",(x+1,z),put_xplus),
                ("zm",(x,z-1),put_zminus),
                ("zp",(x,z+1),put_zplus)]:
                beside=column_sample(*neighbor,heights)
                if beside<h:
                    for y in range(beside,h):
                        fun(f,i,y,j,side_material(x,z,h,y,material))
    return f.mesh(texture,f"terrain_cx{cx}_cz{cz}")


def water_chunk(cx,cz,texture):
    f=Faces()
    sx=cx*CHUNK;sz=cz*CHUNK
    for j in range(CHUNK):
        for i in range(CHUNK):
            x=sx+i;z=sz+j
            if not is_river(x,z): continue
            y=2.55 if z<0 else 0.55
            put_top(f,i,y,j,"river_top")
            # At Z=0, waterfall curtain connects the elevated upstream river.
            if z==-1 and is_river(x,0):
                # Face oriented toward downstream +Z; height 2 m.
                for high in range(2):
                    f.quad([(i,0.55+high,j+1),(i+1,0.55+high,j+1),
                            (i+1,1.55+high,j+1),(i,1.55+high,j+1)],"waterfall")
    return f.mesh(texture,f"water_cx{cx}_cz{cz}",transparent=True)


def make_water_prefab(texture):
    f=Faces()
    # Top of water surface at Y=0.1, bottom 0 (reusable square water plane).
    put_top(f,0,0.1,0,"river_top")
    return f.mesh(texture,"water_square_surface",transparent=True)


def export_scene(scene,output):
    output.parent.mkdir(parents=True,exist_ok=True)
    result=scene.export(file_type="glb")
    if not isinstance(result,bytes) or result[:4]!=b"glTF":
        raise RuntimeError(f"invalid GLB export: {output}")
    output.write_bytes(result)
    return {"filename":output.name,"bytes":len(result),"sha256":hashlib.sha256(result).hexdigest()}


def make_scene(terrain,water=None,origin=(0,0,0)):
    scene=trimesh.Scene()
    mat=np.eye(4)
    mat[:3,3]=origin
    scene.add_geometry(terrain,geom_name=terrain.metadata["name"],node_name=terrain.metadata["name"],transform=mat)
    if water is not None:
        scene.add_geometry(water,geom_name=water.metadata["name"],node_name=water.metadata["name"],transform=mat)
    return scene


def build(out:Path):
    assets=out/"assets";tiles=assets/"tiles";chunks=assets/"chunks"
    for folder in (tiles,chunks): folder.mkdir(parents=True,exist_ok=True)
    texture=atlas_image()
    texture.save(assets/"terrain_pixel_atlas.png")
    tile_files=[]
    for name in ("grass","dirt","stone","bedrock","snow","sand","gravel","mossy_stone"):
        mesh=block_surface(name).mesh(texture,name)
        file=tiles/f"{name}_1m.glb"
        item=export_scene(make_scene(mesh),file)
        item["tile"]=name
        tile_files.append(item)
    mesh=make_water_prefab(texture)
    item=export_scene(make_scene(mesh),tiles/"water_surface_1m.glb")
    item["tile"]="water_surface";tile_files.append(item)

    heights={(x,z):floor_height(x,z) for z in range(-WORLD//2,WORLD//2) for x in range(-WORLD//2,WORLD//2)}
    chunks_data=[]
    assembled=trimesh.Scene()
    for cz in range(-2,2):
        for cx in range(-2,2):
            terrain=terrain_chunk(cx,cz,heights,texture)
            water=water_chunk(cx,cz,texture)
            origin=(cx*CHUNK,0,cz*CHUNK)
            scene=make_scene(terrain,water)
            item=export_scene(scene,chunks/f"terrain_cx{cx}_cz{cz}.glb")
            item.update({"id":f"terrain_cx{cx}_cz{cz}","coord":[cx,cz],"origin_m":list(origin),"bounds_xz_m":[[cx*CHUNK,cz*CHUNK],[(cx+1)*CHUNK,(cz+1)*CHUNK]],"water_cells":sum(1 for z in range(cz*CHUNK,(cz+1)*CHUNK) for x in range(cx*CHUNK,(cx+1)*CHUNK) if is_river(x,z))})
            chunks_data.append(item)
            transform=np.eye(4);transform[:3,3]=origin
            assembled.add_geometry(terrain,geom_name=terrain.metadata["name"],node_name=terrain.metadata["name"],transform=transform)
            if water is not None:
                assembled.add_geometry(water,geom_name=water.metadata["name"],node_name=water.metadata["name"],transform=transform)
    combined=export_scene(assembled,assets/"world_64m_terrain_preview.glb")
    # Data manifest separates geometry from scene engine authoring.
    manifest={
        "format":"glTF 2.0 binary (.glb)","created_by":"generate_square_terrain.py",
        "design_reference":"User-provided voxel terrain image; stylized approximation, not geometric reconstruction",
        "tile_dimensions_m":[1,1,1],"water_prefab_height_m":0.1,
        "voxel_grid_m":1,"world_extent_m":[64,64],"world_min_xz_m":[-32,-32],"chunk_size_m":16,
        "coordinate_system":{"x":"east","y":"up","negative_z":"north","tile_origin":"lower southwest corner"},
        "water_top_height_m":{"upstream":2.55,"downstream":0.55,"waterfall_at_z":0},
        "ground_surface":"Stepped discrete-height terrain and exposed cliff sides; no actual physics/navmesh",
        "tiles":tile_files,"chunks":chunks_data,"preview":combined,
        "note":"The water planes are visual meshes only. A game engine must assign collision, physics, movement and material settings."
    }
    (out/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
    # Package only declared deliverables. Do not recursively archive an entire
    # worktree: that can leak .git, credentials, caches and unrelated game files.
    bundle = out / "square_terrain_glb_kit.zip"
    root = Path(__file__).resolve().parent
    kit_readme = (root / "SQUARE_TERRAIN_KIT.md")
    package_members = [
        out / "manifest.json",
        assets / "terrain_pixel_atlas.png",
        assets / "world_64m_terrain_preview.glb",
        *(tiles / item["filename"] for item in tile_files),
        *(chunks / item["filename"] for item in chunks_data),
    ]
    with zipfile.ZipFile(bundle, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for file in sorted(package_members):
            z.write(file, file.relative_to(out).as_posix())
        z.write(root / "generate_square_terrain.py", "source/generate_square_terrain.py")
        if (root / "test_square_terrain.py").is_file():
            z.write(root / "test_square_terrain.py", "source/test_square_terrain.py")
        if kit_readme.is_file():
            z.write(kit_readme, "README.md")
    return manifest, bundle


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--out",type=Path,default=Path(__file__).resolve().parents[1])
    args=p.parse_args()
    manifest,bundle=build(args.out)
    print(json.dumps({"tiles":len(manifest["tiles"]),"chunks":len(manifest["chunks"]),"preview":manifest["preview"],"zip_bytes":bundle.stat().st_size},indent=2))


if __name__=="__main__":main()
