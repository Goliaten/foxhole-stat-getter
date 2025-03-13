from typing import List, Optional, Self, final
from core.dataholders.Point import Point
import core.config as cfg
from core.helpers.BaseHelper import BaseHelper

# To be fair, I could say eh, and implement the pyautogio class here.
# But i'm thinking of maybe using it in future for different autmation purpose.
# And they i'll probably use the win32 something module.
# So a frontface class will make life easier later.


class MouseMover(BaseHelper):
    _instance: Optional["MouseMover"] = None

    def move_to(self, coords: Point) -> Self:
        # Move to the coords
        return self

    def click(self, coords: Optional[Point] = None, click_type: str = "left") -> Self:
        # if x and y supplied click at those coords
        # if none supplies, click where cursor at
        # (?)if only one supplied, move then click at one axis
        return self

    def click_left(self, coords: Optional[Point] = None) -> Self:
        # this also has to be overloaded
        # should call Self.click(), with left mouse button
        return self

    def click_right(self, coords: Optional[Point] = None) -> Self:
        # this also has to be overloaded
        # should call Self.click(), with right mouse button
        return self

    def click_middle(self, coords: Optional[Point] = None) -> Self:
        # this also has to be overloaded
        # should call Self.click(), with middle mouse button
        return self

    def scroll(self, amount: int, go_up: bool = True) -> Self:
        return self

    def drag_to(self, coords: Point, duration: float) -> Self:
        return self

    def mouse_up(self) -> Self:
        return self

    def mouse_down(self) -> Self:
        return self

    def type_write(
        self, text: str | List[str], interval: float = cfg.MM_TYPEWRITE_INTERVAL
    ) -> Self:
        # maybe instead of List[str], it should be some special type?
        return self

    def button_down(self, button: str) -> Self:
        return self

    def button_up(self, button: str) -> Self:
        return self

    def hotkey(self, *keys: str) -> Self:

        return self

    # Above methods should be overloaded,
    # with implementation depending on type of gui handler
    # Methods below use the afforementioned.

    @final
    def open_f1(self):
        self.type_write(["f1"])

    @final
    def close_f1(self):
        self.type_write(["esc"])

    @final
    def open_activity_log(self, index: int) -> None:
        temp_location: Point = Point(x=100, y=100)
        # TODO - implement some way of parametrisation.
        # In order for this to work in every resolution and interface scale.
        self.click_right(
            temp_location,
        ).click_left(temp_location)
        pass

    @final
    def close_activity_log(self) -> None:
        self.type_write(["esc"])

    @final
    def scroll_one_player(self) -> None:
        temp_scroll = 35
        # TODO - needs parametrisation
        self.scroll(temp_scroll)

    @final
    def open_violation_log(self, index) -> None:
        # tbf, optional. Stat getter is meant to be activity scraper.
        pass
