"""
    queue,pipe, communictaions between processes
"""

from multiprocessing import Process, Queue, current_process
import time
import os


def worker(id, baseNum, q):
    process_id = os.getpid()
    process_name = current_process().name
    sub_total = 0
    for i in range(baseNum):
        sub_total += 1
    q.put(sub_total)
    print(process_id, process_name, id, sub_total)


def main():
    parent_process_id = os.getpid()
    print(parent_process_id)

    processes = []
    start_time = time.time()

    q = Queue()

    for i in range(5):
        t = Process(name=str(i), target=worker, args=(i, 1000000, q))
        processes.append(t)
        t.start()

    for process in processes:
        process.join()
    print(time.time() - start_time)
    q.put("exit")
    total = 0
    while True:
        tmp = q.get()
        if tmp == "exit":
            break
        else:
            total += tmp
    print(total)


if __name__ == "__main__":
    main()


"""
    queue,pipe, communictaions between processes
"""

from multiprocessing import Process, Pipe, current_process
import time
import os


def worker(id, baseNum, conn):
    process_id = os.getpid()
    process_name = current_process().name
    sub_total = 0
    for i in range(baseNum):
        sub_total += 1
    conn.send(sub_total)

    print(process_id, process_name, id, sub_total)


def main():
    parent_process_id = os.getpid()
    print(parent_process_id)

    start_time = time.time()

    parent_conn, child_conn = Pipe()

    t = Process(name=str(1), target=worker, args=(1, 1000000, child_conn))
    t.start()

    t.join()
    print(time.time() - start_time)
    print(parent_conn.recv())


if __name__ == "__main__":
    main()
