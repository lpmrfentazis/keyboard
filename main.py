#!C:/Users/Admin/AppData/Local/Programs/Python/Python37/python.exe

from tests import sleep, timeit, press_times
from pynput import keyboard

flag = 0

class user:
    speed = 0   # per minute
    Interval = []
    Pess = []
    fly = []

    def go_average():
        pass


def on_press(key):
    global flag

    if flag == 1:
        press_times(2)
    else: 
        flag = 1
        print()
        print("press time", "inter time", "fly time", sep="\t")
        print(*press_times(1))
        
    
    """
    try:
        print(key.char)
    except:
        pass
    """


def on_release(key):
    global flag
    
    flag = 0
    press_times(flag)

    try:
        print(key.char)
    except:
        pass

    if key == keyboard.Key.esc:
        # Stop listener
        return False


def main():
    with keyboard.Listener(on_press= on_press,
                           on_release= on_release) as listener:
        listener.join()

    

if __name__ == "__main__":
    main()