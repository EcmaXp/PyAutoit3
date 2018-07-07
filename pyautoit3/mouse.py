from . import au3
from .consts import Click, MouseWheelDirection
from .types import Point, DEFAULT_POINT

__all__ = "Mouse",


class MouseButton:
    def __init__(self, button: Click):
        self.button = button

    def __call__(self, p: Point = DEFAULT_POINT, clicks=1, speed=-1):
        self.click(p, clicks, speed)

    def click(self, p: Point = DEFAULT_POINT, clicks: int = 1, speed: int = -1):
        return au3.mouse_click(self.button, p.x, p.y, clicks, speed)

    def click_drag(self, p1: Point, p2: Point, speed=-1):
        return au3.mouse_click_drag(self.button, p1.x, p1.y, p2.x, p2.y, speed)

    def down(self):
        return au3.mouse_down(self.button)

    def up(self):
        return au3.mouse_up(self.button)

    def __enter__(self):
        self.down()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.up()


class MouseWheelButton(MouseButton):
    def __init__(self):
        super().__init__(Click.Middle)

    def wheel(self, direction: MouseWheelDirection, clicks):
        au3.mouse_wheel(direction, clicks)

    def wheel_up(self, clicks):
        self.wheel(MouseWheelDirection.Up, clicks)

    def wheel_down(self, clicks):
        self.wheel(MouseWheelDirection.Down, clicks)


class MouseType:
    left = MouseButton(Click.Left)
    right = MouseButton(Click.Right)
    middle = wheel = MouseWheelButton()
    main = MouseButton(Click.Main)
    menu = MouseButton(Click.Menu)
    primary = MouseButton(Click.Primary)
    secondary = MouseButton(Click.Secondary)

    @property
    def pos(self) -> Point:
        return au3.mouse_get_pos()

    def move(self, p: Point, speed=None):
        if speed is None:
            speed = -1

        return au3.mouse_move(p.x, p.y, speed)

    def tool_tip(self, tip: str):
        return au3.tool_tip(tip)

    def tool_tip_clear(self):
        return au3.tool_tip("")

    @property
    def cursor(self):
        return au3.mouse_get_cursor()


Mouse = MouseType()
