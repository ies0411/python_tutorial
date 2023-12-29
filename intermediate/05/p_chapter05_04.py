# decorator

# 장점 : 중복제거, 코드간결, 공콩함수 / 로깅, 프레임웤, 유효성 체크 -> 공통 기능 / 조합사용
# 단점 : 가독성, 특정 기능에 한정된 함수는 단일함수로 하는게 유리, 디버깅 불편


import time


def perf_clock(func):
    # free
    def perf_clocked(*args):
        st = time.perf_counter()
        result = func(*args)
        et = time.perf_counter() - st
        name = func.__name__
        arg_str = ", ".join(repr(arg) for arg in args)
        print("[%0.5fs] %s(%s) -> %r" % (et, name, arg_str, result))
        return result

    return perf_clocked


def time_func(seconds):
    time.sleep(seconds)


def sum_func(*numbers):
    return sum(numbers)


none_deco1 = perf_clock(time_func)
none_deco2 = perf_clock(sum_func)

print(none_deco1, none_deco1.__code__.co_freevars)
print(none_deco2, none_deco2.__code__.co_freevars)

none_deco1(1.5)
none_deco2(10, 20, 30, 40, 50)


# decorator
@perf_clock
def time_func(seconds):
    time.sleep(seconds)


@perf_clock
def sum_func(*numbers):
    return sum(numbers)


time_func(1.5)
sum_func(10, 20, 30, 40, 50)
