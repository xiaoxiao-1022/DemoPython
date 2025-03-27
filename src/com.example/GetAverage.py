def get_ageAverage(a, b):
    return (a + b) / 2


print(get_ageAverage(2, 6))


def func(*args, **kw):
    print(args)
    print(kw)


func(10, 20, c=20, d=40)


def deco():
    age = 10

    def wrapper():
        nonlocal age
        age += 1

    return wrapper


deco()()


def foo():
    print("I am a func")


def bar():
    foo = "I am a string"
    foo_dup = globals().get("foo")
    foo_dup()


bar()
