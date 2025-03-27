from threading import local, Thread, currentThread

local_data = local()
local_data.name = "local_data"


class MyThread(Thread):
    def run(self):
        print("赋值前-子线程：", currentThread(), local_data.__dict__)
        local_data.name = self.getName()
        print("赋值后-子线程：", currentThread(), local_data.__dict__)


if __name__ == "__main__":
    print("开始前-主线程：", local_data.__dict__)

    t1 = MyThread()
    t1.start()
    t1.join()

    t2 = MyThread()
    t2.start()
    t2.join()
