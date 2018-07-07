__all__ = "AutoitError",


class AutoitError(Exception):
    def __init__(self, code):
        super().__init__(code)
        self.code = code
