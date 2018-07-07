from . import au3
from .consts import Command, Click, CommandShow
from .types import Point, Rect
from .exception import AutoitError
from .control import Control
from .mouse import Mouse
from .options import Options
from .process import Process
from .window import Window

__all__ = ("au3", "AutoitError", "Control", "Mouse", "Options", "Process", "Window",
           "Point", "Rect", "Click", "Command", "CommandShow")

__version__ = "1.1.2a0"

au3.init()
