"""
chapter1
python advanced - python variable scope
scope, global, nonlocal, locals, globals
"""


a = 10  # global variable


def foo():
    # read global variable
    print(a)  # -> 10


foo()
print(a)  # 10

b = 20


def bar():
    b = 30
    print(b)  # 30


print(b)

# ex3

c = 40


def foobar():
    c = c + 10  # error
    c = 10
    c += 100

    print(c)


foobar()


# ex4
d = 50


def barfoo():
    global d  # global 예약어를 통해 수정가능 -> but global 선언은 자제하자
    d = d + 10
    d += 100
    print(d)


barfoo()


# ex5
# closure
def outer():
    e = 70

    def inner():
        nonlocal e  # important!
        e += 10
        print(e)

    return inner


in_test = outer()  # closure
in_test()


def func(var):
    x = 10

    def printer():
        print("inner")

    print("fucn", locals())


func("Hi")


print("ex7", globals())
test_variable = 100
# globals()["test_variable"]=100
print(globals())

for i in range(1, 10):
    for k in range(1, 10):
        globals()["plus_{}_{}".format(i, k)] = i + k
print(globals())
print(plus_5_5)
print(plus_9_9)
# 전역변수는 고정값에 사용
# 지역변수 : 소멸주기 - 함수 실행 해제시
# 전역변수는 지역내에서 수정안하는것을 권장
