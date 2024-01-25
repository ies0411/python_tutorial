# property : getter, setter
# @property

"""
    1. pythonic
    2. 변수제약설정
    3. getter,setter 효과 동등(코드 일관성)
        - 갭슐화, 유효성 검사 기능 추가 용이
        - 대체 표현(속성 노출, 내부의 표현 숨기기 가능)
        - 속성의 수명 및 메모리 관리 용이
        - 디버깅 용이
        - library 상호 운용성 증가(ex, Django)
"""

# property


class SampleA(object):
    def __init__(self):
        self.x = 0
        self.__y = 0  # private

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @y.deleter
    def y(self):
        del self.__y


a = SampleA()
a.x = 1
a.y = 2
del a.y


# property with restriction
class SampleB(object):
    def __init__(self):
        self.x = 0
        self.__y = 0  # private

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("input above zero")
        self.__y = value

    @y.deleter
    def y(self):
        del self.__y


b = SampleB()

b.x = 1
b.x = -4
