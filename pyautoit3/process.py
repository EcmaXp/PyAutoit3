from . import au3
from .dll.api import AU3_INTDEFAULT
from .internal.process import get_process_name, get_process_path

__all__ = "Process",


class Process:
    pid: int

    def __init__(self, pid: int):
        self.pid = pid

    def __eq__(self, other: "Process") -> bool:
        if isinstance(other, Process):
            return self.pid == other.pid

        return NotImplemented

    @classmethod
    def find(cls, text):
        pid = au3.process_exists(text)
        if pid == AU3_INTDEFAULT:
            return None

        return cls(pid)

    def is_exists(self):
        return au3.process_exists(self._spid) == self.pid

    @property
    def name(self):
        return get_process_name(self.pid)

    @property
    def path(self):
        return get_process_path(self.pid)

    @classmethod
    def find_exists(cls, text):
        return au3.process_exists(text) != AU3_INTDEFAULT

    @classmethod
    def wait_launch(cls, text) -> "Process":
        pid = au3.process_wait(text)
        return cls(pid)

    def wait_close(self):
        au3.process_wait_close(self._spid)

    def set_priority(self, priority):
        return au3.process_set_priority(self._spid, priority)

    @property
    def _spid(self):
        return str(self.pid)

    def __repr__(self):
        return f"<{type(self).__name__}: {self.pid}; {self.name!r}>"
