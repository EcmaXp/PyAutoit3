from .consts import MouseButtonType
from .consts import MouseWheelDirectionType
from .dll import functions as au3
from .dll.api import AU3_INTDEFAULT
from .types import Point

DEFAULT_POINT = Point(
    x=AU3_INTDEFAULT,
    y=AU3_INTDEFAULT,
)


class MouseButton:

    def __init__(self, button: MouseButtonType):
        self.button = button

    def __call__(self, p: Point = None, clicks=1, speed=None):
        self.click(p, clicks, speed)

    def click(self, p: Point = None, clicks: int=1, speed: int=None):
        if p is None:
            p = DEFAULT_POINT

        if speed is None:
            speed = -1

        return au3.mouse_click(self.button, p.x, p.y, clicks, speed)

    def click_drag(self, p1: Point, p2: Point, speed=None):
        if speed is None:
            speed = -1

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
        super().__init__(MouseButtonType.Middle)

    def wheel(self, direction: MouseWheelDirectionType, clicks):
        au3.mouse_wheel(direction, clicks)

    def wheel_up(self, clicks):
        self.wheel(MouseWheelDirectionType.Up, clicks)

    def wheel_down(self, clicks):
        self.wheel(MouseWheelDirectionType.Down, clicks)


class MouseType:
    left = MouseButton(MouseButtonType.Left)
    right = MouseButton(MouseButtonType.Right)
    middle = wheel = MouseWheelButton()
    main = MouseButton(MouseButtonType.Main)
    menu = MouseButton(MouseButtonType.Menu)
    primary = MouseButton(MouseButtonType.Primary)
    secondary = MouseButton(MouseButtonType.Secondary)

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
        return au3.tool_tip_clear()

Mouse = MouseType()
