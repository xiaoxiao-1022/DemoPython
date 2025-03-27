import threading


def job1():
    global n, lock
    with lock:
        for i in range(10):
            n += 1
            with lock:
                print("job1", n)
            pass
    pass


def job2():
    global n, lock
    with lock:
        for i in range(10):
            n += 10
            print("job2", n)


n = 0
lock = threading.RLock()
t1 = threading.Thread(target=job1)
t2 = threading.Thread(target=job2)
t1.start()
t2.start()
