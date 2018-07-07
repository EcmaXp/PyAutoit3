from enum import Enum, IntEnum

__all__ = "Command", "Click", "MouseWheelDirection", "CommandShow"


class Command(Enum):
    IsVisible = 'IsVisible'
    IsEnabled = 'IsEnabled'
    ShowDropDown = 'ShowDropDown'
    HideDropDown = 'HideDropDown'
    AddString = 'AddString'
    DelString = 'DelString'
    FindString = 'FindString'
    SetCurrentSelection = 'SetCurrentSelection'
    SelectString = 'SelectString'
    IsChecked = 'IsChecked'
    Check = 'Check'
    UnCheck = 'UnCheck'
    GetCurrentLine = 'GetCurrentLine'
    GetCurrentCol = 'GetCurrentCol'
    GetCurrentSelection = 'GetCurrentSelection'
    GetLineCount = 'GetLineCount'
    GetLine = 'GetLine'
    GetSelected = 'GetSelected'
    EditPaste = 'EditPaste'
    CurrentTab = 'CurrentTab'
    TabRight = 'TabRight'
    TabLeft = 'TabLeft'


class Click(str, Enum):
    Left = "left"
    Right = "right"
    Middle = "middle"
    Main = "main"
    Menu = "menu"
    Primary = "Primary"
    Secondary = "Secondary"


class MouseWheelDirection(str, Enum):
    Up = "up"
    Down = "down"


class CommandShow(IntEnum):
    SW_HIDE = 0
    SW_SHOWNORMAL = 1
    SW_SHOWMINIMIZED = 2
    SW_SHOWMAXIMIZED = 3
    SW_MAXIMIZE = 3
    SW_SHOWNOACTIVATE = 4
    SW_SHOW = 5
    SW_MINIMIZE = 6
    SW_SHOWMINNOACTIVE = 7
    SW_SHOWNA = 8
    SW_RESTORE = 9
    SW_SHOWDEFAULT = 10
    SW_FORCEMINIMIZE = 11
