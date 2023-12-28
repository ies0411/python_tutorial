# hash table
# key에 value를 저장하는 구조, python은 강력한 hashtable 구조
# python dict은 hash table의 예
# 키값의 연산 결과에 따라 직접 접근이 가능함
# key값을 해싱 함수 -> 해쉬 주소 -> key에 대한 value 참조

# dict structure
print(__builtins__.__dict__)

# hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))
print(hash(t2))  # error : cuz list is mutable

source = (("k1", "val1"), ("k1", "val2"), ("k2", "val3"), ("k2", "val4"))

new_dict1 = {}
new_dict2 = {}

for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)

# use setdefault

for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)
