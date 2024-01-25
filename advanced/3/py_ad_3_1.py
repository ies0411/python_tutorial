"""
    meta:class of class, type, meta class, custom meta class
    1. class만드는 역할 -> class custom
    2. framework작성시 필수
    3. 동적 생성(type), 커스텀 생성(type)함수
    4. 커스텀 클래스 -> 검증클래스 등
    5. 엄격한 class 사용 요구, 메소드 오버라이드 요구
"""


# type 예제
class SampleA:  # class == object, != instance
    pass


obj1 = SampleA()
# obj1 == instance
obj2 = SampleA()

print(obj1.__class__)
print(type(obj1))
print(obj1.__class__ is type(obj1))  # true
print(obj1.__class__.__class__)  # type
# obj1 -> sampleA instance
# sampleA -> type meta class
# type -> type meta class

# ex2

# int,dict
n = 10
d = {"a": 10, "b": 20}


class SampleB:
    pass


obj2 = SampleB()

for o in (n, d, obj2):
    print(type(o), type(o) is o.__class__, o.__class__.__class__)
