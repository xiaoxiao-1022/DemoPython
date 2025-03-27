import time


def eat():
    while True:
        if food:
            print("小明 吃完{}了".format(food))
        yield
        print("小明 要开始吃{}...".format(food))
        time.sleep(1)


food = None
MING = eat()  # 产生一个生成器
MING.send(None)  # 预激
food = "苹果"
MING.send("面包")
MING.send("苹果")
MING.send("香肠")
