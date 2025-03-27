import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name, event):
        super().__init__()
        self.name = name
        self.event = event

    def run(self):
        print("thread:{} start at {}".format(self.name, time.ctime(time.time())))
        self.event.wait()
        print("Thread:{} finish at {}".format(self.name, time.ctime(time.time())))


threads = []
event = threading.Event()
[threads.append(MyThread(str(i), event)) for i in range(1, 5)]
event.clear()
[t.start() for t in threads]
print("等待5s...")
time.sleep(5)
print("唤醒所有线程...")
event.set()
