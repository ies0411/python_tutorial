"""
    cpu bound - synchronous

    cpu bound : 연산
"""


import time


def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums(numbers):
    result = []
    for number in numbers:
        result.append(cpu_bound(number))
    return result


def main():
    numbers = [3_000_000 + x for x in range(30)]
    start_time = time.time()
    total = find_sums(numbers)
    print(total)
    print(time.time() - start_time)


if __name__ == "__main__":
    main()


##################

import time
from multiprocessing import current_process, Array, Manager, Process, freeze_support
import os


def cpu_bound(number, total_list):
    process_id = os.getpid()
    process_name = current_process().name
    print(process_id, process_name)

    total_list.append(sum(i * i for i in range(number)))


def main():
    numbers = [3_000_000 + x for x in range(30)]
    processes = list()
    manager = Manager()
    total_list = manager.list()

    start_time = time.time()
    for i in numbers:  # 1 ~ 100
        t = Process(name=str(i), target=cpu_bound, args=(i, total_list))
        processes.append(t)
        t.start()

    for process in processes:
        process.join()

    # total = find_sums(numbers)
    print(total_list)
    print(time.time() - start_time)


if __name__ == "__main__":
    # freeze_support()
    main()
