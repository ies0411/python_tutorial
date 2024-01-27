"""
    producer & consumer pattern
    1. 멀티스레드 디자인 패턴의 정석
    2. 서버측 프로그래밍의 핵심
    3. 주로 허리역할 중요

    1. flog 초기값(0)
    2. set()->1, clear() ->0,wait(1->리턴,0->대기), isset()현 플래그 상태

"""

import concurrent.futures
import logging
import queue
import random
import threading
import time


def producer(queue, event):
    """네트워크 대기 상태(서버)"""
    while not event.is_set():
        message = random.randint(1, 11)
        print("got message", message)
        queue.put(message)
    print("exiting")


def consumer():
    """소비, DB, 웹뷰"""
    while not event.is_set() or not queue.empty():
        message = queue.get()
        print("storing message", message, queue.qsize())
    print("existing")


if __name__ == "__name__":
    # queue size중요
    pipeline = queue.Queue(maxsize=10)
    # flag
    event = threading.Event()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)
        time.sleep(0.1)

        event.set()  # 종료

    # while True:
    #     pass
    # break condition
