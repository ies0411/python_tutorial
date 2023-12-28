# tuple advanced
# unpacking

# b, a = a, b
print(divmod(100, 9))
print(divmod(*(100, 9)))
print(*(divmod(100, 9)))

x, y, *rest = range(10)
x, y, *rest = 1, 2, 3, 4, 5
x, y, *rest = 1, 2

# mutable vs immutable
l = (15, 20, 25)
m = [15, 20, 25]
print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2
print(l, id(l))
print(m, id(m))

l *= 2
m = m * 2
print(l, id(l))
print(m, id(m))  # list가 memory부하가 적을듯, tuple은 계속 memory에 계속 allocation됨

# sort vs sorted
# reverse, key=len, key=str.lower, key=function..add()

# sorted = 정렬 후 새로운 객체 반환
# sort = 정렬 후 객체 직접 변경 (inplace)
f_list = ["orange", "apple", "mango", "lemon"]

print("sorted : ", sorted(f_list))
print("sorted : ", sorted(f_list, reverse=True))
print("sorted : ", sorted(f_list, key=len))
print("sorted : ", sorted(f_list, key=lambda x: x[-1]))
print("sorted : ", sorted(f_list, key=lambda x: x[-1]), reverse=True)


print(f_list)


print("sort : ", f_list.sort(), f_list)
print("sort : ", f_list.sort(reverse=True), f_list)
print("sort : ", f_list.sort(key=lambda x: x[-1], reverse=True), f_list)

print(f_list)


# list vs array : list는 융통성(다양항 자료형, 속도도 빠름), 숫자기반일때는 array
