# https://pythonrepo.com/repo/boppreh-keyboard-python-miscellaneous
# https://danieldusek.com/feeding-key-presses-to-reluctant-games-in-python.html
import time
import datetime
# a module which has functions related to time.
# It can be installed using cmd command:
# pip install time, in the same way as pyautogui.
import pyautogui
import keyboard
import win32gui
"""
pyautogui.typewrite("hello Geeks !") #type a string
pyautogui.typewrite(["a", "left", "ctrlleft"]) # keyboard modifiers chained
pyautogui.hotkey("ctrlleft", "a") #key combinations
"""
# for c hacks
import os
import ctypes
import win32api

window = win32gui
window_name = "Survive the wild 0.99.5"
is_game_foreground = False
start_time = None
is_looping_t = False
is_looping_space = False

PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
   _fields_ = [("wVk", ctypes.c_ushort),
               ("wScan", ctypes.c_ushort),
               ("dwFlags", ctypes.c_ulong),
               ("time", ctypes.c_ulong),
               ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
   _fields_ = [("uMsg", ctypes.c_ulong),
               ("wParamL", ctypes.c_short),
               ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
   _fields_ = [("dx", ctypes.c_long),
               ("dy", ctypes.c_long),
               ("mouseData", ctypes.c_ulong),
               ("dwFlags", ctypes.c_ulong),
               ("time", ctypes.c_ulong),
               ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
   _fields_ = [("ki", KeyBdInput),
               ("mi", MouseInput),
               ("hi", HardwareInput)]


class Input(ctypes.Structure):
   _fields_ = [("type", ctypes.c_ulong),
("ii", Input_I)]

def press_key(key):
   extra = ctypes.c_ulong(0)
   ii_ = Input_I()

   flags = 0x0008

   ii_.ki = KeyBdInput(0, key, flags, 0, ctypes.pointer(extra))
   x = Input(ctypes.c_ulong(1), ii_)
   ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def release_key(key):
   extra = ctypes.c_ulong(0)
   ii_ = Input_I()

   flags = 0x0008 | 0x0002

   ii_.ki = KeyBdInput(0, key, flags, 0, ctypes.pointer(extra))
   x = Input(ctypes.c_ulong(1), ii_)
   ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
  
# Character map
char_map = {
    'q': 0x10, 'w': 0x11, 'e': 0x12, 'r': 0x13, 't': 0x14, 'z': 0x15, 'u': 0x16, 'i': 0x17, 'o': 0x18, 'p':0x19,
    'a': 0x1E, 's': 0x1F, 'd': 0x20, 'f': 0x21, 'g': 0x22, 'h': 0x23, 'j': 0x24, 'k': 0x25, 'l': 0x26,
    'y': 0x2C, 'x': 0x2D, 'c': 0x2E, 'v': 0x2F, 'b': 0x30, 'n': 0x31, 'm': 0x32 }

def calculatestart(self):
    global start_time
    start_time = datetime.datetime.now()

def calculateend(self):
    end_time = datetime.datetime.now()
    global start_time
    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() * 1000
    print(execution_time)

def combineHands():
    global is_game_foreground
    global is_looping_t
    if is_game_foreground:
        print ("pressing T")
        is_looping_t = True
        is_looping_space = False
    
def useItem():
    global is_game_foreground
    global is_looping_space
    if is_game_foreground:
        print ("pressing T")
        is_looping_space = True
        is_looping_t = False
    
def stop():
    global is_looping_space
    global is_looping_t
    is_looping_space = False
    is_looping_t = False
"""
    keyboard.press('t')
    #time.sleep(0.2)
    keyboard.release('t')
    
    time.sleep(0.1)
    
    keyboard.press('t')
    #time.sleep(0.3)
    keyboard.release("t")
    time.sleep(0.1)
    
    keyboard.press('t')
    #time.sleep(0.1)
    keyboard.release("t")
    
    press_key(char_map['t']);release_key(char_map['t'])
    time.sleep(0.3)
    press_key(char_map['t']);release_key(char_map['t'])
    time.sleep(0.2)
    press_key(char_map['t']);release_key(char_map['t'])
    time.sleep(0.1)
    press_key(char_map['t']);release_key(char_map['t'])
    
    
    pyautogui.hotkey("t")
    pyautogui.typewrite("t")
    
    keyboard.send('t')
    
"""

# program starts here
print('Press Ctrl-C to quit.')
try:
        #keyboard.hook_key('<', launch)
        keyboard.add_hotkey('f9', combineHands)
        keyboard.add_hotkey('f10', useItem)
        keyboard.add_hotkey('f11', stop)
        while True:
            time.sleep(0.002) # seconds
            if window.GetWindowText (window.GetForegroundWindow()) == window_name:
                print ("\n game hooked")
                is_game_foreground = True
                if is_looping_t:
                    keyboard.press('t')
                    time.sleep(0.1)
                    keyboard.release('t')
                    time.sleep(0.3)
                elif is_looping_space:
                    keyboard.press('space')
                    time.sleep(0.1)
                    keyboard.release('space')
                    time.sleep(0.3)
                else:
                    pass                
            else:
                stop()
                is_game_foreground = False
            #print ( window.GetWindowText (window.GetForegroundWindow()) )
            #keyboard.on_press_key('t', calculatestart)
            #keyboard.on_release_key("t", calculateend)
                
except KeyboardInterrupt:
    print('\nquitting...')

