# for i in range(100_000_000):
#     print(i)

# Below will run indefinitely, alternating between tasks 1 and 2
# since they yield after each print, but have an infinite loop
def task1():
    while True:
        print('Task 1')
        yield


def task2():
    while True:
        print('Task 2')
        yield


event_loop = [task1(), task2()]

while True:
    for task in event_loop:
        next(task)
