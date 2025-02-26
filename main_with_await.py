import yield_to_await


async def task1():
    for _ in range(2):
        print('Task 1')
        await yield_to_await.sleep(1)


async def task2():
    for _ in range(3):
        print('Task 2')
        await yield_to_await.sleep(0)


async def main():
    one = yield_to_await.create_task(task1())
    two = yield_to_await.create_task(task2())

    await one
    await two

    print('Done')

if __name__ == '__main__':
    yield_to_await.run(main())
