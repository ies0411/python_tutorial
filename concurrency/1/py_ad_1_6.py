"""
    lock, deadlock
    lock, deadlock, race condition, thread synchronization
    1. 세마포어 : 프로세스간 공유 된 자원에 접근 시 문제 발생 가능성 -> race condition 예방
    2. 뮤텍스 : 공유된 자원의 데이터를 여러 스레드가접근하는 것을 막는 것 -> race condition 예방
    3. 상호 배제를 위한 잠금(lock)처리 -> 데이터 경쟁
    4. 데드락 : 스레드가 자원을 획득하지 못해 다음 처리를 못하는 무한 대기 상황(교착 상태)
    5. thread synchronization 를 통해서 안정적으로 동작하게 처리한다(동기화 메소드, 동기화 블럭)
    6. semaphore와 mutex차이점은 ?
        -> 모두 병렬 프로그래밍 환경
        -> 뮤텍스는 단일 스레드가 리소스 또는 중요 섹션을 소비 허용
        -> 세마포어는 리소스에 대한 제한된 수이 동시 엑세스 허용
"""


import logging
from concurrent.futures import ThreadPoolExecutor
import time
import threading


class FakeDataStore:
    # 공유
    def __init__(self):
        self.value = 0

    # update
    def update(self, n):
        logging.info(n)
        # synchronization
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy


def main():
    format = "%(asctime)s:%(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M;%S")
    logging.info("main")

    store = FakeDataStore()

    with ThreadPoolExecutor(max_workers=3) as executor:
        for n in ["first", "second", "third"]:
            executor.submit(store.update, n)

    print(store.value)


if __name__ == "__main__":
    main()


###### 해결


class FakeDataStore:
    # 공유
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    # update
    def update(self, n):
        logging.info(n)
        # synchronization
        # 방법1
        self._lock.acquire()
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        self._lock.acquire()

        # 방법2
        with self._lock:
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy


def main():
    format = "%(asctime)s:%(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M;%S")
    logging.info("main")

    store = FakeDataStore()

    with ThreadPoolExecutor(max_workers=3) as executor:
        for n in ["first", "second", "third"]:
            executor.submit(store.update, n)

    print(store.value)


if __name__ == "__main__":
    main()
