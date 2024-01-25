# underscore
# access modifier
# 접근 지정자


# 1. 인터프리터, 2. 값 무시, 3. 네이밍(국제화, 자리수)

# unpacking
x, _, y = (1, 2, 3)
print(x, y)

a, *_, b = (1, 2, 3, 4, 5)
print(a, b)

a, *i, b = (1, 2, 3, 4, 5)

print(a, i, b)


for _ in range(10):
    pass

for _, val in enumerate(range(10)):
    pass

# name : public
# _name : protected
# __name : private
# python -> Public 강제 x, 약속된 규약
# 타 클래스(클래스 변수, 인스턴스 변수 값 쓰기 장려 안함) -> Naming Mangling but 강제아님
# 타 클래스 __접근하지 않는 것이 원칙

# No use Property


class SampleA:
    def __init__(self):
        self.x = 0
        self.__y = 0
        self._z = 0


a = SampleA()
a.x = 1
print(f"{a.x}")
print(f"{a.__y}")  # error
print(a._z)
print(dir(a))  # name mangle확인가능
a._SampleA__y = 2  # 변경은 가능 but 룰


# method (getter,setter)
class SampleB(object):
    def __init__(self):
        self.x = 0
        self.__y = 0

    def get_y(self):
        return self.__y

    def set_y(self, value):
        self.__y = value


b = SampleB()
b.x = 1
b.set_y(2)
