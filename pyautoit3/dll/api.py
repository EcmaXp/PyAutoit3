import ctypes
import sys
from importlib import resources

from . import library
from .prototype import API_PROTOTYPE, AU3_PROTOTYPE
from ..exception import AutoitError


class AutoitNativeAPI:
    def __init__(self, dll_name):
        self.dll_name = dll_name
        self.dll = ctypes.WinDLL(dll_name)
        self.cache = {}
        self.AU3_error = self.AU3_error

    @property
    def _handle(self):
        return self.dll._handle

    def errcheck(self, res, func, args):
        code = self.AU3_error()
        if code != 0:
            raise AutoitError(code)

        return res

    def __getattr__(self, name):
        func = self.cache.get(name)
        if func is None:
            prototype: AU3_PROTOTYPE = API_PROTOTYPE[name]
            self.cache[name] = func = prototype(self)

            if name != "AU3_error":
                func.errcheck = self.errcheck

        return func

    @classmethod
    def load(cls):
        dll_name = cls.get_dllname()
        try:
            with resources.path(library.__package__, dll_name) as path:
                return cls(str(path.absolute()))
        except FileNotFoundError:
            return cls(dll_name)

    @classmethod
    def get_dllname(cls):
        if sys.maxsize == 2 ** 31 - 1:
            return "AutoitX3.dll"
        elif sys.maxsize == 2 ** 63 - 1:
            return "AutoitX3_x64.dll"
        else:
            raise Exception("unknown sys.maxsize")


API = AutoitNativeAPI.load()
AU3_INTDEFAULT = -2147483647
