"""
    multithreading - GIL
    CPython, 메모리관리, GIL 사용 이유

    GIL(Global Interpreter Lock)
    1. cpython -> python(byte) 실행 시 여러 thread를 사용할 경우
        -> 단일 스레드만이 python object에 접근하게 제한하는 mutex
    2. cpython 메모리 관리가 취약하기 때문(thread-safe)
    3. 단일 스레드로 충분히 빠르다
    4. 스레드 대신, 프로세스 사용하면 됨(numpy,scipy 는 GIL 외부 영역에서 효율적인 코딩)
    5. 병렬 처리는 multiprocessing, asyncio선택지 다양함
    6. thread 동시성 완벽 처리를 위해 -> jython, IronPython, Stackless Python 등이 존재


"""
import logging
import threading
import time


def thread_func(name):
    logging.info("start sub : %s", name)
    time.sleep(3)
    logging.info("finish sub : %s", name)


# 메인 영역
if __name__ == "__main__":
    format = "%(asctime)s:%(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M;%S")
    logging.info("main")
    x = threading.Thread(target=thread_func, args=("First"))

    logging.info("main2")
    x.start()
    x.join()  # waiting..
    logging.info("main finish")
