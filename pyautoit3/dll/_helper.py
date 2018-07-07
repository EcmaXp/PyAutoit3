# noinspection PyUnresolvedReferences
import ctypes
# noinspection PyUnresolvedReferences
from ctypes import wintypes
# noinspection PyUnresolvedReferences
from typing import *

# noinspection PyUnresolvedReferences
from .api import API, AU3_INTDEFAULT
# noinspection PyUnresolvedReferences
from .bufsize import *
# noinspection PyUnresolvedReferences
from ..consts import *
# noinspection PyUnresolvedReferences
from ..types import *

SW_SHOWNORMAL = CommandShow.SW_SHOWNORMAL

shared_buffer_mode = True
last_buffer = None


def new_buffer_raw(buf_size):
    return ctypes.create_unicode_buffer(buf_size)


def new_buffer(buf_size):
    global last_buffer
    if not shared_buffer_mode:
        return new_buffer_raw(buf_size)

    if last_buffer is None:
        last_buffer = new_buffer_raw(buf_size)
    elif ctypes.sizeof(last_buffer) < buf_size:
        last_buffer = new_buffer_raw(buf_size)

    return last_buffer


def buffer_as_text(buf):
    return buf.value


def build_point(pointer: wintypes.LPPOINT) -> Point:
    return Point.from_wintypes(pointer)


def build_rect(pointer: wintypes.LPRECT) -> Rect:
    return Rect.from_wintypes(pointer)
