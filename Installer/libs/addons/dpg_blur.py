
from ctypes import POINTER, c_bool, c_int, cdll, pointer, sizeof, Structure, byref
from ctypes.wintypes import DWORD, LONG, LPCVOID, ULONG
import ctypes.wintypes
from ctypes import wintypes
from enum import Enum
import os

class WINDOWCOMPOSITIONATTRIB(Enum):
    WCA_ACCENT_POLICY = 19
class ACCENT_STATE(Enum):
    ACCENT_ENABLE_BLURBEHIND = 3
class ACCENT_POLICY(Structure):
    _fields_ = [
        ("AccentState",     DWORD),
        ("AccentFlags",     DWORD),
        ("GradientColor",   DWORD),
        ("AnimationId",     DWORD),
    ]
class WINDOWCOMPOSITIONATTRIBDATA(Structure):
    _fields_ = [
        ("Attribute",   DWORD),
        ("Data",        POINTER(ACCENT_POLICY)),
        ("SizeOfData",  ULONG),
    ]
class MARGINS(Structure):
    _fields_ = [
        ("cxLeftWidth",     c_int),
        ("cxRightWidth",    c_int),
        ("cyTopHeight",     c_int),
        ("cyBottomHeight",  c_int),
    ]
user32 = ctypes.windll.user32
WNDENUMPROC = ctypes.WINFUNCTYPE(ctypes.wintypes.BOOL,
                                 ctypes.wintypes.HWND,
                                 ctypes.wintypes.LPARAM)
user32.EnumWindows.argtypes = [WNDENUMPROC,ctypes.wintypes.LPARAM]
class WindowsWindowEffect:
    def __init__(self):
        self.user32 = cdll.LoadLibrary("user32")
        self.dwmapi = cdll.LoadLibrary("dwmapi")
        self.SetWindowCompositionAttribute = self.user32.SetWindowCompositionAttribute
        self.DwmSetWindowAttribute = self.dwmapi.DwmSetWindowAttribute
        self.SetWindowCompositionAttribute.restype = c_bool
        self.SetWindowCompositionAttribute.argtypes = [
            c_int,
            POINTER(WINDOWCOMPOSITIONATTRIBDATA),
        ]
        self.accentPolicy = ACCENT_POLICY()
        self.winCompAttrData = WINDOWCOMPOSITIONATTRIBDATA()
        self.winCompAttrData.Attribute = WINDOWCOMPOSITIONATTRIB.WCA_ACCENT_POLICY.value
        self.winCompAttrData.SizeOfData = sizeof(self.accentPolicy)
        self.winCompAttrData.Data = pointer(self.accentPolicy)
    def setAeroEffect(self, hWnd):
        self.winCompAttrData.Attribute = WINDOWCOMPOSITIONATTRIB.WCA_ACCENT_POLICY.value
        self.accentPolicy.AccentState = ACCENT_STATE.ACCENT_ENABLE_BLURBEHIND.value
        self.SetWindowCompositionAttribute(hWnd, pointer(self.winCompAttrData))
    def setRoundedCorners(self, hWnd, radius):
        self.DwmSetWindowAttribute(hWnd, wintypes.DWORD(33), byref(wintypes.INT(2)), wintypes.UINT(sizeof(wintypes.INT)))

def get_hwnd_from_pid(pid: int):
    result = None
    def callback(hwnd, _):
        nonlocal result
        lpdw_PID = ctypes.c_ulong()
        user32.GetWindowThreadProcessId(hwnd, ctypes.byref(lpdw_PID))
        hwnd_PID = lpdw_PID.value

        if hwnd_PID == pid:
            result = hwnd
            return False
        return True
    cb_worker = WNDENUMPROC(callback)
    user32.EnumWindows(cb_worker, 0)
    return result
def get_hwnd():
    return get_hwnd_from_pid(os.getpid())
