import ctypes
import os

from .prototype import API_PROTOTYPE, AU3_PROTOTYPE


class Autoit3Error(Exception):
    pass


class Autoit3NativeAPI:
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
            raise Autoit3Error(code)

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
        # TODO: 32 bit or 64 bit
        path = os.path.abspath(os.path.join(__file__, "../data", "AutoitX3_x64.dll"))
        return cls(path)


API = Autoit3NativeAPI.load()
AU3_INTDEFAULT = -2147483647
