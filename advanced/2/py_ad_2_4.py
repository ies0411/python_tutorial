"""
    method overriding
    keyword : overriding, oop, 다형성
"""

"""
    오버라이딩 효과
    1. 서브클래스(자식)에서 슈퍼(부모)클래스를 호출 후 사용
    2. 메소드 재 정의 후 사용가능
    3. 부모클래스의 메소드를 추상화 후 사용가능 (구조적 접근)
    4. 확장 가능, 다형성(다양한 방식으로 동작)
    5. 가독성 증가, 오류가능성 감소, 메소드 이름 절약, 유지보수성 증가 등
"""


# overriding


class ParentEx1(object):
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value


class ChildEx1(ParentEx1):
    pass


c1 = ChildEx1()
p1 = ParentEx1()

print(c1.get_value())
print(dir(c1))

print(ParentEx1.__dict__)
print(ChildEx1.__dict__)
# 인스턴스되는순간 상속


# ex2
# 재정의 overriding
class ParentEx2:
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value


class ChildEx2(ParentEx2):
    def get_value(self):
        return self.value * 10


c2 = ChildEx2()
c2.get_value()

# ex3
# 다형성
import datetime


class Logger(object):
    def log(self, msg):
        print(msg)


class TimestampLogger(Logger):
    def log(self, msg):
        message = f"{datetime.datetime.now()},{msg}"
        # super().log(message)  이렇게 해도됨
        super(TimestampLogger, self).log(message)


class DateLogger(Logger):
    def log(self, msg):
        message = f"{datetime.datetime.now().strftime('%Y-%m-%d'),{msg}}"
        super(DateLogger, self).log(message)


l = Logger()
t = TimestampLogger()
d = DateLogger()
l.log("logger")
t.log("logger")
d.log("logger")
