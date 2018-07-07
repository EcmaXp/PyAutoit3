import ctypes
from ctypes import wintypes
from typing import List

from dataclasses import dataclass

__all__ = "enum_windows",

WNDENUMPROC = ctypes.WINFUNCTYPE(wintypes.BOOL,
                                 wintypes.HWND,
                                 wintypes.LPARAM)
user32 = ctypes.windll.user32
user32.EnumWindows.argtypes = [
    WNDENUMPROC,
    wintypes.LPARAM]
user32.GetWindowTextLengthW.argtypes = [
    wintypes.HWND]
user32.GetWindowTextW.argtypes = [
    wintypes.HWND,
    wintypes.LPWSTR,
    ctypes.c_int]
user32.GetClassNameW.argtypes = [
    wintypes.HWND,
    wintypes.LPWSTR,
    ctypes.c_int]


@dataclass
class RawWindow:
    hwnd: wintypes.HWND

    @property
    def pid(self) -> int:
        pid = ctypes.c_ulong(0)
        user32.GetWindowThreadProcessId(self.hwnd, ctypes.byref(pid))
        return pid.value

    @property
    def title(self) -> str:
        length = user32.GetWindowTextLengthW(self.hwnd) + 1
        buffer = ctypes.create_unicode_buffer(length)
        user32.GetWindowTextW(self.hwnd, buffer, length)
        return buffer.value

    @property
    def class_name(self) -> str:
        length = 1024
        buffer = ctypes.create_unicode_buffer(length)
        user32.GetClassNameW(self.hwnd, buffer, length)
        return buffer.value


def enum_windows() -> List[RawWindow]:
    result = []

    def worker(hwnd, _):
        result.append(RawWindow(hwnd))
        return True

    cb_worker = WNDENUMPROC(worker)

    if not user32.EnumWindows(cb_worker, 1):
        raise ctypes.WinError()

    return result
