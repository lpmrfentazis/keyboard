#!C:/Users/Admin/AppData/Local/Programs/Python/Python37/python.exe

from tests import sleep, timeit, press_times
from pynput import keyboard


menu = "Menu:\n" + "0 - Create new user\n" + "1 - Login\n" + "2 - Test"
mode = 3


class User:
    user_name = ""
    user_password = ""
    interval = []
    press = []
    fly = []

    press_average = 0
    interval_average = 0
    fly_average = 0

    def go_average(self):
        #print(self.press)
        self.press_average = round( sum(self.press) / len(self.press), 1)
        self.interval_average = round( sum(self.interval) / len(self.interval), 1)
        self.fly_average = round( sum(self.fly) / len(self.fly), 1)
    
    def to_empty(self):
        self.press = []
        self.interval = []
        self.fly = []

        self.press_average = 0
        self.interval_average = 0
        self.fly_average = 0
        

    def save_user(self):
        with open("users/{}.txt".format(self.user_name), "w") as f:
            f.write(self.user_name + "\n")
            f.write(self.user_password + "\n")
            f.write(str(self.press_average) + "\n")
            f.write(str(self.interval_average) + "\n")
            f.write(str(self.fly_average) + "\n")

    def check_user(self):
        with open("users/{}.txt".format(self.user_name)) as f:
            lines = f.readlines()

            if (lines[1].split("\n")[0] == self.user_password) and (abs(self.press_average - float(lines[2].split("\n")[0])) < 10000):
                return 1
            else:
                return 0


flag = 0
num = 0
user = User()


def check_username(username):
    from os import listdir

    if username == "": 
        print("The username cannot be empty")
        return 1

    for files in listdir("users/"):
            if username in files:
                
                return 1
    return 0


def create_user(user):
    global num
    temp = ""

    user.go_average()
    print("\n", "Collected statistics:\n")
    print("press time", "inter time", "fly time", sep="\t")
    print(str(round(user.press_average, 1)) + " µs", str(round(user.interval_average, 1)) + " µs", str(round(user.fly_average, 1)) + " µs", sep="\t")

    while check_username(temp) == 1:
        print("The name is already in use")
        print("\nTo cancel, enter 0\n")
        temp = input("Enter username: ")
        if temp == "0":
            user.to_empty()
            num = 0
            return False 
    else:
        user.user_name = temp
        temp = ""
        while temp == "":
            print("\nTo cancel, enter 0")
            print("The password cannot be empty\n")
            temp = input("Enter user password: ")
            if temp == "0":
                user.to_empty()
                num = 0
                return False
        else:
            user.user_password = temp
            user.save_user()
            user.to_empty()
            num = 0
            return False


def login(user):
    global num
    temp = input("Enter username: ")

    while check_username(temp) == 0:
        print("\nTo cancel, enter 0")
        print("The user does not exist\n")
        temp = input("Enter username: ")

        if temp == "0":
            user.to_empty()
            num = 0
            return False

    else:
        user.user_name = temp
        temp = ""
        while temp == "":
            print("\nTo cancel, enter 0")
            print("The password cannot be empty\n")
            temp = input("Enter user password: ")
            if temp == "0":
                user.to_empty()
                num = 0
                return False
        else:
            user.user_password = temp
            if user.check_user():
                print("Welcome")
            else:
                print("Access denied")
            user.to_empty()
            num = 0
            return False


def test_mode(user):
    global num

    user.go_average()
    print("\n", "Collected statistics:\n")
    print("press time", "inter time", "fly time", sep="\t")
    print(str(round(user.press_average, 1)) + " µs", str(round(user.interval_average, 1)) + " µs", str(round(user.fly_average, 1)) + " µs", sep="\t")
    user.to_empty()
    num = 0

    return False


def on_press(key):
    global flag, num, user, mode
    

    if key == keyboard.Key.esc:
        if mode == 0:
            return create_user(user)
        if mode == 1:
            return login(user)
        if mode == 2:
            return test_mode(user)

    else:

        if flag == 1:
            press_times(2, num)
        else: 
            num+=1
            flag = 1
            answer = press_times(flag, num)

            #print("\npress time", "inter time", "fly time", "num", sep="\t")
            #print(*answer, num, sep="\t")

            if num != 1:
                user.press.append(answer[0].seconds * 10**6 + answer[0].microseconds)
                user.interval.append(answer[1].seconds * 10**6 + answer[1].microseconds)
                user.fly.append(answer[2].seconds * 10**6 + answer[2].microseconds)
            

def on_release(key):
    global flag
    flag = 0
    press_times(0, num)
    """
    try:
        print(key.char)
    except:
        pass"""


def main():
    global menu, mode
    print(menu)

    while 1:
        key = input()

        if key == "0":
            print("Enter ~50 symbols")
            mode = 0
            with keyboard.Listener(on_press= on_press,
                                   on_release= on_release) as listener:
                listener.join()

        if key == "1":
            print("Enter ~50 symbols")
            mode = 1
            with keyboard.Listener(on_press= on_press,
                                   on_release= on_release) as listener:
                listener.join()

        if key == "2":
            mode = 2
            with keyboard.Listener(on_press= on_press,
                                   on_release= on_release) as listener:
                listener.join()

        else:
            print("\n")
            print(menu)

    

if __name__ == "__main__":
    main()