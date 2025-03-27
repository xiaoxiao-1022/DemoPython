# # 定义装饰器
# def decorator(func):
#     def wrapper(*args, **kw):
#         return func()
#     return wrapper
#
# # 定义业务函数并进行装饰
# @decorator
# def function():
#     print("hello, decorator")


# 这是装饰器函数，参数 func 是被装饰的函数
def logger(func):
    def wrapper(*args, **kw):
        print("我准备开始执行：{} 函数了:".format(func.__name__))

        # 真正执行的是这行。
        func(*args, **kw)

        print("主人，我执行完啦。")

    return wrapper


@logger
def add(x, y):
    print("{} + {} = {}".format(x, y, x + y))


add(1, 2)


def say_hello(contry):
    def wrapper(func):
        def deco(*args, **kwargs):
            if contry == "china":
                print("你好!")
            elif contry == "america":
                print("hello.")
            else:
                return

            # 真正执行函数的地方
            func(*args, **kwargs)

        return deco

    return wrapper


@say_hello("china")
def xiaoming():
    pass


# jack，美国人
@say_hello("america")
def jack():
    pass


xiaoming()
print("------------")
jack()


class logger(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(
            "[INFO]: the function {func}() is running...".format(
                func=self.func.__name__
            )
        )
        return self.func(*args, **kwargs)


@logger
def say(something):
    print("say {}!".format(something))


say("hello")
