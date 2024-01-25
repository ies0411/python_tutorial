"""
    descriptor,set,get,del,property
    1. 객체에서 서로다른 객체를 속성값으로 가지는 것
    2. read,write,delete등을 미리 정의 가능
    3. data descriptor(set,del), non-data descriptor(get)
    4. 읽기 전용 객체 생성 장점, 클래스를 의도하는 방향으로 생성 가능
"""


# ex1
class DescriptorEx1(object):
    def __init__(self, name="Default"):
        self.name = name

    def __get__(self, obj, objtype):
        return "{}{}{}{}".format(self, obj, objtype, self.name)

    def __set__(self, obj, name):
        print("set called")
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("name should be string")

    def __delete__(self, obj):
        print("delete method is called")
        self.name = None


class Sample1(object):
    name = DescriptorEx1()


s1 = Sample1()
s1.name = "Desceript?"
s1.name = 10
s1.name
del s1.name


# ex2
# class property(fget=None,fset=None,fdel=NOne,doc=NOne)
class DescriptorEx2(object):
    def __init__(self, value):
        self._name = value

    def getVal(self):
        return "get method,{}{}", format(self, self._name)

    def setVal(self, value):
        print("called")
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError("string")

    def delVal(self):
        print("delet")
        self._name = None

    name = property(getVal, setVal, delVal, "property")


s2 = DescriptorEx2("test2")

print(s2.name)
s2.name = "test2 method"
del s2.name
DescriptorEx2.name.__doc__
