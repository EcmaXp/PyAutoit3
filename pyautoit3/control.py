import typing
from ctypes import c_void_p
from typing import Union

from .consts import ClickType, Command
from .dll import functions as au3
from .types import DEFAULT_POINT, Point, Rect

if typing.TYPE_CHECKING:
    from . import Window


class Control:
    def __init__(self, window: "Window", hctrl: c_void_p):
        self.window = window
        self.hctrl = hctrl

    @property
    def hwnd(self):
        return self.window.hwnd

    @classmethod
    def find(cls, window: "Window", control_text=""):
        hctrl = au3.control_get_handle(window.hwnd, control_text)
        return cls(window, hctrl)

    @classmethod
    def find_active(cls, window: "Window"):
        sctrl = au3.control_get_focus_by_handle(window.hwnd)
        return cls.find(window, sctrl)

    def click(self, button: ClickType, clicks: int = 1, point: Point = DEFAULT_POINT):
        return au3.control_click_by_handle(self.hwnd, self.hctrl, button, clicks, point.x, point.y)

    def command(self, command: Union[Command, str], option: str = ""):
        return au3.control_command_by_handle(self.hwnd, self.hctrl, command, option)

    def enable(self):
        return au3.control_enable_by_handle(self.hwnd, self.hctrl)

    def disable(self):
        return au3.control_disable_by_handle(self.hwnd, self.hctrl)

    def focus(self):
        return au3.control_focus_by_handle(self.hwnd, self.hctrl)

    def hide(self):
        return au3.control_hide_by_handle(self.hwnd, self.hctrl)

    def move(self, target: Union[Point, Rect]):
        if isinstance(target, Point):
            au3.control_move_by_handle(self.hwnd, self.hctrl, target.x, target.y)
        elif isinstance(target, Rect):
            au3.control_move_by_handle(self.hwnd, self.hctrl, target.left, target.top, target.width, target.height)
        else:
            raise TypeError

    def show(self):
        return au3.control_show_by_handle(self.hwnd, self.hctrl)

    def send(self, text):
        return au3.control_send_by_handle(self.hwnd, self.hctrl, text)

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

    """
    AU3_API int WINAPI AU3_ControlClickByHandle(HWND hWnd, HWND hCtrl, LPCWSTR szButton, int nNumClicks, int nX = AU3_INTDEFAULT, int nY = AU3_INTDEFAULT);
    AU3_API void WINAPI AU3_ControlCommandByHandle(HWND hWnd, HWND hCtrl, LPCWSTR szCommand, LPCWSTR szExtra, LPWSTR szResult, int nBufSize);
    AU3_API void WINAPI AU3_ControlListViewByHandle(HWND hWnd, HWND hCtrl, LPCWSTR szCommand, LPCWSTR szExtra1, LPCWSTR szExtra2, LPWSTR szResult, int nBufSize);
    AU3_API int WINAPI AU3_ControlDisableByHandle(HWND hWnd, HWND hCtrl);
    AU3_API int WINAPI AU3_ControlEnableByHandle(HWND hWnd, HWND hCtrl);
    AU3_API int WINAPI AU3_ControlFocusByHandle(HWND hWnd, HWND hCtrl);
    AU3_API void WINAPI AU3_ControlGetFocusByHandle(HWND hWnd, LPWSTR szControlWithFocus, int nBufSize);
    AU3_API HWND WINAPI AU3_ControlGetHandle(HWND hWnd, LPCWSTR szControl);
    AU3_API void WINAPI AU3_ControlGetHandleAsText(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText, LPCWSTR szControl, LPWSTR szRetText, int nBufSize);
    AU3_API int WINAPI AU3_ControlGetPosByHandle(HWND hWnd, HWND hCtrl, LPRECT lpRect);
    AU3_API void WINAPI AU3_ControlGetTextByHandle(HWND hWnd, HWND hCtrl, LPWSTR szControlText, int nBufSize);
    AU3_API int WINAPI AU3_ControlHideByHandle(HWND hWnd, HWND hCtrl);
    AU3_API int WINAPI AU3_ControlMoveByHandle(HWND hWnd, HWND hCtrl, int nX, int nY, int nWidth = -1, int nHeight = -1);
    AU3_API int WINAPI AU3_ControlSendByHandle(HWND hWnd, HWND hCtrl, LPCWSTR szSendText, int nMode = 0);
    AU3_API int WINAPI AU3_ControlSetTextByHandle(HWND hWnd, HWND hCtrl, LPCWSTR szControlText);
    AU3_API int WINAPI AU3_ControlShowByHandle(HWND hWnd, HWND hCtrl);
    AU3_API void WINAPI AU3_ControlTreeViewByHandle(HWND hWnd, HWND hCtrl, LPCWSTR szCommand, LPCWSTR szExtra1, LPCWSTR szExtra2, LPWSTR szResult, int nBufSize);
    """
