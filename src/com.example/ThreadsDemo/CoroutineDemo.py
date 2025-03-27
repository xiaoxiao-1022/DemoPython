import asyncio
from collections.abc import Generator, Coroutine


# async def hello(name):
#     print('hello',name)
#
# if __name__ == '__main__':
#     coroutine=hello('world')
#     print(isinstance(coroutine,Coroutine))


@asyncio.coroutine
def hello():
    # 异步调用asyncio.sleep(1):
    yield from asyncio.sleep(1)


if __name__ == "__main__":
    coroutine = hello()
    print(isinstance(coroutine, Generator))  # True
    print(isinstance(coroutine, Coroutine))  # False
