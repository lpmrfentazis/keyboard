#!C:/Users/Admin/AppData/Local/Programs/Python/Python37/python.exe

from tests import sleep, timeit, press_times
from pynput import keyboard


class User:
    speed = 0   # per minute
    interval = []
    press = []
    fly = []

    press_average = 0
    interval_average = 0
    fly_average = 0

    def go_average(self):
        self.press_average = sum(self.press) / len(self.press)
        self.interval_average = sum(self.interval) / len(self.interval)
        self.fly_average = sum(self.fly) / len(self.fly)


flag = 0
num = 0
user = User()


def on_press(key):
    global flag, num, user

    if key == keyboard.Key.esc:
        user.go_average()
        print("press time", "inter time", "fly time", "num", sep="\t")
        print(user.press_average + "µs", user.interval_average + "µs", user.fly_average + "µs", sep="\t")
        return False

    else:

        if flag == 1:
            press_times(2, num)
        else: 
            num+=1
            flag = 1
            answer = press_times(flag, num)
            print()
            print("press time", "inter time", "fly time", "num", sep="\t")
            print(*answer, num, sep="\t")

            if num != 1:
                user.press.append(answer[0].seconds * 10**6 + answer[0].microseconds)
                user.interval.append(answer[1].seconds * 10**6 + answer[1].microseconds)
                user.fly.append(answer[2].seconds * 10**6 + answer[2].microseconds)
            




def on_release(key):
    global flag
    
    flag = 0
    press_times(0, num)

    try:
        print(key.char)
    except:
        pass


def main():
    with keyboard.Listener(on_press= on_press,
                           on_release= on_release) as listener:
        listener.join()

    

if __name__ == "__main__":
    user = User()

    main()