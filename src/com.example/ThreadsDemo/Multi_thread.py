from threading import Thread

from Time_timer import timer
from ThreadTest import *


@timer("【多线程】")
def multi_thread(func, type=""):
    thread_list = []
    for i in range(10):
        t = Thread(target=func, args=())
        thread_list.append(t)
        t.start()
    e = len(thread_list)

    while True:
        for th in thread_list:
            if not th.is_alive():
                e -= 1
        if e <= 0:
            break


# 多线程
multi_thread(count, type="CPU计算密集型")
multi_thread(io_disk, type="磁盘IO密集型")
multi_thread(io_request, type="网络IO密集型")
multi_thread(io_simulation, type="模拟IO密集型")
