from enum import Enum, IntEnum


class Command(str, Enum):
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


class ClickType(str, Enum):
    Left = "left"
    Right = "right"
    Middle = "middle"
    Main = "main"
    Menu = "menu"
    Primary = "Primary"
    Secondary = "Secondary"


class MouseWheelDirectionType(str, Enum):
    Up = "up"
    Down = "down"


class WindowsStatus(IntEnum):
    SW_SHOWNORMAL = 1


SW_SHOWNORMAL = WindowsStatus.SW_SHOWNORMAL
