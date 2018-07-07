from .dll.functions import auto_it_set_option

__all__ = "Options",


class Option:
    def __init__(self, name):
        self.name = name
        self.value = None

    def __get__(self, instance, owner) -> int:
        value = self.value
        if value is None:
            value = auto_it_set_option(self.name, 0)
            auto_it_set_option(self.name, value)
            self.value = value

        return value

    def __set__(self, instance, value: int):
        auto_it_set_option(self.name, value)
        self.value = value


class Options:
    CaretCoordMode = Option('CaretCoordMode')
    ExpandEnvStrings = Option('ExpandEnvStrings')
    ExpandVarStrings = Option('ExpandVarStrings')
    GUICloseOnESC = Option('GUICloseOnESC')
    GUICoordMode = Option('GUICoordMode')
    GUIDataSeparatorChar = Option('GUIDataSeparatorChar')
    GUIOnEventMode = Option('GUIOnEventMode')
    GUIResizeMode = Option('GUIResizeMode')
    GUIEventOptions = Option('GUIEventOptions')
    MouseClickDelay = Option('MouseClickDelay')
    MouseClickDownDelay = Option('MouseClickDownDelay')
    MouseClickDragDelay = Option('MouseClickDragDelay')
    MouseCoordMode = Option('MouseCoordMode')
    MustDeclareVars = Option('MustDeclareVars')
    PixelCoordMode = Option('PixelCoordMode')
    SendAttachMode = Option('SendAttachMode')
    SendCapslockMode = Option('SendCapslockMode')
    SendKeyDelay = Option('SendKeyDelay')
    SendKeyDownDelay = Option('SendKeyDownDelay')
    TCPTimeout = Option('TCPTimeout')
    TrayAutoPause = Option('TrayAutoPause')
    TrayIconDebug = Option('TrayIconDebug')
    TrayIconHide = Option('TrayIconHide')
    TrayMenuMode = Option('TrayMenuMode')
    TrayOnEventMode = Option('TrayOnEventMode')
    WinDetectHiddenText = Option('WinDetectHiddenText')
    WinSearchChildren = Option('WinSearchChildren')
    WinTextMatchMode = Option('WinTextMatchMode')
    WinTitleMatchMode = Option('WinTitleMatchMode')
    WinWaitDelay = Option('WinWaitDelay')
