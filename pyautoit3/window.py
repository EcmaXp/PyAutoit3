from ctypes import c_void_p
from typing import Union, List, Optional

from . import au3
from .control import Control
from .exception import AutoitError
from .internal.window import enum_windows
from .process import Process
from .types import Rect, Point


class Window:
    def __init__(self, hwnd: c_void_p):
        self.hwnd = hwnd

    @classmethod
    def find(cls, title, text="") -> Optional["Window"]:
        try:
            hwnd = au3.win_get_handle(title, text)
        except AutoitError as e:
            if e.code == 1:
                return None

            raise
        else:
            return cls(hwnd)

    @classmethod
    def exists(cls, title, text="") -> bool:
        return bool(au3.win_exists(title, text))

    @classmethod
    def get_active_window(cls):
        return cls.find("[ACTIVE]")

    @classmethod
    def findall_raw(cls, *, title=None, class_name=None, pid=None):
        for window in enum_windows():
            if pid is not None:
                if window.pid != pid:
                    continue

            if title is not None:
                if window.title != title:
                    continue

            if class_name is not None:
                if window.class_name != class_name:
                    continue

            yield cls(window.hwnd)

    @classmethod
    def find_raw(cls, *, title=None, class_name=None):
        if title is None and class_name is None:
            raise ValueError

        for self in cls.findall_raw(title=title, class_name=class_name):
            return self

    def activate(self):
        au3.win_activate_by_handle(self.hwnd)

    def is_active(self) -> int:
        return au3.win_active_by_handle(self.hwnd)

    def is_exists(self) -> int:
        return au3.win_exists_by_handle(self.hwnd)

    def close(self):
        au3.win_close_by_handle(self.hwnd)

    def kill(self):
        au3.win_kill_by_handle(self.hwnd)

    def move(self, target: Union[Rect, Point]):
        if isinstance(target, Point):
            au3.win_move_by_handle(self.hwnd, target.x, target.y)
        elif isinstance(target, Rect):
            au3.win_move_by_handle(self.hwnd, target.left, target.top, target.width, target.height)
        else:
            raise TypeError

    def menu_select_item(self, *items: str):
        if len(items) > 8:
            raise Exception

        au3.win_menu_select_item_by_handle(self.hwnd, *items)

    def set_on_top(self, flag):
        au3.win_set_on_top_by_handle(self.hwnd, flag)

    def wait(self, timeout=0):
        au3.win_wait_by_handle(self.hwnd, timeout)

    def wait_active(self, timeout=0):
        au3.win_wait_active_by_handle(self.hwnd, timeout)

    def wait_not_active(self):
        au3.win_wait_not_active_by_handle(self.hwnd)

    def wait_close(self, timeout=0):
        au3.win_wait_close_by_handle(self.hwnd, timeout)

    def find_control(self, control_text) -> Control:
        return Control.find(self, control_text)

    def __getitem__(self, control_text) -> Control:
        control = self.find_control(control_text)
        if control is None:
            raise KeyError(control_text)

        return control

    @property
    def title(self) -> str:
        return au3.win_get_title_by_handle(self.hwnd)

    @title.setter
    def title(self, title: str):
        au3.win_set_title_by_handle(self.hwnd, title)

    @property
    def text(self):
        return au3.win_get_text_by_handle(self.hwnd)

    @property
    def class_list(self) -> List[str]:
        return au3.win_get_class_list_by_handle(self.hwnd).splitlines()

    @property
    def pos(self) -> Rect:
        result, rect = au3.win_get_pos_by_handle(self.hwnd)
        return rect

    @pos.setter
    def pos(self, rect: Union[Rect, Point]):
        self.move(rect)

    @property
    def client_size(self) -> Rect:
        result, rect = au3.win_get_client_size_by_handle(self.hwnd)
        return rect

    @property
    def state(self):
        return au3.win_get_state_by_handle(self.hwnd)

    @state.setter
    def state(self, state: int):
        au3.win_set_state_by_handle(self.hwnd, state)

    @property
    def active_control(self) -> Control:
        return Control.find_active(self)

    @property
    def process(self) -> Process:
        pid = au3.win_get_process_by_handle(self.hwnd)
        return Process(pid)

    def __repr__(self):
        if self.hwnd is not None:
            return f"<{type(self).__name__}: {self.title!r}>"
