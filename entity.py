from __future__ import annotations
import copy
from typing import Tuple, TypeVar, TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from game_map import GameMap
T = TypeVar("T", bound="Entity")

class Entity:
    '''A generic class for representing entities'''
    gamemap: GameMap

    def __init__(self, gamemap:Optional[GameMap]=None, x:int=0, y:int=0, 
                 char:str="?", color:Tuple[int,int,int]=(255,255,255),
                 name="<Unnamed>", blocks_movement:bool=False,):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks_movement = blocks_movement
        if gamemap:
            #If gamemap isn't provided now then it will be later
            self.gamemap=gamemap
            gamemap.entities.add(self)

    def spawn(self: T, gamemap: GameMap, x: int, y: int) -> T:
        """Spawns a copy of T at the given location"""
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        clone.gamemap = gamemap
        gamemap.entities.add(clone)
        return clone
    
    def place(self, x:int, y:int, gamemap:Optional[GameMap]=None) -> None:
        "Place this entity at a new location, handles moving across GameMaps"
        self.x = x 
        self.y = y
        if gamemap:
            if hasattr(self, "gamemap"): #Possibly uninitialised
                self.gamemap.entities.remove(self)
            self.gamemap = gamemap
            gamemap.entities.add(self)

    def move(self, dx:int, dy:int) -> None:
        # Moves the entity
        self.x += dx
        self.y += dy
        