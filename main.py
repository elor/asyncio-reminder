import asyncio


async def producer(n: int, sleep_time: float, queue: asyncio.Queue):
    while n >= 0:
        queue.put_nowait(n)
        await asyncio.sleep(sleep_time)
        n -= 1


async def consumer(name: str, queue: asyncio.Queue):
    while True:
        result = await queue.get()
        print(name, result)
        if result == 0:
            return


async def main():
    bobs_queue = asyncio.Queue()
    alices_queue = asyncio.Queue()
    charlie_queue = asyncio.Queue()
    await asyncio.gather(
        asyncio.create_task(producer(6, 0.5, bobs_queue)),
        asyncio.create_task(consumer("Alice", alices_queue)),
        asyncio.create_task(consumer("Bob", bobs_queue)),
        asyncio.create_task(producer(3, 1.0, alices_queue)),
        asyncio.create_task(producer(30, 0.1, charlie_queue)),
        asyncio.create_task(consumer("Charlie", charlie_queue)),
    )

asyncio.run(main())
