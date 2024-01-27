"""
    Threading basic

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
