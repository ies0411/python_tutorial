# closure

# 변수범위


def func_v1(a):
    print(a)


func_v1(10)

b = 20


def func_v2(a):
    print(a)
    print(b)


func_v2(10)

c = 30


def func_v3(a):
    global c
    print(c)
    c = 40
    print(a)
    print(c)
    # c = 40 error


func_v3(10)
print(">>", c)


# closure :
# server programming -> concurrency -> race condition, dead lock
# 메모리 공유안하고 메시지 전달로 제어 -> Erlang
# 공유하되 변경되지 않는 (read only, immutable)
# atm, STM을 통해 멀티스레드(coroutine) 프로그래밍에 강점

a = 100

print(a + 100)
print(a + 1000)

print(sum(range(1, 51)))
print(sum(range(51, 101)))


class Averager(object):
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print("inner >> {}/{}".format(self._series, len(self._series)))
        return sum(self._series / len(self._series))


averager_cls = Averager()
print(dir(averager_cls))
print(averager_cls(10))
print(averager_cls(30))
print(averager_cls(50))
