import time
import re
import keyboard
import ctypes
import win32gui

name = "BBQ Bot"
version = "0.2.1"
window = win32gui
window_name = "Survive the wild "
is_game_foreground = False
is_looping_t = False
is_looping_space = False

## press the T key to combine hands, for gutting animals and using boats
def combineHands():
    global is_game_foreground
    global is_looping_t
    if is_game_foreground:
        # ("pressing T")
        is_looping_space = False
        is_looping_t = True


## press space to use an item in your hands
def useItem():
    global is_game_foreground
    global is_looping_space
    if is_game_foreground:
        # ("pressing space")
        is_looping_t = False
        is_looping_space = True


## stop the bot, kill all action 
def stop():
    global is_looping_space
    global is_looping_t
    is_looping_space = False
    is_looping_t = False



## program starts here
ctypes.windll.kernel32.SetConsoleTitleW(name + ", V" + version)
print ("welcome to " + name + " V " + version)

print('Press Ctrl-C to quit.')
try:
        # register keys, the one that the game is not using
        keyboard.add_hotkey('f9', combineHands)
        keyboard.add_hotkey('f10', useItem)
        keyboard.add_hotkey('f11', stop)
        keyboard.add_hotkey('<', stop)

        while True:
            time.sleep(0.002) # seconds for a tick
            
            # handle next versions of the game with regex
            if re.sub("\d{1}.\d{2}.\d{1}", "", window.GetWindowText (window.GetForegroundWindow()) ) == window_name:
                # ("\n game is now foreground")
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
                # ("leaving game window, stopping actions")
                stop()
                is_game_foreground = False
                
except KeyboardInterrupt:
    print('\nclosing program...')