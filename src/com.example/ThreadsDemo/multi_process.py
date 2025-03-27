from multiprocessing.dummy import Process

from Time_timer import timer
from ThreadTest import *


@timer("【多进程】")
def multi_process(func, type=""):
    process_list = []
    for x in range(10):
        p = Process(target=func, args=())
        process_list.append(p)
        p.start()
    e = process_list.__len__()

    while True:
        for pr in process_list:
            if not pr.is_alive():
                e -= 1
        if e <= 0:
            break


# 多进程
multi_process(count, type="CPU计算密集型")
multi_process(io_disk, type="磁盘IO密集型")
multi_process(io_request, type="网络IO密集型")
multi_process(io_simulation, type="模拟IO密集型")
