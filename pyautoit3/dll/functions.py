import ctypes
from ctypes import wintypes

from . import _functions as _au3
from ._functions import *
from ..types import *

__all__ = 'auto_it_set_option', 'clip_get', 'clip_put', 'control_click', 'control_click_by_handle', 'control_command', 'control_command_by_handle', 'control_disable', 'control_disable_by_handle', 'control_enable', 'control_enable_by_handle', 'control_focus', 'control_focus_by_handle', 'control_get_focus', 'control_get_focus_by_handle', 'control_get_handle', 'control_get_handle_as_text', 'control_get_pos', 'control_get_pos_by_handle', 'control_get_text', 'control_get_text_by_handle', 'control_hide', 'control_hide_by_handle', 'control_list_view', 'control_list_view_by_handle', 'control_move', 'control_move_by_handle', 'control_send', 'control_send_by_handle', 'control_set_text', 'control_set_text_by_handle', 'control_show', 'control_show_by_handle', 'control_tree_view', 'control_tree_view_by_handle', 'drive_map_add', 'drive_map_del', 'drive_map_get', 'error', 'init', 'is_admin', 'mouse_click', 'mouse_click_drag', 'mouse_down', 'mouse_get_cursor', 'mouse_get_pos', 'mouse_move', 'mouse_up', 'mouse_wheel', 'opt', 'pixel_checksum', 'pixel_get_color', 'pixel_search', 'process_close', 'process_exists', 'process_set_priority', 'process_wait', 'process_wait_close', 'run', 'run_as', 'run_as_wait', 'run_wait', 'send', 'shutdown', 'sleep', 'statusbar_get_text', 'statusbar_get_text_by_handle', 'tool_tip', 'win_activate', 'win_activate_by_handle', 'win_active', 'win_active_by_handle', 'win_close', 'win_close_by_handle', 'win_exists', 'win_exists_by_handle', 'win_get_caret_pos', 'win_get_class_list', 'win_get_class_list_by_handle', 'win_get_client_size', 'win_get_client_size_by_handle', 'win_get_handle', 'win_get_handle_as_text', 'win_get_pos', 'win_get_pos_by_handle', 'win_get_process', 'win_get_process_by_handle', 'win_get_state', 'win_get_state_by_handle', 'win_get_text', 'win_get_text_by_handle', 'win_get_title', 'win_get_title_by_handle', 'win_kill', 'win_kill_by_handle', 'win_menu_select_item', 'win_menu_select_item_by_handle', 'win_minimize_all', 'win_minimize_all_undo', 'win_move', 'win_move_by_handle', 'win_set_on_top', 'win_set_on_top_by_handle', 'win_set_state', 'win_set_state_by_handle', 'win_set_title', 'win_set_title_by_handle', 'win_set_trans', 'win_set_trans_by_handle', 'win_wait', 'win_wait_active', 'win_wait_active_by_handle', 'win_wait_by_handle', 'win_wait_close', 'win_wait_close_by_handle', 'win_wait_not_active', 'win_wait_not_active_by_handle'

BUFFER_SIZE_DEFAULT = 0x1000  # 4096
LONG_BUFFER_SIZE_DEFAULT = 0x10000  # 65536


def clip_get(buf_size: int = BUFFER_SIZE_DEFAULT) -> str:
    buffer = ctypes.create_unicode_buffer(buf_size)
    _au3.clip_get(buffer, buf_size)
    return buffer.value.rstrip('\0')


def mouse_get_pos() -> Point:
    point = wintypes.POINT()
    _au3.mouse_get_pos(point)
    return Point.from_wintypes(point)


def tool_tip_clear():
    _au3.tool_tip("")


def win_get_client_size_by_handle(hwnd: wintypes.HWND) -> Rect:
    rect = wintypes.RECT()
    _au3.win_get_client_size_by_handle(hwnd, rect)
    return Rect.from_wintypes(rect)


def win_get_caret_pos() -> Point:
    point = wintypes.POINT()
    _au3.win_get_caret_pos(point)
    return Point.from_wintypes(point)


def win_get_pos_by_handle(hwnd: wintypes.HWND) -> Rect:
    rect = wintypes.RECT()
    _au3.win_get_pos_by_handle(hwnd, rect)
    return Rect.from_wintypes(rect)


def win_get_text_by_handle(hwnd: wintypes.HWND, buf_size: int = LONG_BUFFER_SIZE_DEFAULT) -> str:
    buffer = ctypes.create_unicode_buffer(buf_size)
    _au3.win_get_text_by_handle(hwnd, buffer, buf_size)
    return buffer.value.rstrip('\0')


def win_get_title_by_handle(hwnd: wintypes.HWND, buf_size: int = BUFFER_SIZE_DEFAULT) -> str:
    buffer = ctypes.create_unicode_buffer(buf_size)
    _au3.win_get_title_by_handle(hwnd, buffer, buf_size)
    return buffer.value.rstrip('\0')
