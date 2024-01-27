"""
    many threads, concurrent.futures, poolExcutor
    1.python 3.2이상
    2.concurrent.futures
    3.with 사용으로 생성, 소멸 라이프사이클 관리 용이
    4.디버깅하기 난해
    5.대기중인 작업 -> Queue -> 완료상태 조사 -> 결과 또는 예외 반환 -> 단일화(캡슐화)
"""


import logging
from concurrent.futures import ThreadPoolExecutor
import time


def task(name):
    logging.info(name)
    result = 0
    for i in range(10001):
        result = result + i
    logging.info(name, result)
    return result


def main():
    format = "%(asctime)s:%(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M;%S")
    logging.info("main")
    # 1
    # max_workers : 작업의 개수가 넘어가면 직접 설정이 유리
    excutor = ThreadPoolExecutor(max_workers=3)
    task1 = excutor.submit(task, ("first"))
    task2 = excutor.submit(task, ("second"))

    print(task1.result())
    print(task2.result())

    # 2
    with ThreadPoolExecutor(max_workers=3) as excutor:
        tasks = excutor.map(task, ["First", "Second"])
        print(list(tasks))


if __name__ == "__main__":
    main()
