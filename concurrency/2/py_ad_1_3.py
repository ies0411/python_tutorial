"""
    naming, parallel processing

"""
from multiprocessing import Process, current_process
import os
import random
import time


def square(n):
    time.sleep(random.randint(1, 3))
    process_id = os.getpid()
    process_name = current_process().name
    result = n * n
    print(process_id)
    print(process_name)
    print(result)


def main():
    parent_process_id = os.getpid()
    print(parent_process_id)
    processes = []
    for i in range(10):
        t = Process(name=str(i), target=square, args=(i,))
        processes.append(t)
        t.start()
    for process in processes:
        process.join()


if __name__ == "__main__":
    main()
