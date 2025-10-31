from typing import Tuple
import numpy as np

graphics_dt = np.dtype(
    [
        ("ch", np.int32), #Unicode Codepoint
        ("fg", "3B"), # 3 Unsigned bytes, for RGB colors.
        ("bg", "3B"),
    ]
)

tile_dt = np.dtype(
    [
        ("walkable", np.bool),
        ("transparent", np.bool),
        ("dark", graphics_dt), #Graphics when tile not in FOV
        ("light", graphics_dt), #Graphics when tile is in FOV
    ]
)

def new_tile(
        *, # Enforce keyword args
        walkable:int,
        transparent:int,
        dark: Tuple[int, Tuple[int,int,int], Tuple[int,int,int]],
        light: Tuple[int, Tuple[int,int,int], Tuple[int,int,int]],
) -> np.ndarray:
    '''Helper function for defining tile types'''
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)

#Shroud represents unexplored, unseen tiles
SHROUD = np.array((ord(" "), (255,255,255), (0,0,0)), dtype=graphics_dt)

floor = new_tile(
    walkable= True, 
    transparent= True, 
    dark=(ord(' '), (255,255,255), (0,100,0)),
    light=(ord(" "), (255,255,255), (100,200,100)),
)
wall = new_tile(
    walkable= False, 
    transparent= False, 
    dark=(ord(' '), (255,255,255), (0,0,100)),
    light=(ord(" "), (255,255,255), (100,100,200)),
)
down_stairs = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord('>'),(0,0,100),(50,50,150)),
    light=(ord('>'), (255,255,255), (200,180,50)),
)