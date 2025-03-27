import asyncio


async def do_some_works(x):
    print("Waiting:", x)
    await asyncio.sleep(x)
    return "Done after{}s".format(x)


coroutine1 = do_some_works(1)
coroutine2 = do_some_works(5)
coroutine3 = do_some_works(7)

tasks = [
    # 将协程转为task对象
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3),
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print("Task ret:", task.result())
