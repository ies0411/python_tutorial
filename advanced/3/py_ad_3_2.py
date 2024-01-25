"""
    meta: meta class
    type(name,base,dct) dynamic metaclass
    1. 메타클래스 동적 생성
    2. 동적 생성한 메타클래스 -> 커스텀 메타클래스 생성
    3. 의도하는 방향으로 직접 클래스 생성에 관여 할 수 있는 큰 장점
"""


# type 동적 클래스 생성 예제


# name(이름), bases(상속), Dct(속성,메소드)

# class Sample1:
#     pass


s1 = type("sample1", (), {})

print(s1)
print(type(s1))
print(s1.__base__)
print(s1.__dict__)


# 동적 생성 + 상속
class Parent1:
    pass


# class Sample2(Parent1)
#     attr1=100
#     attr2="hi"

s2 = type("Sample2", (Parent1,), dict(attr1=100, attr2="hi"))


print(s2)
print(type(s2))
print(s2.__base__)
print(s2.__dict__)
print(s2.attr1, s2.attr2)


# 2
class SampleEx:
    attr1 = 3
    attr2 = 100

    def add(self, m, n):
        return m + n

    def mul(self, m, n):
        return m * n


ex = SampleEx()
print(ex.attr1)
print(ex.attr2)
print(ex.add(100, 200))
print(ex.mul(100, 20))

s3 = type(
    "Sample3",
    (object,),
    {"attr1": 30, "attr2": 100, "add": lambda x, y: x + y, "mul": lambda x, y: x * y},
)
print(s3.attr1)
print(s3.attr2)
print(s3.add(100, 200))
print(s3.mul(100, 20))
