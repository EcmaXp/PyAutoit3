import typing
from ctypes import c_void_p
from typing import Union

from . import au3
from .consts import Click, Command
from .exception import AutoitError
from .types import DEFAULT_POINT, Point, Rect

if typing.TYPE_CHECKING:
    from . import Window

__all__ = "Control",


class Control:
    def __init__(self, window: "Window", hctrl: c_void_p):
        self.window = window
        self.hctrl = hctrl

    @property
    def hwnd(self):
        return self.window.hwnd

    @classmethod
    def find(cls, window: "Window", control_text=""):
        try:
            hctrl = au3.control_get_handle(window.hwnd, control_text)
        except AutoitError as e:
            if e.code == 1:
                return None

            raise
        else:
            return cls(window, hctrl)

    @classmethod
    def find_active(cls, window: "Window"):
        sctrl = au3.control_get_focus_by_handle(window.hwnd)
        return cls.find(window, sctrl)

    def click(self, button: Click = Click.Primary, clicks: int = 1, point: Point = DEFAULT_POINT):
        return au3.control_click_by_handle(self.hwnd, self.hctrl, button, clicks, point.x, point.y)

    def focus(self):
        return au3.control_focus_by_handle(self.hwnd, self.hctrl)

    def command(self, command: Union[Command, str], option: str = ""):
        return au3.control_command_by_handle(self.hwnd, self.hctrl, command, option)

    def send(self, text):
        return au3.control_send_by_handle(self.hwnd, self.hctrl, text)

    def enable(self):
        return au3.control_enable_by_handle(self.hwnd, self.hctrl)

    def disable(self):
        return au3.control_disable_by_handle(self.hwnd, self.hctrl)

    def show(self):
        return au3.control_show_by_handle(self.hwnd, self.hctrl)

    def hide(self):
        return au3.control_hide_by_handle(self.hwnd, self.hctrl)

    def move(self, target: Union[Point, Rect]):
        if isinstance(target, Point):
            au3.control_move_by_handle(self.hwnd, self.hctrl, target.x, target.y)
        elif isinstance(target, Rect):
            au3.control_move_by_handle(self.hwnd, self.hctrl, target.left, target.top, target.width, target.height)
        else:
            raise TypeError

    def list_view(self, command: str, extra1: str, extra2: str):
        return au3.control_list_view_by_handle(self.hwnd, self.hctrl, command, extra1, extra2)

    def tree_view(self, command: str, extra1: str, extra2: str):
        return au3.control_tree_view_by_handle(self.hwnd, self.hctrl, command, extra1, extra2)

    @property
    def pos(self) -> Rect:
        result, rect = au3.control_get_pos_by_handle(self.hwnd, self.hctrl)
        return rect

    @pos.setter
    def pos(self, rect: Union[Rect, Point]):
        self.move(rect)

    @property
    def text(self):
        return au3.control_get_text_by_handle(self.hwnd, self.hctrl)

    @text.setter
    def text(self, text: str):
        au3.control_set_text_by_handle(self.hwnd, self.hctrl, text)

