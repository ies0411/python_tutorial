"""
    descriptor vs property, low level(descriptor), high level(property)
    descriptor
    1.상황에 맞는 메소드 구현을 통한 객체 지향 프로그래밍 구현
    2.property와 달리 reuse가능
    3.ORM framework사용
"""
# ex1
import os


class DirectoryFileCount:
    def __get__(self, obj, objtype=None):
        print(os.listdir(obj.dirname))
        return len(os.listdir(obj.dirname))


class DirectoryPath:
    size = DirectoryFileCount()

    def __init__(self, dirname):
        self.dirname = dirname


s = DirectoryPath("./")
s.size

import logging

logging.basicConfig(
    format="%(asctime)s %(message)s", level=logging.INFO, datafmt="%Y-%m-%d %H:%M:%S"
)


class LoggedScoreAccess:
    def __init__(self, value=50):
        self.value = value

    def __get__(self, obj, objtype=None):
        logging.info("accessing %r giving %r", "score", self.value)
        return self.value
    def __set__(self,obj,value)
        logging.info("updating %r giving %r", "score", self.value)
        self.value= value

class Student:
    score = LoggedScoreAccess()

    def __init__(self, name):
        self.name = name

s1 = Student("kim")
s2 = Student("lee")

s1.score
s1.score +=20
s1.score

vars(s1)
vars(s2)
s1.__dict__
s2.__dict__