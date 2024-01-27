"""
    daemon, join
    1. 백그라운드에 실행
    2. 메인스레드 종료시 즉시 종료
    3. 주로 백그라운드 무한 대기 이벤트 발생 실행하는 부분 담당 -> JVM(가비지 컬렉터), 자동 저장
    4. 일반 스레드는 작업 종료시까지
"""
import logging
import threading
import time


def thread_func(name, d):
    logging.info("start sub : %s", name)
    # time.sleep(3)
    for i in d:
        pass
    logging.info("finish sub : %s", name)


# 메인 영역
if __name__ == "__main__":
    format = "%(asctime)s:%(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M;%S")
    logging.info("main")
    x = threading.Thread(target=thread_func, args=("First", range(200000)), daemon=True)
    y = threading.Thread(target=thread_func, args=("Two  ", range(1000)), daemon=True)
    logging.info("main2")
    x.start()
    y.start()
    print(x.isDaemon())
    # x.join()  # waiting..
    # y.join()
    while True:
        pass
    logging.info("main finish")
