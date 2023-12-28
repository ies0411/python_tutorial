# sequence , iterator, function, class
# class안에 정의할수있는 built-in method 0>
# magic method : __init__, __str__, __repr__ ...
# CPython 공부

# 기본형
print(int)  # class
print(dir(float))

n = 10  # class
print(n + 100)  # __add__의 magic method가 operator overriding
print(n.__add__(100))
print(n.__doc__)
print(n.__bool__())

# overriding임 결국 모두


# example1
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return "{},{}".format(self._name, self._price)

    def __add__(self, x):
        return self._price + x._price

    def __sub__(self, x):
        return self._price - x._price

    # def __le__
    # def __ge__


s1 = Fruit("orange", 100)
s2 = Fruit("banana", 30)
print(s1 + s2)  # magic method's overriding
