# lambda, reduce, map, filter function

# lambda : 익명, 힙 영역, 즉시 소멸, pythonic, 가비지 컬렉션(count=0)
# 일반함수 : 재사용
# 시퀀스형 전처리에 reduce,map,filter주로사용


def test(a, b, c):
    return a + b + c


# ->메모리에 저장됨


# lambda
cal = lambda a, b, c: a * b + c
print(cal(10, 14, 20))


# map(함수,인자)
digits1 = [x * 10 for x in range(1, 11)]
print(digits1)


def ex2_func(x):
    return x**2


# 1
result = map(ex2_func, digits1)
print(result)

# 2
result = map(lambda i: i**2, digits1)
print(result)

# 3
result = list(map(lambda i: i**2, digits1))
print(result)


# 4
def also_square(nums):
    def double(x):
        return x**2

    return map(double, nums)


# filter(func:true or fals,인자(List))
digit2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 1
result = filter(lambda x: x % 2 == 0, digit2)
print(result)
result = list(filter(lambda x: x % 2 == 0, digit2))
print(result)

# 2


def also_events(nums):
    def is_even(x):
        return x % 2 == 0

    return filter(is_even, nums)


print(list(also_events(digit2)))

# reduce누적
# filter,map -> 내장, reduce->외장
from functools import reduce

# 1
digits3 = [x for x in range(1, 101)]
result = reduce(lambda x, y: x + y, digits3)
print(result)


# 2
def also_add(nums):
    def add_plus(x, y):
        return x + y

    return reduce(add_plus, nums)


print(also_add(digits3))
