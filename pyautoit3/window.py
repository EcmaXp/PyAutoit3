from .dll import functions as au3
from .types import Rect


class Window:
    def __init__(self, handle):
        self.handle = handle

    def __del__(self):
        # TODO: free handle?
        self.handle = None

    @classmethod
    def find(cls, title, text=""):
        handle = au3.win_get_handle(title, text)
        return cls(handle)

    """
    AU3_API int WINAPI AU3_WinActivateByHandle(HWND hWnd);
    AU3_API int WINAPI AU3_WinActiveByHandle(HWND hWnd);
    AU3_API int WINAPI AU3_WinCloseByHandle(HWND hWnd);
    AU3_API int WINAPI AU3_WinExistsByHandle(HWND hWnd);
    AU3_API void WINAPI AU3_WinGetClassListByHandle(HWND hWnd, LPWSTR szRetText, int nBufSize);
    AU3_API int WINAPI AU3_WinGetClientSizeByHandle(HWND hWnd, LPRECT lpRect);
    AU3_API void WINAPI AU3_WinGetHandleAsText(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText, LPWSTR szRetText, int nBufSize);
    AU3_API int WINAPI AU3_WinGetPosByHandle(HWND hWnd, LPRECT lpRect);
    AU3_API DWORD WINAPI AU3_WinGetProcessByHandle(HWND hWnd);
    AU3_API int WINAPI AU3_WinGetStateByHandle(HWND hWnd);
    AU3_API void WINAPI AU3_WinGetTextByHandle(HWND hWnd, LPWSTR szRetText, int nBufSize);
    AU3_API void WINAPI AU3_WinGetTitleByHandle(HWND hWnd, LPWSTR szRetText, int nBufSize);
    AU3_API int WINAPI AU3_WinKillByHandle(HWND hWnd);
    AU3_API int WINAPI AU3_WinMenuSelectItemByHandle(HWND hWnd, LPCWSTR szItem1, LPCWSTR szItem2, LPCWSTR szItem3, LPCWSTR szItem4, LPCWSTR szItem5, LPCWSTR szItem6, LPCWSTR szItem7, LPCWSTR szItem8);
    AU3_API int WINAPI AU3_WinMoveByHandle(HWND hWnd, int nX, int nY, int nWidth = -1, int nHeight = -1);
    AU3_API int WINAPI AU3_WinSetOnTopByHandle(HWND hWnd, int nFlag);
    AU3_API int WINAPI AU3_WinSetStateByHandle(HWND hWnd, int nFlags);
    AU3_API int WINAPI AU3_WinSetTitleByHandle(HWND hWnd, LPCWSTR szNewTitle);
    AU3_API int WINAPI AU3_WinSetTransByHandle(HWND hWnd, int nTrans);
    AU3_API int WINAPI AU3_WinWaitByHandle(HWND hWnd, int nTimeout);
    AU3_API int WINAPI AU3_WinWaitActiveByHandle(HWND hWnd, int nTimeout);
    AU3_API int WINAPI AU3_WinWaitCloseByHandle(HWND hWnd, int nTimeout);
    AU3_API int WINAPI AU3_WinWaitNotActiveByHandle(HWND hWnd, int nTimeout = 0);
    """

    def activate(self):
        au3.win_activate_by_handle(self.handle)

    def active(self) -> int:
        return au3.win_active_by_handle(self.handle)

    def close(self):
        au3.win_close_by_handle(self.handle)

    def exists(self) -> int:
        return au3.win_exists_by_handle(self.handle)

    def class_list(self) -> str:
        raise NotImplementedError

    @property
    def client_size(self) -> Rect:
        return au3.win_get_client_size_by_handle(self.handle)

    def wait_active(self, timeout=0):
        au3.win_wait_active_by_handle(self.handle, timeout)

    def wait_not_active(self):
        au3.win_wait_not_active_by_handle(self.handle)

    @property
    def pos(self) -> Rect:
        return au3.win_get_pos_by_handle(self.handle)

    @property
    def state(self):
        return au3.win_get_state_by_handle(self.handle)

    @state.setter
    def state(self, state: int):
        au3.win_set_state_by_handle(self.handle, state)

    @property
    def text(self):
        return au3.win_get_text_by_handle(self.handle)

    @property
    def title(self) -> str:
        return au3.win_get_title_by_handle(self.handle)

    @title.setter
    def title(self, title: str):
        au3.win_set_title_by_handle(self.handle, title)

    def __repr__(self):
        if self.handle is not None:
            return f"<{type(self).__name__}: {self.title}>"
