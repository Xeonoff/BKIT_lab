import random
import time as t


def gen_random(num_count, begin, end):
    mylist = []
    try:
        for i in range(num_count):
            mylist.append(random.randint(begin,end))
    except:
        return []
    return mylist


def cm_timer(sleeping_time):
    start = t.time()
    try:
        sleeping_time = int(sleeping_time)
    except:
        return 0
    t.sleep(sleeping_time)
    return int(t.time()-start)


def sort(data):
    try:
        mas = sorted(data, key=lambda x: abs(x), reverse=True)
    except:
        return 0
    return mas

