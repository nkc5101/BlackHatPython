import ctypes
import random
import time
import sys

user = ctypes.windll.user32
kernel = ctypes.windll.kernel32

keystrokes = 0
mouse_clicks = 0
double_clicks = 0

class LASTINPUTINFO(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_uint),
                ("dwTime", ctypes.c_ulong)]

    def get_last_input(self):

        struct_lastinputinfo = LASTINPUTINFO()
        struct_lastinputinfo.cbSize = ctypes.sizeof(LASTINPUTINFO)

        user.GetLastInputInfor(ctypes.byref(struct_lastinputinfo))

        run_time = kernel.GetTickCount()

        elpased = run_time - struct_lastinputinfo.dwTime

        print "It's been %d milliseconds since the last input event" % elpased

        return elpased

    while True:
        get_last_input()
        time.sleep(1)