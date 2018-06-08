from enum import Enum, IntEnum


class MouseButtonType(str, Enum):
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
