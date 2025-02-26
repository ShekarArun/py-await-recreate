# for i in range(100_000_000):
#     print(i)

# # Below will run indefinitely, alternating between tasks 1 and 2
# # since they yield after each print, but have an infinite loop
# def task1():
#     while True:
#         print('Task 1')
#         yield


# def task2():
#     while True:
#         print('Task 2')
#         yield


# event_loop = [task1(), task2()]

# while True:
#     for task in event_loop:
#         next(task)

# Below example shows the transfer of control in the event loop
# Whenever the process sleeps, it yields and upon completion
# Of the specified time, proceeds to the next line of code
import time


def sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        # This returns control whenever the time limit hasn't been reached
        yield


def task1():
    while True:
        print('Task 1')
        yield from sleep(2)


def task2():
    while True:
        print('Task 2')
        yield from sleep(5)


event_loop = [task1(), task2()]

while True:
    for task in event_loop:
        next(task)
