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
        ("dark", graphics_dt),
    ]
)

def new_tile(
        *, # Enforce keyword args
        walkable:int,
        transparent:int,
        dark: Tuple[int, Tuple[int,int,int], tuple[int,int,int]],
) -> np.ndarray:
    '''Helper function for defining tile types'''
    return np.array((walkable, transparent, dark), dtype=tile_dt)

floor = new_tile(
    walkable= True, transparent= True, dark=(ord(' '), (255,255,255), (0,100,0)),
)
wall = new_tile(
    walkable= False, transparent= False, dark=(ord(' '), (255,255,255), (0,0,100))
)