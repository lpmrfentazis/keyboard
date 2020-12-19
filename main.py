#!C:/Users/Admin/AppData/Local/Programs/Python/Python37/python.exe

from tests import sleep, timeit, press_times
from pynput import keyboard

flag = 0
num = 0

class user:
    speed = 0   # per minute
    Interval = []
    Pess = []
    fly = []

    def go_average():
        pass


def on_press(key):
    global flag, num

    if key == keyboard.Key.backspace:
        num-=1

    else:
        num+=1

        if flag == 1:
            press_times(2, num)
        else: 
            flag = 1
            if key == keyboard.Key.backspace:
                answer = press_times(flag, num, "backspace")
                print()
                print("press time", "inter time", "fly time", "num", sep="\t")
                print(*answer, "\t", num)
            else:
                answer = press_times(flag, num)
                print()
                print("press time", "inter time", "fly time", "num", sep="\t")
                print(*answer, num, sep="\t")



def on_release(key):
    global flag
    
    flag = 0
    press_times(0, num)


    

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