from typing import Optional
import tcod.event
from actions import Action, EscapeAction, BumpAction

class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        if key == tcod.event.KeySym.W:
            action = BumpAction(dx=0, dy=-1)
        elif key == tcod.event.KeySym.S:
            action = BumpAction(dx=0, dy=1)
        elif key == tcod.event.KeySym.D:
            action = BumpAction(dx=1, dy=0)
        elif key == tcod.event.KeySym.A:
            action = BumpAction(dx=-1, dy=0)
        elif key == tcod.event.KeySym.ESCAPE:
            action = EscapeAction()
        return action