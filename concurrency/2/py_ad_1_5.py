"""
    memory share in multi-processing
    memory sharing, array, value
"""

from multiprocessing import Process, current_process, Value, Array
import os


def generate_update_number(v: int):
    for _ in range(50):
        v += 1
    print(current_process().name, "data", v)


#####################


def generate_update_number(v):
    for _ in range(50):
        v.value += 1
    print(current_process().name, "data", v.value)


########
def main():
    parent_process_id = os.getpid()
    print(parent_process_id)

    processes = []
    ############################
    share_value = 0

    for _ in range(1, 10):
        p = Process(target=generate_update_number, args=(share_value,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(share_value)  # 공유안됨 cuz it is process

    ############################
    share_value = Value("i", 0)  # 공유됨
    # share_numbers = Array("i", range(50))
    # from multiprocess import shared_memory
    # from multiprocess import Manager
    for _ in range(1, 10):
        p = Process(target=generate_update_number, args=(share_value,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(share_value.value)


if __name__ == "__main__":
    main()
