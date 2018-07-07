import ctypes
from contextlib import contextmanager

__all__ = "get_process_name", "get_process_path"

user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32
psapi = ctypes.windll.psapi

PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010


@contextmanager
def open_process(pid):
    process = kernel32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, pid)

    try:
        yield process
    finally:
        kernel32.CloseHandle(process)


def get_process_name(pid: int) -> str:
    length = 256

    with open_process(pid) as process:
        buffer = ctypes.create_unicode_buffer(length)
        psapi.GetModuleBaseNameW(process, None, ctypes.byref(buffer), length)

    return buffer.value


def get_process_path(pid: int) -> str:
    with open_process(pid) as process:
        length = 4096
        buffer = ctypes.create_unicode_buffer(length)

        psapi.GetModuleFileNameExW(process, None, ctypes.byref(buffer), length)

    return buffer.value
