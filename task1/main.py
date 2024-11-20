import asyncio


async def timer_tick():
    n = 1
    while True:
        print(n)
        n += 1
        await asyncio.sleep(1)


async def async_task(delay):
    print('Задача уснула на {} секунд'.format(delay))
    await asyncio.sleep(delay)
    print("Задача успешно выполнена за {} секунд".format(delay))
    
    

async def main():
    task1 = asyncio.create_task(async_task(10))
    task2 = asyncio.create_task(async_task(3))
    task3 = asyncio.create_task(timer_tick())

    await asyncio.gather(task1, task2, task3)


if __name__ == '__main__':
    asyncio.run(main())