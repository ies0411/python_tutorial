"""contextlib, __enter__, __exit__
"""


# ex1
import time


class ExcuteTimer(object):
    def __init__(self, msg):
        self._msg = msg

    def __enter__(self):
        self._start = time.monotonic()
        return self._start

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print(f"logging {exc_type,exc_value,exc_traceback}")
        else:
            print(f"{self._msg} : {time.monotonic()-self._start}")
        return True


with ExcuteTimer("Start! job") as v:
    print("monotonic1 : {v}")
    for i in range(1000000):
        pass
    raise Exception("Raise!")  # 강제로 발생
