import ctypes
from ctypes import wintypes
from typing import Tuple, Type

from dataclasses import dataclass

API_PROTOTYPE = {}


@dataclass
class AU3_PROTOTYPE:
    line: str
    name: str
    func: Type[ctypes._CFuncPtr]
    paramflags: Tuple

    def __call__(self, api):
        return self.func((self.name, api), self.paramflags)


def AU3_FUNC(line, name, restype, argtypes, paramflags):
    flags = ctypes._FUNCFLAG_STDCALL

    if name == "AU3_error":
        flags = ctypes._FUNCFLAG_CDECL

    # noinspection PyRedeclaration
    class Autoit3FunctionType(ctypes._CFuncPtr):
        _argtypes_ = argtypes
        _restype_ = restype
        _flags_ = flags

    Autoit3FunctionType.__name__ += f"[{name}]"

    return AU3_PROTOTYPE(
        line,
        name,
        Autoit3FunctionType,
        paramflags,
    )


API_PROTOTYPE['AU3_Init'] = AU3_FUNC(
    line='void init()',
    name='AU3_Init',
    restype=None,
    argtypes=(

    ),
    paramflags=(

    ),
)

API_PROTOTYPE['AU3_error'] = AU3_FUNC(
    line='int error()',
    name='AU3_error',
    restype=ctypes.c_int32,
    argtypes=(

    ),
    paramflags=(

    ),
)

API_PROTOTYPE['AU3_AutoItSetOption'] = AU3_FUNC(
    line='int auto_it_set_option(LPCWSTR szOption, int nValue)',
    name='AU3_AutoItSetOption',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szOption', None),
        (1, 'nValue', None),
    ),
)

API_PROTOTYPE['AU3_ClipGet'] = AU3_FUNC(
    line='void clip_get(LPCWSTR szClip, int nBufSize)',
    name='AU3_ClipGet',
    restype=None,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szClip', None),
        (1, 'nBufSize', None),
    ),
)

API_PROTOTYPE['AU3_ClipPut'] = AU3_FUNC(
    line='void clip_put(LPCWSTR szClip)',
    name='AU3_ClipPut',
    restype=None,
    argtypes=(
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'szClip', None),
    ),
)

API_PROTOTYPE['AU3_ControlClick'] = AU3_FUNC(
    line="int control_click(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl, LPCWSTR szButton, int nNumClicks, int nX = 'AU3_INTDEFAULT', int nY = 'AU3_INTDEFAULT')",
    name='AU3_ControlClick',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
        ctypes.c_int32,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', None),
        (1, 'szControl', None),
        (1, 'szButton', None),
        (1, 'nNumClicks', None),
        (1, 'nX', 'AU3_INTDEFAULT'),
        (1, 'nY', 'AU3_INTDEFAULT'),
    ),
)

API_PROTOTYPE['AU3_ControlClickByHandle'] = AU3_FUNC(
    line="int control_click_by_handle(HWND hWnd, HWND hCtrl, LPCWSTR szButton, int nNumClicks, int nX = 'AU3_INTDEFAULT', int nY = 'AU3_INTDEFAULT')",
    name='AU3_ControlClickByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_voidp,
        ctypes.c_wchar_p,
        ctypes.c_int32,
        ctypes.c_int32,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'hCtrl', None),
        (1, 'szButton', None),
        (1, 'nNumClicks', None),
        (1, 'nX', 'AU3_INTDEFAULT'),
        (1, 'nY', 'AU3_INTDEFAULT'),
    ),
)

API_PROTOTYPE['AU3_ControlCommand'] = AU3_FUNC(
    line='void control_command(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl, LPCWSTR szCommand, LPCWSTR szExtra, LPCWSTR szResult, int nBufSize)',
    name='AU3_ControlCommand',
    restype=None,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', None),
        (1, 'szControl', None),
        (1, 'szCommand', None),
        (1, 'szExtra', None),
        (1, 'szResult', None),
        (1, 'nBufSize', None),
    ),
)

API_PROTOTYPE['AU3_ControlCommandByHandle'] = AU3_FUNC(
    line='void control_command_by_handle(HWND hWnd, HWND hCtrl, LPCWSTR szCommand, LPCWSTR szExtra, LPCWSTR szResult, int nBufSize)',
    name='AU3_ControlCommandByHandle',
    restype=None,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_voidp,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'hCtrl', None),
        (1, 'szCommand', None),
        (1, 'szExtra', None),
        (1, 'szResult', None),
        (1, 'nBufSize', None),
    ),
)

API_PROTOTYPE['AU3_ControlListView'] = AU3_FUNC(
    line='void control_list_view(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl, LPCWSTR szCommand, LPCWSTR szExtra1, LPCWSTR szExtra2, LPCWSTR szResult, int nBufSize)',
    name='AU3_ControlListView',
    restype=None,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', None),
        (1, 'szControl', None),
        (1, 'szCommand', None),
        (1, 'szExtra1', None),
        (1, 'szExtra2', None),
        (1, 'szResult', None),
        (1, 'nBufSize', None),
    ),
)

API_PROTOTYPE['AU3_ControlListViewByHandle'] = AU3_FUNC(
    line='void control_list_view_by_handle(HWND hWnd, HWND hCtrl, LPCWSTR szCommand, LPCWSTR szExtra1, LPCWSTR szExtra2, LPCWSTR szResult, int nBufSize)',
    name='AU3_ControlListViewByHandle',
    restype=None,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_voidp,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'hCtrl', None),
        (1, 'szCommand', None),
        (1, 'szExtra1', None),
        (1, 'szExtra2', None),
        (1, 'szResult', None),
        (1, 'nBufSize', None),
    ),
)

API_PROTOTYPE['AU3_ControlDisable'] = AU3_FUNC(
    line='int control_disable(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl)',
    name='AU3_ControlDisable',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', None),
        (1, 'szControl', None),
    ),
)

API_PROTOTYPE['AU3_ControlDisableByHandle'] = AU3_FUNC(
    line='int control_disable_by_handle(HWND hWnd, HWND hCtrl)',
    name='AU3_ControlDisableByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_voidp,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'hCtrl', None),
    ),
)

API_PROTOTYPE['AU3_ControlEnable'] = AU3_FUNC(
    line='int control_enable(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl)',
    name='AU3_ControlEnable',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', None),
        (1, 'szControl', None),
    ),
)

API_PROTOTYPE['AU3_ControlEnableByHandle'] = AU3_FUNC(
    line='int control_enable_by_handle(HWND hWnd, HWND hCtrl)',
    name='AU3_ControlEnableByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_voidp,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'hCtrl', None),
    ),
)

API_PROTOTYPE['AU3_ControlFocus'] = AU3_FUNC(
    line='int control_focus(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl)',
    name='AU3_ControlFocus',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', None),
        (1, 'szControl', None),
    ),
)

API_PROTOTYPE['AU3_ControlFocusByHandle'] = AU3_FUNC(
    line='int control_focus_by_handle(HWND hWnd, HWND hCtrl)',
    name='AU3_ControlFocusByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_voidp,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'hCtrl', None),
    ),
)

API_PROTOTYPE['AU3_ControlGetFocus'] = AU3_FUNC(
    line='void control_get_focus(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControlWithFocus, int nBufSize)',
    name='AU3_ControlGetFocus',
    restype=None,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', None),
        (1, 'szControlWithFocus', None),
        (1, 'nBufSize', None),
    ),
)

API_PROTOTYPE['AU3_ControlGetFocusByHandle'] = AU3_FUNC(
    line='void control_get_focus_by_handle(HWND hWnd, LPCWSTR szControlWithFocus, int nBufSize)',
    name='AU3_ControlGetFocusByHandle',
    restype=None,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'szControlWithFocus', None),
        (1, 'nBufSize', None),
    ),
)

API_PROTOTYPE['AU3_ControlGetHandle'] = AU3_FUNC(
    line='HWND control_get_handle(HWND hWnd, LPCWSTR szControl)',
    name='AU3_ControlGetHandle',
    restype=ctypes.c_voidp,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'szControl', None),
    ),
)

API_PROTOTYPE['AU3_ControlGetHandleAsText'] = AU3_FUNC(
    line="void control_get_handle_as_text(LPCWSTR szTitle, [in] LPCWSTR szText = '', [in] LPCWSTR szControl = '', [in] LPCWSTR szRetText = '', [in] int nBufSize = '')",
    name='AU3_ControlGetHandleAsText',
    restype=None,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
        (1, 'szControl', ''),
        (1, 'szRetText', ''),
        (1, 'nBufSize', ''),
    ),
)

API_PROTOTYPE['AU3_ControlGetPos'] = AU3_FUNC(
    line='int control_get_pos(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl, LPRECT lpRect)',
    name='AU3_ControlGetPos',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        wintypes.PRECTL,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', None),
        (1, 'szControl', None),
        (1, 'lpRect', None),
    ),
)

API_PROTOTYPE['AU3_ControlGetPosByHandle'] = AU3_FUNC(
    line='int control_get_pos_by_handle(HWND hWnd, HWND hCtrl, LPRECT lpRect)',
    name='AU3_ControlGetPosByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_voidp,
        wintypes.PRECTL,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'hCtrl', None),
        (1, 'lpRect', None),
    ),
)

API_PROTOTYPE['AU3_ControlGetText'] = AU3_FUNC(
    line='void control_get_text(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl, LPCWSTR szControlText, int nBufSize)',
    name='AU3_ControlGetText',
    restype=None,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', None),
        (1, 'szControl', None),
        (1, 'szControlText', None),
        (1, 'nBufSize', None),
    ),
)

API_PROTOTYPE['AU3_ControlGetTextByHandle'] = AU3_FUNC(
    line='void control_get_text_by_handle(HWND hWnd, HWND hCtrl, LPCWSTR szControlText, int nBufSize)',
    name='AU3_ControlGetTextByHandle',
    restype=None,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_voidp,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'hCtrl', None),
        (1, 'szControlText', None),
        (1, 'nBufSize', None),
    ),
)

API_PROTOTYPE['AU3_ControlHide'] = AU3_FUNC(
    line='int control_hide(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl)',
    name='AU3_ControlHide',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', None),
        (1, 'szControl', None),
    ),
)

API_PROTOTYPE['AU3_ControlHideByHandle'] = AU3_FUNC(
    line='int control_hide_by_handle(HWND hWnd, HWND hCtrl)',
    name='AU3_ControlHideByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_voidp,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'hCtrl', None),
    ),
)

API_PROTOTYPE['AU3_ControlMove'] = AU3_FUNC(
    line='int control_move(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl, int nX, int nY, int nWidth = -1, int nHeight = -1)',
    name='AU3_ControlMove',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
        ctypes.c_int32,
        ctypes.c_int32,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', None),
        (1, 'szControl', None),
        (1, 'nX', None),
        (1, 'nY', None),
        (1, 'nWidth', -1),
        (1, 'nHeight', -1),
    ),
)

API_PROTOTYPE['AU3_ControlMoveByHandle'] = AU3_FUNC(
    line='int control_move_by_handle(HWND hWnd, HWND hCtrl, int nX, int nY, int nWidth = -1, int nHeight = -1)',
    name='AU3_ControlMoveByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_voidp,
        ctypes.c_int32,
        ctypes.c_int32,
        ctypes.c_int32,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'hCtrl', None),
        (1, 'nX', None),
        (1, 'nY', None),
        (1, 'nWidth', -1),
        (1, 'nHeight', -1),
    ),
)

API_PROTOTYPE['AU3_ControlSend'] = AU3_FUNC(
    line='int control_send(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl, LPCWSTR szSendText, int nMode = 0)',
    name='AU3_ControlSend',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', None),
        (1, 'szControl', None),
        (1, 'szSendText', None),
        (1, 'nMode', 0),
    ),
)

API_PROTOTYPE['AU3_ControlSendByHandle'] = AU3_FUNC(
    line='int control_send_by_handle(HWND hWnd, HWND hCtrl, LPCWSTR szSendText, int nMode = 0)',
    name='AU3_ControlSendByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_voidp,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'hCtrl', None),
        (1, 'szSendText', None),
        (1, 'nMode', 0),
    ),
)

API_PROTOTYPE['AU3_ControlSetText'] = AU3_FUNC(
    line='int control_set_text(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl, LPCWSTR szControlText)',
    name='AU3_ControlSetText',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', None),
        (1, 'szControl', None),
        (1, 'szControlText', None),
    ),
)

API_PROTOTYPE['AU3_ControlSetTextByHandle'] = AU3_FUNC(
    line='int control_set_text_by_handle(HWND hWnd, HWND hCtrl, LPCWSTR szControlText)',
    name='AU3_ControlSetTextByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_voidp,
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'hCtrl', None),
        (1, 'szControlText', None),
    ),
)

API_PROTOTYPE['AU3_ControlShow'] = AU3_FUNC(
    line='int control_show(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl)',
    name='AU3_ControlShow',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', None),
        (1, 'szControl', None),
    ),
)

API_PROTOTYPE['AU3_ControlShowByHandle'] = AU3_FUNC(
    line='int control_show_by_handle(HWND hWnd, HWND hCtrl)',
    name='AU3_ControlShowByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_voidp,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'hCtrl', None),
    ),
)

API_PROTOTYPE['AU3_ControlTreeView'] = AU3_FUNC(
    line='void control_tree_view(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl, LPCWSTR szCommand, LPCWSTR szExtra1, LPCWSTR szExtra2, LPCWSTR szResult, int nBufSize)',
    name='AU3_ControlTreeView',
    restype=None,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', None),
        (1, 'szControl', None),
        (1, 'szCommand', None),
        (1, 'szExtra1', None),
        (1, 'szExtra2', None),
        (1, 'szResult', None),
        (1, 'nBufSize', None),
    ),
)

API_PROTOTYPE['AU3_ControlTreeViewByHandle'] = AU3_FUNC(
    line='void control_tree_view_by_handle(HWND hWnd, HWND hCtrl, LPCWSTR szCommand, LPCWSTR szExtra1, LPCWSTR szExtra2, LPCWSTR szResult, int nBufSize)',
    name='AU3_ControlTreeViewByHandle',
    restype=None,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_voidp,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'hCtrl', None),
        (1, 'szCommand', None),
        (1, 'szExtra1', None),
        (1, 'szExtra2', None),
        (1, 'szResult', None),
        (1, 'nBufSize', None),
    ),
)

API_PROTOTYPE['AU3_DriveMapAdd'] = AU3_FUNC(
    line="void drive_map_add(LPCWSTR szDevice, LPCWSTR szShare, int nFlags, [in] LPCWSTR szUser = '', [in] LPCWSTR szPwd = '', [in] LPCWSTR szResult = '', [in] int nBufSize = '')",
    name='AU3_DriveMapAdd',
    restype=None,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szDevice', None),
        (1, 'szShare', None),
        (1, 'nFlags', None),
        (1, 'szUser', ''),
        (1, 'szPwd', ''),
        (1, 'szResult', ''),
        (1, 'nBufSize', ''),
    ),
)

API_PROTOTYPE['AU3_DriveMapDel'] = AU3_FUNC(
    line='int drive_map_del(LPCWSTR szDevice)',
    name='AU3_DriveMapDel',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'szDevice', None),
    ),
)

API_PROTOTYPE['AU3_DriveMapGet'] = AU3_FUNC(
    line='void drive_map_get(LPCWSTR szDevice, LPCWSTR szMapping, int nBufSize)',
    name='AU3_DriveMapGet',
    restype=None,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szDevice', None),
        (1, 'szMapping', None),
        (1, 'nBufSize', None),
    ),
)

API_PROTOTYPE['AU3_IsAdmin'] = AU3_FUNC(
    line='int is_admin()',
    name='AU3_IsAdmin',
    restype=ctypes.c_int32,
    argtypes=(

    ),
    paramflags=(

    ),
)

API_PROTOTYPE['AU3_MouseClick'] = AU3_FUNC(
    line="int mouse_click([in] LPCWSTR szButton = 'LEFT', int nX = 'AU3_INTDEFAULT', int nY = 'AU3_INTDEFAULT', int nClicks = 1, int nSpeed = -1)",
    name='AU3_MouseClick',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_int32,
        ctypes.c_int32,
        ctypes.c_int32,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szButton', 'LEFT'),
        (1, 'nX', 'AU3_INTDEFAULT'),
        (1, 'nY', 'AU3_INTDEFAULT'),
        (1, 'nClicks', 1),
        (1, 'nSpeed', -1),
    ),
)

API_PROTOTYPE['AU3_MouseClickDrag'] = AU3_FUNC(
    line='int mouse_click_drag(LPCWSTR szButton, int nX1, int nY1, int nX2, int nY2, int nSpeed = -1)',
    name='AU3_MouseClickDrag',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_int32,
        ctypes.c_int32,
        ctypes.c_int32,
        ctypes.c_int32,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szButton', None),
        (1, 'nX1', None),
        (1, 'nY1', None),
        (1, 'nX2', None),
        (1, 'nY2', None),
        (1, 'nSpeed', -1),
    ),
)

API_PROTOTYPE['AU3_MouseDown'] = AU3_FUNC(
    line="void mouse_down([in] LPCWSTR szButton = 'LEFT')",
    name='AU3_MouseDown',
    restype=None,
    argtypes=(
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'szButton', 'LEFT'),
    ),
)

API_PROTOTYPE['AU3_MouseGetCursor'] = AU3_FUNC(
    line='int mouse_get_cursor()',
    name='AU3_MouseGetCursor',
    restype=ctypes.c_int32,
    argtypes=(

    ),
    paramflags=(

    ),
)

API_PROTOTYPE['AU3_MouseGetPos'] = AU3_FUNC(
    line='void mouse_get_pos(LPPOINT lpPoint)',
    name='AU3_MouseGetPos',
    restype=None,
    argtypes=(
        wintypes.PPOINTL,
    ),
    paramflags=(
        (1, 'lpPoint', None),
    ),
)

API_PROTOTYPE['AU3_MouseMove'] = AU3_FUNC(
    line='int mouse_move(int nX, int nY, int nSpeed = -1)',
    name='AU3_MouseMove',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_int32,
        ctypes.c_int32,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'nX', None),
        (1, 'nY', None),
        (1, 'nSpeed', -1),
    ),
)

API_PROTOTYPE['AU3_MouseUp'] = AU3_FUNC(
    line="void mouse_up([in] LPCWSTR szButton = 'LEFT')",
    name='AU3_MouseUp',
    restype=None,
    argtypes=(
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'szButton', 'LEFT'),
    ),
)

API_PROTOTYPE['AU3_MouseWheel'] = AU3_FUNC(
    line='void mouse_wheel(LPCWSTR szDirection, int nClicks)',
    name='AU3_MouseWheel',
    restype=None,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szDirection', None),
        (1, 'nClicks', None),
    ),
)

API_PROTOTYPE['AU3_Opt'] = AU3_FUNC(
    line='int opt(LPCWSTR szOption, int nValue)',
    name='AU3_Opt',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szOption', None),
        (1, 'nValue', None),
    ),
)

API_PROTOTYPE['AU3_PixelChecksum'] = AU3_FUNC(
    line='DWORD pixel_checksum(LPRECT lpRect, int nStep = 1)',
    name='AU3_PixelChecksum',
    restype=ctypes.c_uint32,
    argtypes=(
        wintypes.PRECTL,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'lpRect', None),
        (1, 'nStep', 1),
    ),
)

API_PROTOTYPE['AU3_PixelGetColor'] = AU3_FUNC(
    line='int pixel_get_color(int nX, int nY)',
    name='AU3_PixelGetColor',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_int32,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'nX', None),
        (1, 'nY', None),
    ),
)

API_PROTOTYPE['AU3_PixelSearch'] = AU3_FUNC(
    line='void pixel_search(LPRECT lpRect, int nCol, int nVar = 0, int nStep = 1, LPPOINT pPointResult = 1)',
    name='AU3_PixelSearch',
    restype=None,
    argtypes=(
        wintypes.PRECTL,
        ctypes.c_int32,
        ctypes.c_int32,
        ctypes.c_int32,
        wintypes.PPOINTL,
    ),
    paramflags=(
        (1, 'lpRect', None),
        (1, 'nCol', None),
        (1, 'nVar', 0),
        (1, 'nStep', 1),
        (1, 'pPointResult', 1),
    ),
)

API_PROTOTYPE['AU3_ProcessClose'] = AU3_FUNC(
    line='int process_close(LPCWSTR szProcess)',
    name='AU3_ProcessClose',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'szProcess', None),
    ),
)

API_PROTOTYPE['AU3_ProcessExists'] = AU3_FUNC(
    line='int process_exists(LPCWSTR szProcess)',
    name='AU3_ProcessExists',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'szProcess', None),
    ),
)

API_PROTOTYPE['AU3_ProcessSetPriority'] = AU3_FUNC(
    line='int process_set_priority(LPCWSTR szProcess, int nPriority)',
    name='AU3_ProcessSetPriority',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szProcess', None),
        (1, 'nPriority', None),
    ),
)

API_PROTOTYPE['AU3_ProcessWait'] = AU3_FUNC(
    line='int process_wait(LPCWSTR szProcess, int nTimeout = 0)',
    name='AU3_ProcessWait',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szProcess', None),
        (1, 'nTimeout', 0),
    ),
)

API_PROTOTYPE['AU3_ProcessWaitClose'] = AU3_FUNC(
    line='int process_wait_close(LPCWSTR szProcess, int nTimeout = 0)',
    name='AU3_ProcessWaitClose',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szProcess', None),
        (1, 'nTimeout', 0),
    ),
)

API_PROTOTYPE['AU3_Run'] = AU3_FUNC(
    line="int run(LPCWSTR szProgram, [in] LPCWSTR szDir = '', int nShowFlag = 'SW_SHOWNORMAL')",
    name='AU3_Run',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szProgram', None),
        (1, 'szDir', ''),
        (1, 'nShowFlag', 'SW_SHOWNORMAL'),
    ),
)

API_PROTOTYPE['AU3_RunWait'] = AU3_FUNC(
    line="int run_wait(LPCWSTR szProgram, [in] LPCWSTR szDir = '', int nShowFlag = 'SW_SHOWNORMAL')",
    name='AU3_RunWait',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szProgram', None),
        (1, 'szDir', ''),
        (1, 'nShowFlag', 'SW_SHOWNORMAL'),
    ),
)

API_PROTOTYPE['AU3_RunAs'] = AU3_FUNC(
    line="int run_as(LPCWSTR szUser, LPCWSTR szDomain, LPCWSTR szPassword, int nLogonFlag, LPCWSTR szProgram, [in] LPCWSTR szDir = '', int nShowFlag = 'SW_SHOWNORMAL')",
    name='AU3_RunAs',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szUser', None),
        (1, 'szDomain', None),
        (1, 'szPassword', None),
        (1, 'nLogonFlag', None),
        (1, 'szProgram', None),
        (1, 'szDir', ''),
        (1, 'nShowFlag', 'SW_SHOWNORMAL'),
    ),
)

API_PROTOTYPE['AU3_RunAsWait'] = AU3_FUNC(
    line="int run_as_wait(LPCWSTR szUser, LPCWSTR szDomain, LPCWSTR szPassword, int nLogonFlag, LPCWSTR szProgram, [in] LPCWSTR szDir = '', int nShowFlag = 'SW_SHOWNORMAL')",
    name='AU3_RunAsWait',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szUser', None),
        (1, 'szDomain', None),
        (1, 'szPassword', None),
        (1, 'nLogonFlag', None),
        (1, 'szProgram', None),
        (1, 'szDir', ''),
        (1, 'nShowFlag', 'SW_SHOWNORMAL'),
    ),
)

API_PROTOTYPE['AU3_Send'] = AU3_FUNC(
    line='void send(LPCWSTR szSendText, int nMode = 0)',
    name='AU3_Send',
    restype=None,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szSendText', None),
        (1, 'nMode', 0),
    ),
)

API_PROTOTYPE['AU3_Shutdown'] = AU3_FUNC(
    line='int shutdown(int nFlags)',
    name='AU3_Shutdown',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'nFlags', None),
    ),
)

API_PROTOTYPE['AU3_Sleep'] = AU3_FUNC(
    line='void sleep(int nMilliseconds)',
    name='AU3_Sleep',
    restype=None,
    argtypes=(
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'nMilliseconds', None),
    ),
)

API_PROTOTYPE['AU3_StatusbarGetText'] = AU3_FUNC(
    line="int statusbar_get_text(LPCWSTR szTitle, [in] LPCWSTR szText = '', [in] int nPart = 1, [in] LPCWSTR szStatusText = 1, [in] int nBufSize = 1)",
    name='AU3_StatusbarGetText',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
        (1, 'nPart', 1),
        (1, 'szStatusText', 1),
        (1, 'nBufSize', 1),
    ),
)

API_PROTOTYPE['AU3_StatusbarGetTextByHandle'] = AU3_FUNC(
    line='int statusbar_get_text_by_handle(HWND hWnd, [in] int nPart = 1, [in] LPCWSTR szStatusText = 1, [in] int nBufSize = 1)',
    name='AU3_StatusbarGetTextByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_int32,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'nPart', 1),
        (1, 'szStatusText', 1),
        (1, 'nBufSize', 1),
    ),
)

API_PROTOTYPE['AU3_ToolTip'] = AU3_FUNC(
    line="void tool_tip(LPCWSTR szTip, int nX = 'AU3_INTDEFAULT', int nY = 'AU3_INTDEFAULT')",
    name='AU3_ToolTip',
    restype=None,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_int32,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szTip', None),
        (1, 'nX', 'AU3_INTDEFAULT'),
        (1, 'nY', 'AU3_INTDEFAULT'),
    ),
)

API_PROTOTYPE['AU3_WinActivate'] = AU3_FUNC(
    line="int win_activate(LPCWSTR szTitle, [in] LPCWSTR szText = '')",
    name='AU3_WinActivate',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
    ),
)

API_PROTOTYPE['AU3_WinActivateByHandle'] = AU3_FUNC(
    line='int win_activate_by_handle(HWND hWnd)',
    name='AU3_WinActivateByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
    ),
    paramflags=(
        (1, 'hWnd', None),
    ),
)

API_PROTOTYPE['AU3_WinActive'] = AU3_FUNC(
    line="int win_active(LPCWSTR szTitle, [in] LPCWSTR szText = '')",
    name='AU3_WinActive',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
    ),
)

API_PROTOTYPE['AU3_WinActiveByHandle'] = AU3_FUNC(
    line='int win_active_by_handle(HWND hWnd)',
    name='AU3_WinActiveByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
    ),
    paramflags=(
        (1, 'hWnd', None),
    ),
)

API_PROTOTYPE['AU3_WinClose'] = AU3_FUNC(
    line="int win_close(LPCWSTR szTitle, [in] LPCWSTR szText = '')",
    name='AU3_WinClose',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
    ),
)

API_PROTOTYPE['AU3_WinCloseByHandle'] = AU3_FUNC(
    line='int win_close_by_handle(HWND hWnd)',
    name='AU3_WinCloseByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
    ),
    paramflags=(
        (1, 'hWnd', None),
    ),
)

API_PROTOTYPE['AU3_WinExists'] = AU3_FUNC(
    line="int win_exists(LPCWSTR szTitle, [in] LPCWSTR szText = '')",
    name='AU3_WinExists',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
    ),
)

API_PROTOTYPE['AU3_WinExistsByHandle'] = AU3_FUNC(
    line='int win_exists_by_handle(HWND hWnd)',
    name='AU3_WinExistsByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
    ),
    paramflags=(
        (1, 'hWnd', None),
    ),
)

API_PROTOTYPE['AU3_WinGetCaretPos'] = AU3_FUNC(
    line='int win_get_caret_pos(LPPOINT lpPoint)',
    name='AU3_WinGetCaretPos',
    restype=ctypes.c_int32,
    argtypes=(
        wintypes.PPOINTL,
    ),
    paramflags=(
        (1, 'lpPoint', None),
    ),
)

API_PROTOTYPE['AU3_WinGetClassList'] = AU3_FUNC(
    line="void win_get_class_list(LPCWSTR szTitle, [in] LPCWSTR szText = '', [in] LPCWSTR szRetText = '', [in] int nBufSize = '')",
    name='AU3_WinGetClassList',
    restype=None,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
        (1, 'szRetText', ''),
        (1, 'nBufSize', ''),
    ),
)

API_PROTOTYPE['AU3_WinGetClassListByHandle'] = AU3_FUNC(
    line='void win_get_class_list_by_handle(HWND hWnd, LPCWSTR szRetText, int nBufSize)',
    name='AU3_WinGetClassListByHandle',
    restype=None,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'szRetText', None),
        (1, 'nBufSize', None),
    ),
)

API_PROTOTYPE['AU3_WinGetClientSize'] = AU3_FUNC(
    line="int win_get_client_size(LPCWSTR szTitle, [in] LPCWSTR szText = '', [in] LPRECT lpRect = '')",
    name='AU3_WinGetClientSize',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        wintypes.PRECTL,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
        (1, 'lpRect', ''),
    ),
)

API_PROTOTYPE['AU3_WinGetClientSizeByHandle'] = AU3_FUNC(
    line='int win_get_client_size_by_handle(HWND hWnd, LPRECT lpRect)',
    name='AU3_WinGetClientSizeByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
        wintypes.PRECTL,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'lpRect', None),
    ),
)

API_PROTOTYPE['AU3_WinGetHandle'] = AU3_FUNC(
    line="HWND win_get_handle(LPCWSTR szTitle, [in] LPCWSTR szText = '')",
    name='AU3_WinGetHandle',
    restype=ctypes.c_voidp,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
    ),
)

API_PROTOTYPE['AU3_WinGetHandleAsText'] = AU3_FUNC(
    line="void win_get_handle_as_text(LPCWSTR szTitle, [in] LPCWSTR szText = '', [in] LPCWSTR szRetText = '', [in] int nBufSize = '')",
    name='AU3_WinGetHandleAsText',
    restype=None,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
        (1, 'szRetText', ''),
        (1, 'nBufSize', ''),
    ),
)

API_PROTOTYPE['AU3_WinGetPos'] = AU3_FUNC(
    line="int win_get_pos(LPCWSTR szTitle, [in] LPCWSTR szText = '', [in] LPRECT lpRect = '')",
    name='AU3_WinGetPos',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        wintypes.PRECTL,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
        (1, 'lpRect', ''),
    ),
)

API_PROTOTYPE['AU3_WinGetPosByHandle'] = AU3_FUNC(
    line='int win_get_pos_by_handle(HWND hWnd, LPRECT lpRect)',
    name='AU3_WinGetPosByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
        wintypes.PRECTL,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'lpRect', None),
    ),
)

API_PROTOTYPE['AU3_WinGetProcess'] = AU3_FUNC(
    line="DWORD win_get_process(LPCWSTR szTitle, [in] LPCWSTR szText = '')",
    name='AU3_WinGetProcess',
    restype=ctypes.c_uint32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
    ),
)

API_PROTOTYPE['AU3_WinGetProcessByHandle'] = AU3_FUNC(
    line='DWORD win_get_process_by_handle(HWND hWnd)',
    name='AU3_WinGetProcessByHandle',
    restype=ctypes.c_uint32,
    argtypes=(
        ctypes.c_voidp,
    ),
    paramflags=(
        (1, 'hWnd', None),
    ),
)

API_PROTOTYPE['AU3_WinGetState'] = AU3_FUNC(
    line="int win_get_state(LPCWSTR szTitle, [in] LPCWSTR szText = '')",
    name='AU3_WinGetState',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
    ),
)

API_PROTOTYPE['AU3_WinGetStateByHandle'] = AU3_FUNC(
    line='int win_get_state_by_handle(HWND hWnd)',
    name='AU3_WinGetStateByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
    ),
    paramflags=(
        (1, 'hWnd', None),
    ),
)

API_PROTOTYPE['AU3_WinGetText'] = AU3_FUNC(
    line="void win_get_text(LPCWSTR szTitle, [in] LPCWSTR szText = '', [in] LPCWSTR szRetText = '', [in] int nBufSize = '')",
    name='AU3_WinGetText',
    restype=None,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
        (1, 'szRetText', ''),
        (1, 'nBufSize', ''),
    ),
)

API_PROTOTYPE['AU3_WinGetTextByHandle'] = AU3_FUNC(
    line='void win_get_text_by_handle(HWND hWnd, LPCWSTR szRetText, int nBufSize)',
    name='AU3_WinGetTextByHandle',
    restype=None,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'szRetText', None),
        (1, 'nBufSize', None),
    ),
)

API_PROTOTYPE['AU3_WinGetTitle'] = AU3_FUNC(
    line="void win_get_title(LPCWSTR szTitle, [in] LPCWSTR szText = '', [in] LPCWSTR szRetText = '', [in] int nBufSize = '')",
    name='AU3_WinGetTitle',
    restype=None,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
        (1, 'szRetText', ''),
        (1, 'nBufSize', ''),
    ),
)

API_PROTOTYPE['AU3_WinGetTitleByHandle'] = AU3_FUNC(
    line='void win_get_title_by_handle(HWND hWnd, LPCWSTR szRetText, int nBufSize)',
    name='AU3_WinGetTitleByHandle',
    restype=None,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'szRetText', None),
        (1, 'nBufSize', None),
    ),
)

API_PROTOTYPE['AU3_WinKill'] = AU3_FUNC(
    line="int win_kill(LPCWSTR szTitle, [in] LPCWSTR szText = '')",
    name='AU3_WinKill',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
    ),
)

API_PROTOTYPE['AU3_WinKillByHandle'] = AU3_FUNC(
    line='int win_kill_by_handle(HWND hWnd)',
    name='AU3_WinKillByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
    ),
    paramflags=(
        (1, 'hWnd', None),
    ),
)

API_PROTOTYPE['AU3_WinMenuSelectItem'] = AU3_FUNC(
    line="int win_menu_select_item(LPCWSTR szTitle, [in] LPCWSTR szText = '', [in] LPCWSTR szItem1 = '', [in] LPCWSTR szItem2 = '', [in] LPCWSTR szItem3 = '', [in] LPCWSTR szItem4 = '', [in] LPCWSTR szItem5 = '', [in] LPCWSTR szItem6 = '', [in] LPCWSTR szItem7 = '', [in] LPCWSTR szItem8 = '')",
    name='AU3_WinMenuSelectItem',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
        (1, 'szItem1', ''),
        (1, 'szItem2', ''),
        (1, 'szItem3', ''),
        (1, 'szItem4', ''),
        (1, 'szItem5', ''),
        (1, 'szItem6', ''),
        (1, 'szItem7', ''),
        (1, 'szItem8', ''),
    ),
)

API_PROTOTYPE['AU3_WinMenuSelectItemByHandle'] = AU3_FUNC(
    line='int win_menu_select_item_by_handle(HWND hWnd, LPCWSTR szItem1, LPCWSTR szItem2, LPCWSTR szItem3, LPCWSTR szItem4, LPCWSTR szItem5, LPCWSTR szItem6, LPCWSTR szItem7, LPCWSTR szItem8)',
    name='AU3_WinMenuSelectItemByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'szItem1', None),
        (1, 'szItem2', None),
        (1, 'szItem3', None),
        (1, 'szItem4', None),
        (1, 'szItem5', None),
        (1, 'szItem6', None),
        (1, 'szItem7', None),
        (1, 'szItem8', None),
    ),
)

API_PROTOTYPE['AU3_WinMinimizeAll'] = AU3_FUNC(
    line='void win_minimize_all()',
    name='AU3_WinMinimizeAll',
    restype=None,
    argtypes=(

    ),
    paramflags=(

    ),
)

API_PROTOTYPE['AU3_WinMinimizeAllUndo'] = AU3_FUNC(
    line='void win_minimize_all_undo()',
    name='AU3_WinMinimizeAllUndo',
    restype=None,
    argtypes=(

    ),
    paramflags=(

    ),
)

API_PROTOTYPE['AU3_WinMove'] = AU3_FUNC(
    line="int win_move(LPCWSTR szTitle, [in] LPCWSTR szText = '', [in] int nX = '', [in] int nY = '', int nWidth = -1, int nHeight = -1)",
    name='AU3_WinMove',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
        ctypes.c_int32,
        ctypes.c_int32,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
        (1, 'nX', ''),
        (1, 'nY', ''),
        (1, 'nWidth', -1),
        (1, 'nHeight', -1),
    ),
)

API_PROTOTYPE['AU3_WinMoveByHandle'] = AU3_FUNC(
    line='int win_move_by_handle(HWND hWnd, int nX, int nY, int nWidth = -1, int nHeight = -1)',
    name='AU3_WinMoveByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_int32,
        ctypes.c_int32,
        ctypes.c_int32,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'nX', None),
        (1, 'nY', None),
        (1, 'nWidth', -1),
        (1, 'nHeight', -1),
    ),
)

API_PROTOTYPE['AU3_WinSetOnTop'] = AU3_FUNC(
    line="int win_set_on_top(LPCWSTR szTitle, [in] LPCWSTR szText = '', [in] int nFlag = '')",
    name='AU3_WinSetOnTop',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
        (1, 'nFlag', ''),
    ),
)

API_PROTOTYPE['AU3_WinSetOnTopByHandle'] = AU3_FUNC(
    line='int win_set_on_top_by_handle(HWND hWnd, int nFlag)',
    name='AU3_WinSetOnTopByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'nFlag', None),
    ),
)

API_PROTOTYPE['AU3_WinSetState'] = AU3_FUNC(
    line="int win_set_state(LPCWSTR szTitle, [in] LPCWSTR szText = '', [in] int nFlags = '')",
    name='AU3_WinSetState',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
        (1, 'nFlags', ''),
    ),
)

API_PROTOTYPE['AU3_WinSetStateByHandle'] = AU3_FUNC(
    line='int win_set_state_by_handle(HWND hWnd, int nFlags)',
    name='AU3_WinSetStateByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'nFlags', None),
    ),
)

API_PROTOTYPE['AU3_WinSetTitle'] = AU3_FUNC(
    line="int win_set_title(LPCWSTR szTitle, [in] LPCWSTR szText = '', [in] LPCWSTR szNewTitle = '')",
    name='AU3_WinSetTitle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
        (1, 'szNewTitle', ''),
    ),
)

API_PROTOTYPE['AU3_WinSetTitleByHandle'] = AU3_FUNC(
    line='int win_set_title_by_handle(HWND hWnd, LPCWSTR szNewTitle)',
    name='AU3_WinSetTitleByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_wchar_p,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'szNewTitle', None),
    ),
)

API_PROTOTYPE['AU3_WinSetTrans'] = AU3_FUNC(
    line="int win_set_trans(LPCWSTR szTitle, [in] LPCWSTR szText = '', [in] int nTrans = '')",
    name='AU3_WinSetTrans',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
        (1, 'nTrans', ''),
    ),
)

API_PROTOTYPE['AU3_WinSetTransByHandle'] = AU3_FUNC(
    line='int win_set_trans_by_handle(HWND hWnd, int nTrans)',
    name='AU3_WinSetTransByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'nTrans', None),
    ),
)

API_PROTOTYPE['AU3_WinWait'] = AU3_FUNC(
    line="int win_wait(LPCWSTR szTitle, [in] LPCWSTR szText = '', int nTimeout = 0)",
    name='AU3_WinWait',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
        (1, 'nTimeout', 0),
    ),
)

API_PROTOTYPE['AU3_WinWaitByHandle'] = AU3_FUNC(
    line='int win_wait_by_handle(HWND hWnd, int nTimeout)',
    name='AU3_WinWaitByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'nTimeout', None),
    ),
)

API_PROTOTYPE['AU3_WinWaitActive'] = AU3_FUNC(
    line="int win_wait_active(LPCWSTR szTitle, [in] LPCWSTR szText = '', int nTimeout = 0)",
    name='AU3_WinWaitActive',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
        (1, 'nTimeout', 0),
    ),
)

API_PROTOTYPE['AU3_WinWaitActiveByHandle'] = AU3_FUNC(
    line='int win_wait_active_by_handle(HWND hWnd, int nTimeout)',
    name='AU3_WinWaitActiveByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'nTimeout', None),
    ),
)

API_PROTOTYPE['AU3_WinWaitClose'] = AU3_FUNC(
    line="int win_wait_close(LPCWSTR szTitle, [in] LPCWSTR szText = '', int nTimeout = 0)",
    name='AU3_WinWaitClose',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
        (1, 'nTimeout', 0),
    ),
)

API_PROTOTYPE['AU3_WinWaitCloseByHandle'] = AU3_FUNC(
    line='int win_wait_close_by_handle(HWND hWnd, int nTimeout)',
    name='AU3_WinWaitCloseByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'nTimeout', None),
    ),
)

API_PROTOTYPE['AU3_WinWaitNotActive'] = AU3_FUNC(
    line="int win_wait_not_active(LPCWSTR szTitle, [in] LPCWSTR szText = '', [in] int nTimeout = '')",
    name='AU3_WinWaitNotActive',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_wchar_p,
        ctypes.c_wchar_p,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'szTitle', None),
        (1, 'szText', ''),
        (1, 'nTimeout', ''),
    ),
)

API_PROTOTYPE['AU3_WinWaitNotActiveByHandle'] = AU3_FUNC(
    line='int win_wait_not_active_by_handle(HWND hWnd, int nTimeout = 0)',
    name='AU3_WinWaitNotActiveByHandle',
    restype=ctypes.c_int32,
    argtypes=(
        ctypes.c_voidp,
        ctypes.c_int32,
    ),
    paramflags=(
        (1, 'hWnd', None),
        (1, 'nTimeout', 0),
    ),
)
