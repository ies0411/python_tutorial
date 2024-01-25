"""python advanced(2), contextmanager, __enter__, __exit__
"""

# with, decorator

import contextlib
import time


@contextlib.contextmanager
def my_file_writer(file_name, method):
    f = open(file_name, method)
    yield f  # __enter__
    f.close()  # __exit__


with my_file_writer("testfile.txt", "w") as f:
    f.write("context manager")


@contextlib.contextmanager
def excuteTimerDc(msg):
    start = time.monotonic()
    try:
        yield start  # __enter__
    except BaseException as e:
        print(f"{msg,e}")
        raise
    else:  # __exit__
        print(f"{msg,time.monotonic()-start}")


with excuteTimerDc("Start! job") as v:
    print("monotonic1 : {v}")
    for i in range(1000000):
        pass
    raise ValueError("Raise!")  # 강제로 발생
