import pyautogui
from typing import List, Optional, Self
import core.config as cfg
from core.dataholders.Point import Point
from core.helpers.gui_controllers.MouseMover import MouseMover


class PyAutoGUIMouseMover(MouseMover):
    def _initialize(cls):
        # Initialize any necessary configurations for pyautogui
        pyautogui.FAILSAFE = cfg.PAG_FAILSAFE  # Enable failsafe
        pyautogui.PAUSE = cfg.PAG_PAUSE  # Set a small pause between actions

    def move_to(self, coords: Point) -> Self:
        pyautogui.moveTo(coords.x, coords.y)
        return self

    def click(self, coords: Optional[Point] = None, click_type: str = "left") -> Self:
        if coords:
            self.move_to(coords)
        pyautogui.click(button=click_type)
        return self

    def click_left(self, coords: Optional[Point] = None) -> Self:
        return self.click(coords, "left")

    def click_right(self, coords: Optional[Point] = None) -> Self:
        return self.click(coords, "right")

    def click_middle(self, coords: Optional[Point] = None) -> Self:
        return self.click(coords, "middle")

    def scroll(self, amount: int, go_up: bool = True) -> Self:
        scroll_direction = 1 if go_up else -1
        pyautogui.scroll(amount * scroll_direction)
        return self

    def drag_to(self, coords: Point, duration: float) -> Self:
        pyautogui.dragTo(coords.x, coords.y, duration=duration, button="left")
        return self

    def mouse_up(self) -> Self:
        pyautogui.mouseUp()
        return self

    def mouse_down(self) -> Self:
        pyautogui.mouseDown()
        return self

    def type_write(self, text: str | List[str], interval: float = 0) -> Self:
        if isinstance(text, list):
            text = "".join(text)
        pyautogui.typewrite(text, interval=interval)
        return self

    def button_down(self, button: str) -> Self:
        pyautogui.mouseDown(button=button)
        return self

    def button_up(self, button: str) -> Self:
        pyautogui.mouseUp(button=button)
        return self

    def hotkey(self, *keys: str) -> Self:
        pyautogui.hotkey(*keys)
        return self
