"""
    shallow copy, deep copy

    가변 : list,set,dict
    객체의 복사 : copy,shallow copy,deep copy
"""

# copy

# call by value, call by reference, call by share
a_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
b_list = a_list

print(id(a_list))
print(id(b_list))

b_list[2] = 100
print(a_list)
print(b_list)

b_list[3][2] = 100
print(a_list)
print(b_list)

# immutable : int,str,float,bool.unicode
# shallow copy -> 안에있는 mutable value는 복사안됨

import copy

c_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
d_list = copy.copy(c_list)

print(id(c_list))
print(id(d_list))

d_list[1] = 100
print(c_list)
print(d_list)

d_list[3].append(1000)
d_list[4][1] = 10000
print(c_list)
print(d_list)

# deep copy
e_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
f_list = copy.deepcopy(c_list)
print(id(e_list))
print(id(f_list))


f_list[3].append(1000)
f_list[4][1] = 10000
print(e_list)
print(f_list)
