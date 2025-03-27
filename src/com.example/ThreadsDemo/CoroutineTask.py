import asyncio


async def hello(name):
    print("hello", name)
    return "hello" + name


def callback(future):
    print("这里是回调函数，获取返回结果是：", future.result())


coroutine = hello("world")

loop = asyncio.get_event_loop()

task = asyncio.ensure_future(coroutine)
#
# task =loop.create_task(coroutine)
task.add_done_callback(callback)
loop.run_until_complete(task)

# print('返回结果{}'.format(task.re))
