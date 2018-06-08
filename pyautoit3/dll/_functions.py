from .api import API, AU3_INTDEFAULT
from pyautoit3.consts import *
from ctypes import wintypes

__all__ = ['init', 'error', 'auto_it_set_option', 'clip_get', 'clip_put', 'control_click', 'control_click_by_handle',
           'control_command', 'control_command_by_handle', 'control_list_view', 'control_list_view_by_handle',
           'control_disable', 'control_disable_by_handle', 'control_enable', 'control_enable_by_handle',
           'control_focus', 'control_focus_by_handle', 'control_get_focus', 'control_get_focus_by_handle',
           'control_get_handle', 'control_get_handle_as_text', 'control_get_pos', 'control_get_pos_by_handle',
           'control_get_text', 'control_get_text_by_handle', 'control_hide', 'control_hide_by_handle', 'control_move',
           'control_move_by_handle', 'control_send', 'control_send_by_handle', 'control_set_text',
           'control_set_text_by_handle', 'control_show', 'control_show_by_handle', 'control_tree_view',
           'control_tree_view_by_handle', 'drive_map_add', 'drive_map_del', 'drive_map_get', 'is_admin', 'mouse_click',
           'mouse_click_drag', 'mouse_down', 'mouse_get_cursor', 'mouse_get_pos', 'mouse_move', 'mouse_up',
           'mouse_wheel', 'opt', 'pixel_checksum', 'pixel_get_color', 'pixel_search', 'process_close', 'process_exists',
           'process_set_priority', 'process_wait', 'process_wait_close', 'run', 'run_wait', 'run_as', 'run_as_wait',
           'send', 'shutdown', 'sleep', 'statusbar_get_text', 'statusbar_get_text_by_handle', 'tool_tip',
           'win_activate', 'win_activate_by_handle', 'win_active', 'win_active_by_handle', 'win_close',
           'win_close_by_handle', 'win_exists', 'win_exists_by_handle', 'win_get_caret_pos', 'win_get_class_list',
           'win_get_class_list_by_handle', 'win_get_client_size', 'win_get_client_size_by_handle', 'win_get_handle',
           'win_get_handle_as_text', 'win_get_pos', 'win_get_pos_by_handle', 'win_get_process',
           'win_get_process_by_handle', 'win_get_state', 'win_get_state_by_handle', 'win_get_text',
           'win_get_text_by_handle', 'win_get_title', 'win_get_title_by_handle', 'win_kill', 'win_kill_by_handle',
           'win_menu_select_item', 'win_menu_select_item_by_handle', 'win_minimize_all', 'win_minimize_all_undo',
           'win_move', 'win_move_by_handle', 'win_set_on_top', 'win_set_on_top_by_handle', 'win_set_state',
           'win_set_state_by_handle', 'win_set_title', 'win_set_title_by_handle', 'win_set_trans',
           'win_set_trans_by_handle', 'win_wait', 'win_wait_by_handle', 'win_wait_active', 'win_wait_active_by_handle',
           'win_wait_close', 'win_wait_close_by_handle', 'win_wait_not_active', 'win_wait_not_active_by_handle']


def init() -> None:
    return API.AU3_Init()


def error() -> int:
    return API.AU3_error()


def auto_it_set_option(option: str, value: int) -> int:
    return API.AU3_AutoItSetOption(option, value)


def clip_get(clip: str, buf_size: int) -> None:
    return API.AU3_ClipGet(clip, buf_size)


def clip_put(clip: str) -> None:
    return API.AU3_ClipPut(clip)


def control_click(title: str, text: str, control: str, button: str, num_clicks: int, x: int = AU3_INTDEFAULT,
                  y: int = AU3_INTDEFAULT) -> int:
    return API.AU3_ControlClick(title, text, control, button, num_clicks, x, y)


def control_click_by_handle(hwnd: wintypes.HWND, ctrl: wintypes.HWND, button: str, num_clicks: int,
                            x: int = AU3_INTDEFAULT, y: int = AU3_INTDEFAULT) -> int:
    return API.AU3_ControlClickByHandle(hwnd, ctrl, button, num_clicks, x, y)


def control_command(title: str, text: str, control: str, command: str, extra: str, result: str, buf_size: int) -> None:
    return API.AU3_ControlCommand(title, text, control, command, extra, result, buf_size)


def control_command_by_handle(hwnd: wintypes.HWND, ctrl: wintypes.HWND, command: str, extra: str, result: str,
                              buf_size: int) -> None:
    return API.AU3_ControlCommandByHandle(hwnd, ctrl, command, extra, result, buf_size)


def control_list_view(title: str, text: str, control: str, command: str, extra1: str, extra2: str, result: str,
                      buf_size: int) -> None:
    return API.AU3_ControlListView(title, text, control, command, extra1, extra2, result, buf_size)


def control_list_view_by_handle(hwnd: wintypes.HWND, ctrl: wintypes.HWND, command: str, extra1: str, extra2: str,
                                result: str, buf_size: int) -> None:
    return API.AU3_ControlListViewByHandle(hwnd, ctrl, command, extra1, extra2, result, buf_size)


def control_disable(title: str, text: str, control: str) -> int:
    return API.AU3_ControlDisable(title, text, control)


def control_disable_by_handle(hwnd: wintypes.HWND, ctrl: wintypes.HWND) -> int:
    return API.AU3_ControlDisableByHandle(hwnd, ctrl)


def control_enable(title: str, text: str, control: str) -> int:
    return API.AU3_ControlEnable(title, text, control)


def control_enable_by_handle(hwnd: wintypes.HWND, ctrl: wintypes.HWND) -> int:
    return API.AU3_ControlEnableByHandle(hwnd, ctrl)


def control_focus(title: str, text: str, control: str) -> int:
    return API.AU3_ControlFocus(title, text, control)


def control_focus_by_handle(hwnd: wintypes.HWND, ctrl: wintypes.HWND) -> int:
    return API.AU3_ControlFocusByHandle(hwnd, ctrl)


def control_get_focus(title: str, text: str, control_with_focus: str, buf_size: int) -> None:
    return API.AU3_ControlGetFocus(title, text, control_with_focus, buf_size)


def control_get_focus_by_handle(hwnd: wintypes.HWND, control_with_focus: str, buf_size: int) -> None:
    return API.AU3_ControlGetFocusByHandle(hwnd, control_with_focus, buf_size)


def control_get_handle(hwnd: wintypes.HWND, control: str) -> wintypes.HWND:
    return API.AU3_ControlGetHandle(hwnd, control)


def control_get_handle_as_text(title: str, text: str = '', control: str = '', ret_text: str = '',
                               buf_size: int = AU3_INTDEFAULT) -> None:
    return API.AU3_ControlGetHandleAsText(title, text, control, ret_text, buf_size)


def control_get_pos(title: str, text: str, control: str, rect: wintypes.LPRECT) -> int:
    return API.AU3_ControlGetPos(title, text, control, rect)


def control_get_pos_by_handle(hwnd: wintypes.HWND, ctrl: wintypes.HWND, rect: wintypes.LPRECT) -> int:
    return API.AU3_ControlGetPosByHandle(hwnd, ctrl, rect)


def control_get_text(title: str, text: str, control: str, control_text: str, buf_size: int) -> None:
    return API.AU3_ControlGetText(title, text, control, control_text, buf_size)


def control_get_text_by_handle(hwnd: wintypes.HWND, ctrl: wintypes.HWND, control_text: str, buf_size: int) -> None:
    return API.AU3_ControlGetTextByHandle(hwnd, ctrl, control_text, buf_size)


def control_hide(title: str, text: str, control: str) -> int:
    return API.AU3_ControlHide(title, text, control)


def control_hide_by_handle(hwnd: wintypes.HWND, ctrl: wintypes.HWND) -> int:
    return API.AU3_ControlHideByHandle(hwnd, ctrl)


def control_move(title: str, text: str, control: str, x: int, y: int, width: int = -1, height: int = -1) -> int:
    return API.AU3_ControlMove(title, text, control, x, y, width, height)


def control_move_by_handle(hwnd: wintypes.HWND, ctrl: wintypes.HWND, x: int, y: int, width: int = -1,
                           height: int = -1) -> int:
    return API.AU3_ControlMoveByHandle(hwnd, ctrl, x, y, width, height)


def control_send(title: str, text: str, control: str, send_text: str, mode: int = 0) -> int:
    return API.AU3_ControlSend(title, text, control, send_text, mode)


def control_send_by_handle(hwnd: wintypes.HWND, ctrl: wintypes.HWND, send_text: str, mode: int = 0) -> int:
    return API.AU3_ControlSendByHandle(hwnd, ctrl, send_text, mode)


def control_set_text(title: str, text: str, control: str, control_text: str) -> int:
    return API.AU3_ControlSetText(title, text, control, control_text)


def control_set_text_by_handle(hwnd: wintypes.HWND, ctrl: wintypes.HWND, control_text: str) -> int:
    return API.AU3_ControlSetTextByHandle(hwnd, ctrl, control_text)


def control_show(title: str, text: str, control: str) -> int:
    return API.AU3_ControlShow(title, text, control)


def control_show_by_handle(hwnd: wintypes.HWND, ctrl: wintypes.HWND) -> int:
    return API.AU3_ControlShowByHandle(hwnd, ctrl)


def control_tree_view(title: str, text: str, control: str, command: str, extra1: str, extra2: str, result: str,
                      buf_size: int) -> None:
    return API.AU3_ControlTreeView(title, text, control, command, extra1, extra2, result, buf_size)


def control_tree_view_by_handle(hwnd: wintypes.HWND, ctrl: wintypes.HWND, command: str, extra1: str, extra2: str,
                                result: str, buf_size: int) -> None:
    return API.AU3_ControlTreeViewByHandle(hwnd, ctrl, command, extra1, extra2, result, buf_size)


def drive_map_add(device: str, share: str, flags: int, user: str = '', pwd: str = '', result: str = '',
                  buf_size: int = AU3_INTDEFAULT) -> None:
    return API.AU3_DriveMapAdd(device, share, flags, user, pwd, result, buf_size)


def drive_map_del(device: str) -> int:
    return API.AU3_DriveMapDel(device)


def drive_map_get(device: str, mapping: str, buf_size: int) -> None:
    return API.AU3_DriveMapGet(device, mapping, buf_size)


def is_admin() -> int:
    return API.AU3_IsAdmin()


def mouse_click(button: str = 'LEFT', x: int = AU3_INTDEFAULT, y: int = AU3_INTDEFAULT, clicks: int = 1,
                speed: int = -1) -> int:
    return API.AU3_MouseClick(button, x, y, clicks, speed)


def mouse_click_drag(button: str, x1: int, y1: int, x2: int, y2: int, speed: int = -1) -> int:
    return API.AU3_MouseClickDrag(button, x1, y1, x2, y2, speed)


def mouse_down(button: str = 'LEFT') -> None:
    return API.AU3_MouseDown(button)


def mouse_get_cursor() -> int:
    return API.AU3_MouseGetCursor()


def mouse_get_pos(point: wintypes.LPPOINT) -> None:
    return API.AU3_MouseGetPos(point)


def mouse_move(x: int, y: int, speed: int = -1) -> int:
    return API.AU3_MouseMove(x, y, speed)


def mouse_up(button: str = 'LEFT') -> None:
    return API.AU3_MouseUp(button)


def mouse_wheel(direction: str, clicks: int) -> None:
    return API.AU3_MouseWheel(direction, clicks)


def opt(option: str, value: int) -> int:
    return API.AU3_Opt(option, value)


def pixel_checksum(rect: wintypes.LPRECT, step: int = 1) -> int:
    return API.AU3_PixelChecksum(rect, step)


def pixel_get_color(x: int, y: int) -> int:
    return API.AU3_PixelGetColor(x, y)


def pixel_search(rect: wintypes.LPRECT, col: int, var: int = 0, step: int = 1,
                 point_result: wintypes.LPPOINT = AU3_INTDEFAULT) -> None:
    return API.AU3_PixelSearch(rect, col, var, step, point_result)


def process_close(process: str) -> int:
    return API.AU3_ProcessClose(process)


def process_exists(process: str) -> int:
    return API.AU3_ProcessExists(process)


def process_set_priority(process: str, priority: int) -> int:
    return API.AU3_ProcessSetPriority(process, priority)


def process_wait(process: str, timeout: int = 0) -> int:
    return API.AU3_ProcessWait(process, timeout)


def process_wait_close(process: str, timeout: int = 0) -> int:
    return API.AU3_ProcessWaitClose(process, timeout)


def run(program: str, dir: str = '', show_flag: int = SW_SHOWNORMAL) -> int:
    return API.AU3_Run(program, dir, show_flag)


def run_wait(program: str, dir: str = '', show_flag: int = SW_SHOWNORMAL) -> int:
    return API.AU3_RunWait(program, dir, show_flag)


def run_as(user: str, domain: str, password: str, logon_flag: int, program: str, dir: str = '',
           show_flag: int = SW_SHOWNORMAL) -> int:
    return API.AU3_RunAs(user, domain, password, logon_flag, program, dir, show_flag)


def run_as_wait(user: str, domain: str, password: str, logon_flag: int, program: str, dir: str = '',
                show_flag: int = SW_SHOWNORMAL) -> int:
    return API.AU3_RunAsWait(user, domain, password, logon_flag, program, dir, show_flag)


def send(send_text: str, mode: int = 0) -> None:
    return API.AU3_Send(send_text, mode)


def shutdown(flags: int) -> int:
    return API.AU3_Shutdown(flags)


def sleep(milliseconds: int) -> None:
    return API.AU3_Sleep(milliseconds)


def statusbar_get_text(title: str, text: str = '', part: int = 1, status_text: str = AU3_INTDEFAULT,
                       buf_size: int = AU3_INTDEFAULT) -> int:
    return API.AU3_StatusbarGetText(title, text, part, status_text, buf_size)


def statusbar_get_text_by_handle(hwnd: wintypes.HWND, part: int = 1, status_text: str = AU3_INTDEFAULT,
                                 buf_size: int = AU3_INTDEFAULT) -> int:
    return API.AU3_StatusbarGetTextByHandle(hwnd, part, status_text, buf_size)


def tool_tip(tip: str, x: int = AU3_INTDEFAULT, y: int = AU3_INTDEFAULT) -> None:
    return API.AU3_ToolTip(tip, x, y)


def win_activate(title: str, text: str = '') -> int:
    return API.AU3_WinActivate(title, text)


def win_activate_by_handle(hwnd: wintypes.HWND) -> int:
    return API.AU3_WinActivateByHandle(hwnd)


def win_active(title: str, text: str = '') -> int:
    return API.AU3_WinActive(title, text)


def win_active_by_handle(hwnd: wintypes.HWND) -> int:
    return API.AU3_WinActiveByHandle(hwnd)


def win_close(title: str, text: str = '') -> int:
    return API.AU3_WinClose(title, text)


def win_close_by_handle(hwnd: wintypes.HWND) -> int:
    return API.AU3_WinCloseByHandle(hwnd)


def win_exists(title: str, text: str = '') -> int:
    return API.AU3_WinExists(title, text)


def win_exists_by_handle(hwnd: wintypes.HWND) -> int:
    return API.AU3_WinExistsByHandle(hwnd)


def win_get_caret_pos(point: wintypes.LPPOINT) -> int:
    return API.AU3_WinGetCaretPos(point)


def win_get_class_list(title: str, text: str = '', ret_text: str = '', buf_size: int = AU3_INTDEFAULT) -> None:
    return API.AU3_WinGetClassList(title, text, ret_text, buf_size)


def win_get_class_list_by_handle(hwnd: wintypes.HWND, ret_text: str, buf_size: int) -> None:
    return API.AU3_WinGetClassListByHandle(hwnd, ret_text, buf_size)


def win_get_client_size(title: str, text: str = '', rect: wintypes.LPRECT = AU3_INTDEFAULT) -> int:
    return API.AU3_WinGetClientSize(title, text, rect)


def win_get_client_size_by_handle(hwnd: wintypes.HWND, rect: wintypes.LPRECT) -> int:
    return API.AU3_WinGetClientSizeByHandle(hwnd, rect)


def win_get_handle(title: str, text: str = '') -> wintypes.HWND:
    return API.AU3_WinGetHandle(title, text)


def win_get_handle_as_text(title: str, text: str = '', ret_text: str = '', buf_size: int = AU3_INTDEFAULT) -> None:
    return API.AU3_WinGetHandleAsText(title, text, ret_text, buf_size)


def win_get_pos(title: str, text: str = '', rect: wintypes.LPRECT = AU3_INTDEFAULT) -> int:
    return API.AU3_WinGetPos(title, text, rect)


def win_get_pos_by_handle(hwnd: wintypes.HWND, rect: wintypes.LPRECT) -> int:
    return API.AU3_WinGetPosByHandle(hwnd, rect)


def win_get_process(title: str, text: str = '') -> int:
    return API.AU3_WinGetProcess(title, text)


def win_get_process_by_handle(hwnd: wintypes.HWND) -> int:
    return API.AU3_WinGetProcessByHandle(hwnd)


def win_get_state(title: str, text: str = '') -> int:
    return API.AU3_WinGetState(title, text)


def win_get_state_by_handle(hwnd: wintypes.HWND) -> int:
    return API.AU3_WinGetStateByHandle(hwnd)


def win_get_text(title: str, text: str = '', ret_text: str = '', buf_size: int = AU3_INTDEFAULT) -> None:
    return API.AU3_WinGetText(title, text, ret_text, buf_size)


def win_get_text_by_handle(hwnd: wintypes.HWND, ret_text: str, buf_size: int) -> None:
    return API.AU3_WinGetTextByHandle(hwnd, ret_text, buf_size)


def win_get_title(title: str, text: str = '', ret_text: str = '', buf_size: int = AU3_INTDEFAULT) -> None:
    return API.AU3_WinGetTitle(title, text, ret_text, buf_size)


def win_get_title_by_handle(hwnd: wintypes.HWND, ret_text: str, buf_size: int) -> None:
    return API.AU3_WinGetTitleByHandle(hwnd, ret_text, buf_size)


def win_kill(title: str, text: str = '') -> int:
    return API.AU3_WinKill(title, text)


def win_kill_by_handle(hwnd: wintypes.HWND) -> int:
    return API.AU3_WinKillByHandle(hwnd)


def win_menu_select_item(title: str, text: str = '', item1: str = '', item2: str = '', item3: str = '', item4: str = '',
                         item5: str = '', item6: str = '', item7: str = '', item8: str = '') -> int:
    return API.AU3_WinMenuSelectItem(title, text, item1, item2, item3, item4, item5, item6, item7, item8)


def win_menu_select_item_by_handle(hwnd: wintypes.HWND, item1: str, item2: str, item3: str, item4: str, item5: str,
                                   item6: str, item7: str, item8: str) -> int:
    return API.AU3_WinMenuSelectItemByHandle(hwnd, item1, item2, item3, item4, item5, item6, item7, item8)


def win_minimize_all() -> None:
    return API.AU3_WinMinimizeAll()


def win_minimize_all_undo() -> None:
    return API.AU3_WinMinimizeAllUndo()


def win_move(title: str, text: str = '', x: int = AU3_INTDEFAULT, y: int = AU3_INTDEFAULT, width: int = -1,
             height: int = -1) -> int:
    return API.AU3_WinMove(title, text, x, y, width, height)


def win_move_by_handle(hwnd: wintypes.HWND, x: int, y: int, width: int = -1, height: int = -1) -> int:
    return API.AU3_WinMoveByHandle(hwnd, x, y, width, height)


def win_set_on_top(title: str, text: str = '', flag: int = AU3_INTDEFAULT) -> int:
    return API.AU3_WinSetOnTop(title, text, flag)


def win_set_on_top_by_handle(hwnd: wintypes.HWND, flag: int) -> int:
    return API.AU3_WinSetOnTopByHandle(hwnd, flag)


def win_set_state(title: str, text: str = '', flags: int = AU3_INTDEFAULT) -> int:
    return API.AU3_WinSetState(title, text, flags)


def win_set_state_by_handle(hwnd: wintypes.HWND, flags: int) -> int:
    return API.AU3_WinSetStateByHandle(hwnd, flags)


def win_set_title(title: str, text: str = '', new_title: str = '') -> int:
    return API.AU3_WinSetTitle(title, text, new_title)


def win_set_title_by_handle(hwnd: wintypes.HWND, new_title: str) -> int:
    return API.AU3_WinSetTitleByHandle(hwnd, new_title)


def win_set_trans(title: str, text: str = '', trans: int = AU3_INTDEFAULT) -> int:
    return API.AU3_WinSetTrans(title, text, trans)


def win_set_trans_by_handle(hwnd: wintypes.HWND, trans: int) -> int:
    return API.AU3_WinSetTransByHandle(hwnd, trans)


def win_wait(title: str, text: str = '', timeout: int = 0) -> int:
    return API.AU3_WinWait(title, text, timeout)


def win_wait_by_handle(hwnd: wintypes.HWND, timeout: int) -> int:
    return API.AU3_WinWaitByHandle(hwnd, timeout)


def win_wait_active(title: str, text: str = '', timeout: int = 0) -> int:
    return API.AU3_WinWaitActive(title, text, timeout)


def win_wait_active_by_handle(hwnd: wintypes.HWND, timeout: int) -> int:
    return API.AU3_WinWaitActiveByHandle(hwnd, timeout)


def win_wait_close(title: str, text: str = '', timeout: int = 0) -> int:
    return API.AU3_WinWaitClose(title, text, timeout)


def win_wait_close_by_handle(hwnd: wintypes.HWND, timeout: int) -> int:
    return API.AU3_WinWaitCloseByHandle(hwnd, timeout)


def win_wait_not_active(title: str, text: str = '', timeout: int = AU3_INTDEFAULT) -> int:
    return API.AU3_WinWaitNotActive(title, text, timeout)


def win_wait_not_active_by_handle(hwnd: wintypes.HWND, timeout: int = 0) -> int:
    return API.AU3_WinWaitNotActiveByHandle(hwnd, timeout)
