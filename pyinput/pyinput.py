import sched
from time import sleep, time
import win32gui, win32ui, win32con, win32api

# http://www.kbdedit.com/manual/low_level_vk_list.html
VK_KEY_W = 0x57
VK_KEY_A = 0x41
VK_KEY_S = 0x53
VK_KEY_D = 0x44
VK_KEY_P = 0x50
VK_SHIFT = 0xA0
VK_RETURN = 0x0D

def list_windows():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), '"' + win32gui.GetWindowText(hwnd) + '"')
    win32gui.EnumWindows(winEnumHandler, None)
    return

def list_inner_windows(whndl):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            hwnds[win32gui.GetClassName(hwnd)] = hwnd
        return True
    hwnds = {}
    win32gui.EnumChildWindows(whndl, callback, hwnds)
    print(hwnds)
    return 

def get_handle(windowName):
    return win32gui.FindWindow(None, windowName)

def press_key(hwnd, key, hold_sec):
    #Todo: threading
    win32gui.SetForegroundWindow(hwnd)
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, key, 0)
    sleep(hold_sec);
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, key, 0)
            

#Todo delete
def main():
    
    if 0:
        #list_windows()
        list_inner_windows(1967572)
    else:
        # init window handle
        window_name = "Binding of Isaac: Repentance"
        hwnd = get_handle(window_name)
        
        press_key(hwnd, VK_RETURN, 0.1)
        press_key(hwnd, VK_KEY_W, 2)

    return
main()