from __future__ import annotations
from typing import TYPE_CHECKING, Tuple
import color
if TYPE_CHECKING:
    from tcod.console import Console
    from engine import Engine
    from game_map import GameMap

def get_names_at_location(x:int,y:int,game_map:GameMap) -> str:
    if not game_map.in_bounds(x,y) or not game_map.visible[x,y]:
        return ""
    
    names = ", ".join(
        entity.name for entity in game_map.entities if entity.x == x and entity.y == y
    )

    return names.capitalize()

def render_bar(
        console: Console, current_value: int, max_value: int, total_width: int, x:int=0,y:int=45
) -> None:
    bar_width = int(float(current_value) / max_value * total_width)
    console.draw_rect(x=x,y=y,width=total_width,height=1,ch=1,bg=color.bar_empty)

    if bar_width > 0:
        console.draw_rect(
            x=x,y=y,width=bar_width,height=1,ch=1,bg=color.bar_filled
        )
        console.print(
            x=x+1,y=y,text=f"HP: {current_value}/{max_value}", fg=color.bar_text
        )

def render_exp_bar(
        console: Console, engine: Engine, total_width: int, x:int=0,y:int=47,
) -> None:
    bar_width = int (engine.player.level.current_xp / engine.player.level.experience_to_next_level * total_width)
    console.draw_rect(x=x,y=y,width=total_width,height=1,ch=1,bg=color.bar_empty)

    if bar_width > 0:
        console.draw_rect(
            x=x,y=y,width=bar_width,height=1,ch=1,bg=color.exp_filled
        )
        console.print(
            x=x+1,y=y,text=f"LVL:{engine.player.level.current_level}" 
            f"({int(engine.player.level.current_xp/engine.player.level.experience_to_next_level*100)}%)",
            fg=color.bar_text
        )


def render_dungeon_level(
        console: Console, dungeon_level:int, location: Tuple[int,int]
) -> None:
    """
    Render the level the player is current on, at the given location.
    """
    x, y = location
    console.print(x=x,y=y, text=f"Current Floor: {dungeon_level}")

def render_names_at_mouse_location(
        console: Console, x:int, y:int, engine:Engine
) -> None:
    mouse_x, mouse_y = engine.mouse_location

    names_at_mouse_location = get_names_at_location(
        x=int(mouse_x),y=int(mouse_y), game_map=engine.game_map
    )

    console.print(x=x,y=y, text=names_at_mouse_location)