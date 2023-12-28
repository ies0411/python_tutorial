# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

# tuple
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

print(l_leng1)


# named tuple; tuple인데 dict같음
from collections import namedtuple

Point = namedtuple("Points", "x y")

pt3 = Point(1.0, 5.0)
pt4 = Point(2.0, 1.5)
print(pt3[0])
print(pt3.x)
print(pt3)

l_leng12 = sqrt((pt1.x - pt2.x) ** 2 + (pt1.y - pt2.y) ** 2)

Point1 = namedtuple("Point1", ["x", "y"])
Point2 = namedtuple("POint2", "x, y")
Point3 = namedtuple("Point3", "x y")
Point4 = namedtuple("Point", "x y x class", rename=True)

print(Point4)
p1 = Point1(x=10, y=35)
p4 = Point4(10, 20, 30, 40)

# Dict to unpacking
temp_dict = {"x": 75, "y": 10}
p5 = Point1(**temp_dict)


x, y = p1
print(p1.x + p4.y)

# method

temp = [52, 23]
# _make()
p4 = Point1._make(temp)
print(p4)
# _field
print(p1._fields)  # ('x' , 'y')

# _asdict() : ordereddict
print(p1._asdict())


# example
Classes = namedtuple("Classes", ["rank", "number"])

numbers = [str(n) for n in range(1, 21)]
ranks = "A B C D".split()

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]

print(students)
# 추천
students2 = [
    Classes(rank, number)
    for rank in "A B C D".split()
    for number in [str(n) for n in range(1, 21)]
]

for s in students2
    print(s)