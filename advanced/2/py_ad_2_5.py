"""
    overloading
    overloading, oop, multiple dispatch
    1. 동일 메소드 재정의
    2. 네이밍 기능 예측
    3. 코드 절약, 가독성 향상
    4. 메소드 파라미터 기반 호출 방식
"""

# ex1
# 동일 이름 메소드 사용 예제
# 동적 타입 검사 - > 런타임에 실행(티입 에러가 실행시에 발견)


class SampleA:
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z

    # packing으로 해결가능
    def add(self, *args):
        sum(args)


a = SampleA()
a.add(2, 3)  # error

dir(a)  # 하나만 있음?


# ex2
class SampleB:
    def add(self, datatype, *args):
        if datatype == "int":
            return sum(args)
        if datatype == "str":
            return "".join([x for x in args])


b = SampleB()
b.add("int", 5, 6)
b.add("str", "a", "b")

# ex3
# multipledispatch, pip install multipledispatch
from multipledispatch import dispatch


class SampleC:
    @dispatch(int, int)
    def product(x, y):
        return x, y

    @dispatch(int, int, int)
    def product(x, y, z):
        return x * y * z

    @dispatch(float, float, float)
    def product(x, y, z):
        return x * y * z


c = SampleC()
c.product(5, 6)
c.product(5, 6, 5)
c.product(5, 6.0, 12.0)
