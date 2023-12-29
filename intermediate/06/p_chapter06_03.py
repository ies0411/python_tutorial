# coroutine : 단일 스레드, 스텝을 기반으로 동작하는 비동기 작업
# thread : os관리, cpu core에서 실시간, 시분할 비동기 작업 -> 멀티쓰레드
# yield : 메인 <-> 서브

# 서브루팅 : 메인루틴 호출 -> 서브루틴에서 수행(흐름제어)
# 코루틴 : 루틴 실행 중 중지 -> 동시성 프로개르밍
# 코루틴 : 쓰레드에 비해 오버헤드 감소
# 쓰레드 : 싱글쓰레드 -> 멀티쓰레드 -> 복잡 -> race condition, dead lock, context switching cost 높음


# ex1
def coroutine1():
    print(">>started")
    i = yield
    print(">>> received : {}".format(i))


cr1 = coroutine1()
print(cr1, type(cr1))
next(cr1)  # yield 지점까지 서브루틴 수행

# 기본 전달 값은 None
cr1.send(100)  # 값 전송

cr2 = coroutine1()
cr2.send(100)  # error

# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행상태
# GEN_SUSPENDED : yield 대기
# GEN_CLOSED : 실행 완료

# 3.5이상에서  def -> async, yield -> await로 변경가능


def coroutine2(x):
    print(">>>started : {}".format(x))
    y = yield x  # (받는거 = yield 내보내는거)
    print("receive : {}".format(y))
    z = yield x + y
    print("recieved : {}".format(z))


cr3 = coroutine2(10)
from inspect import getgeneratorstate

print(getgeneratorstate(cr3))
print(next(cr3))
print(getgeneratorstate(cr3))
cr3.send(100)
print(getgeneratorstate(cr3))
cr3.send(100)
print(getgeneratorstate(cr3))

# ex3
# stopiteration 자동처리(3.5 await)


def generator1():
    for x in "AB":
        yield x
    for y in range(1, 4):
        yield y


t1 = generator1()
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))

t2 = generator1()
print(list(t2))


def generator2():
    yield from "AB"
    yield from range(1, 4)


t3 = generator2()
print(next(t3))
print(next(t3))
