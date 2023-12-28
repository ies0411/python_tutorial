# squence
# container : 서로다른 자료형(list, tuple, collections.deque) a=[3,3.0,'a]
# Flat : 단일 자료형 (str, bytes, bytearray, array.array, memoryview)
# 가변 : list, bytearray, array.array, memoryview, deque
# 불변 : tuple, str, bytes

chars = "+_)(*&^%#@!)"
chars[2] = "d"  # error
code_list1 = []
for s in chars:
    # unicode list
    code_list1.append(ord(s))
print(code_list1)

# comprehending lists
code_list2 = [ord(s) for s in chars]

# comprehending lists + Maps, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
print(code_list3)

code_list4 = list(filter(lambda x: x > 40, map(ord, chars)))

# generator : iterator , 한번에 한개의 항목을 생성(메모리 유지 x)
# __iter__가 있으면 for문에서 실행할수있다
import array


tuple_g = (ord(s) for s in chars)
print(tuple_g)
print(type(tuple_g))
print(next(tuple_g))
print(next(tuple_g))
print(next(tuple_g))


array_g = array.array("I", (ord(s) for s in chars))
print(array_g)
print(type(array_g))
print(array_g.tolist())

print(("%s" % c + str(n) for c in ["A", "B", "C", "D"] for n in range(1, 21)))

for s in ("%s" % c + str(n) for c in ["A", "B", "C", "D"] for n in range(1, 21)):
    print(s)

# list 주의 : deepcopy, shallow copy

marks1 = [["~"] * 3 for _ in range(4)]
print(marks1)
marks2 = [["~"] * 3] * 4

# 수정
marks1[0][1] = "X"  # results of deep copy , different id(address)
print(marks1)

marks2[0][1] = "X"  # results of shallow copy , same id(address)
print(marks2)

print([id(i) for i in marks1])
print([id(i) for i in marks2])
