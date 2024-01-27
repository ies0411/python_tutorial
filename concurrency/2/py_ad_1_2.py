"""
    join, is_alive
    multiprocessing, processing state

"""

from multiprocessing import Process
import time
import logging


def proc_func(name):
    print(name)
    time.sleep(3)


def main():
    p = Process(target=proc_func, args=("first",))
    p.start()
    # p.terminate()
    p.join()
    print(p.is_alive())


if __name__ == "__main__":
    main()
