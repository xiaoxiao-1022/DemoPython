from Time_timer import timer
from ThreadTest import *


@timer("【单线程】")
def single_thread(func, type=""):
    for i in range(10):
        func(i)


single_thread(count, type="CPU计算密集型")
single_thread(io_disk, type="磁盘IO密集型")
single_thread(io_request, type="网络IO密集型")
single_thread(io_simulation, type="模拟IO密集型")
