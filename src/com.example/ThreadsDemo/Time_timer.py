import time


def timer(mode):
    def wrapper(func):
        def deco(*args, **kw):
            type = kw.setdefault("type", None)
            t1 = time.time()
            func(*args, **kw)
            t2 = time.time()
            cost_time = t2 - t1
            print("{}-{}花费时间：{}秒".format(mode, type, cost_time))

        return deco

    return wrapper
