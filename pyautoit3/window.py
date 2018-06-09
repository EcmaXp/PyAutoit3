from ctypes import c_void_p
from typing import Union

from pyautoit3.control import Control
from pyautoit3.internal.window import enum_windows
from .dll import functions as au3
from .types import Rect, Point


class Window:
    def __init__(self, hwnd: c_void_p):
        self.hwnd = hwnd

    @classmethod
    def find(cls, title, text=""):
        hwnd = au3.win_get_handle(title, text)
        return cls(hwnd)

    @classmethod
    def findall_raw(cls, title=None, class_name=None):
        for window in enum_windows():
            if title is not None:
                if window.title != title:
                    continue

            if class_name is not None:
                if window.class_name != class_name:
                    continue

            yield cls(window.hwnd)

    @classmethod
    def find_raw(cls, title=None, class_name=None):
        if title is None and class_name is None:
            raise ValueError

        for self in cls.findall_raw(title=title, class_name=class_name):
            return self

    """
    AU3_API int WINAPI AU3_WinActivateByHandle(HWND hWnd);
    AU3_API int WINAPI AU3_WinActiveByHandle(HWND hWnd);
    AU3_API int WINAPI AU3_WinCloseByHandle(HWND hWnd);
    AU3_API int WINAPI AU3_WinExistsByHandle(HWND hWnd);
    AU3_API void WINAPI AU3_WinGetClassListByHandle(HWND hWnd, LPWSTR szRetText, int nBufSize);
    AU3_API int WINAPI AU3_WinGetClientSizeByHandle(HWND hWnd, LPRECT lpRect);
    AU3_API void WINAPI AU3_WinGetHandleAsText(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText, LPWSTR szRetText, int nBufSize);
    AU3_API int WINAPI AU3_WinGetPosByHandle(HWND hWnd, LPRECT lpRect);
    AU3_API DWORD WINAPI AU3_WinGetProcessByHandle(HWND hWnd);
    AU3_API int WINAPI AU3_WinGetStateByHandle(HWND hWnd);
    AU3_API void WINAPI AU3_WinGetTextByHandle(HWND hWnd, LPWSTR szRetText, int nBufSize);
    AU3_API void WINAPI AU3_WinGetTitleByHandle(HWND hWnd, LPWSTR szRetText, int nBufSize);
    AU3_API int WINAPI AU3_WinKillByHandle(HWND hWnd);
    AU3_API int WINAPI AU3_WinMenuSelectItemByHandle(HWND hWnd, LPCWSTR szItem1, LPCWSTR szItem2, LPCWSTR szItem3, LPCWSTR szItem4, LPCWSTR szItem5, LPCWSTR szItem6, LPCWSTR szItem7, LPCWSTR szItem8);
    AU3_API int WINAPI AU3_WinMoveByHandle(HWND hWnd, int nX, int nY, int nWidth = -1, int nHeight = -1);
    AU3_API int WINAPI AU3_WinSetOnTopByHandle(HWND hWnd, int nFlag);
    AU3_API int WINAPI AU3_WinSetStateByHandle(HWND hWnd, int nFlags);
    AU3_API int WINAPI AU3_WinSetTitleByHandle(HWND hWnd, LPCWSTR szNewTitle);
    AU3_API int WINAPI AU3_WinSetTransByHandle(HWND hWnd, int nTrans);
    AU3_API int WINAPI AU3_WinWaitByHandle(HWND hWnd, int nTimeout);
    AU3_API int WINAPI AU3_WinWaitActiveByHandle(HWND hWnd, int nTimeout);
    AU3_API int WINAPI AU3_WinWaitCloseByHandle(HWND hWnd, int nTimeout);
    AU3_API int WINAPI AU3_WinWaitNotActiveByHandle(HWND hWnd, int nTimeout = 0);
    """

    def activate(self):
        au3.win_activate_by_handle(self.hwnd)

    def is_active(self) -> int:
        return au3.win_active_by_handle(self.hwnd)

    def close(self):
        au3.win_close_by_handle(self.hwnd)

    def is_exists(self) -> int:
        return au3.win_exists_by_handle(self.hwnd)

    def class_list(self) -> str:
        raise au3.win_get_class_list_by_handle(self.hwnd)

    def move(self, target: Union[Rect, Point]):
        if isinstance(target, Point):
            au3.win_move_by_handle(self.hwnd, target.x, target.y)
        elif isinstance(target, Rect):
            au3.win_move_by_handle(self.hwnd, target.left, target.top, target.width, target.height)
        else:
            raise TypeError

    def wait_active(self, timeout=0):
        au3.win_wait_active_by_handle(self.hwnd, timeout)

    def wait_not_active(self):
        au3.win_wait_not_active_by_handle(self.hwnd)

    @property
    def client_size(self) -> Rect:
        result, rect = au3.win_get_client_size_by_handle(self.hwnd)
        return rect

    @property
    def pos(self) -> Rect:
        result, rect = au3.win_get_pos_by_handle(self.hwnd)
        return rect

    @pos.setter
    def pos(self, rect: Union[Rect, Point]):
        self.move(rect)

    @property
    def state(self):
        return au3.win_get_state_by_handle(self.hwnd)

    @state.setter
    def state(self, state: int):
        au3.win_set_state_by_handle(self.hwnd, state)

    @property
    def text(self):
        return au3.win_get_text_by_handle(self.hwnd)

    @property
    def title(self) -> str:
        return au3.win_get_title_by_handle(self.hwnd)

    @title.setter
    def title(self, title: str):
        au3.win_set_title_by_handle(self.hwnd, title)

    @property
    def active_control(self) -> Control:
        return Control.find_active(self)

    def __repr__(self):
        if self.hwnd is not None:
            return f"<{type(self).__name__}: {self.title}>"
