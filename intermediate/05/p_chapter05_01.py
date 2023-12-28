# 함수형 프로그래밍, pure function
# 일급함수 first class
# 1.runtime 초기화
# 2.변수 할당 가능
# 3.함수 인수 전달 가능
# 4.함수 결과 반환 가능(return)


def factorial(n):
    """
    n:int
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


class A:
    pass


print(factorial(5))
print(factorial.__doc__)
print(type(factorial), type(A))
print(dir(factorial))
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
print(factorial.__name__)
print(factorial.__code__)

# 변수 할당
var_func = factorial
print(var_func)
print(var_func(10))
print(list(map(var_func, range(1, 11))))

# 인수전달(higher-order function)
# map, filter,reduce
print(list(map(var_func, filter(lambda x: x % 2, range(1, 6)))))
print([var_func(i) for i in range(1, 6) if i % 2])

# reduce
from functools import reduce
from operator import add


print(reduce(add, range(1, 11)))
print(sum(range(1, 11)))

# lambda
# 가급적 주석 작성
# 가급적 일반함수 작성

print(reduce(lambda x, t: x + t, range(1, 11)))

# callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
print(
    callable(str),
    callable(A),
    callable(list),
    callable(var_func),
    callable(factorial),
    callable(3, 14),
)
# partial 사용법 ** 인수고정 -> callback함수
from operator import mul
from functools import partial

print(mul(10, 2), 10 * 2)

# 인수고정
five = partial(mul, 5)

print(five(10))
six = partial(five, 6)
print(six())
print(six(1))  # error, too much parameter

print([five(i) for i in range(1, 10)])
print(list(map(five, range(1, 11))))
