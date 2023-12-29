# closure : 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근(엑세스) 가능
# function도 python 내부적으로는 class라 가능한듯
# closure 사용
def closure_ex1():
    # free variable, closure region
    series = []

    def averager(v):
        series.append(v)
        print("inner >> {}/{}".format(series, len(series)))
        return sum(series) / len(series)

    return averager


avg_closure1 = closure_ex1()

print(avg_closure1)
print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))


# function inspection
print(dir(avg_closure1))
print(avg_closure1.__code__)
print(avg_closure1.__code__.co_freevars)
print(avg_closure1.__closure__[0].cell_contents)


# 잘못된 closure
def closure_ex2():
    # free variable
    cnt = 0
    total = 0

    def averager(v):
        cnt += 1
        total += v
        return total / cnt

    return averager


avg_closure2 = closure_ex2()
avg_closure2(10)


def closure_ex3():
    # free variable
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt

    return averager


avg_closure3 = closure_ex3()
avg_closure3(10)
avg_closure3(120)
avg_closure3(30)
