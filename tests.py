from datetime import datetime, timedelta
from time import sleep

def timeit(func):
    start = datetime.now()

    def temp(*argv):
        func(*argv)

        print(datetime.now() - start)
    return temp

time = timedelta(microseconds=0)
inter_time = timedelta(microseconds=0)
press_time = timedelta(microseconds=0)
fly_time = timedelta(microseconds=0)


def press_times(flag):
    global time, inter_time, press_time, fly_time

    if type(time) == datetime and (time.second > 45): time = timedelta(microseconds=0)
    if type(inter_time) == datetime and (inter_time.second) > 45: inter_time = timedelta(microseconds=0)
    if type(press_time) == datetime and (press_time.second) > 45: press_time = timedelta(microseconds=0)
    if type(fly_time) == datetime and (fly_time.second) > 45: fly_time = timedelta(microseconds=0)
    
    if flag == 1:
        time = datetime.now()

        inter_time = datetime.now() - inter_time
        fly_time = press_time + inter_time
        #print("inter time ", inter_time)
        #print("fly time ", press_time + inter_time)
        return press_time, inter_time, fly_time

        press_time = datetime.now()

    elif flag == 0:
        press_time = datetime.now() - time
        #print(fly_time + press_time)
        #print("press time = ", press_time)
        #print()
        time = datetime.now()
        inter_time = datetime.now()
    