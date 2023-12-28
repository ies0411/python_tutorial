# hashtable 0> 적은 리소스로 많은 데이터를 효율적으로 관리
# dict -> key중복 안됨, set -> 중복 허용 안됨

# immutable dict
from types import MappingProxyType

d = {"key1": "value1"}
# read only
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))
d["key2"] = "value2"
d_frozen["key2"] = "value2"  # error


s1 = {"Apple", "Orange", "Apple", "Kiwi"}
s2 = set(["Apple", "Orange", "Apple", "Kiwi"])
s3 = {3}
s4 = set()
s5 = frozenset({"Apple", "Orange", "Apple", "Kiwi"})

s1.add("melon")
s5.add("melon")  # error : read-only

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))


# 선언 최적화 ,  bytecod -> python intepreter실행
from dis import dis

print(dis("{10}"))  # 좀더 빠름 단계가 더 적음
print(dis("set([10])"))

# comprehending set
from unicodedata import name

print({name(chr(i), "") for i in range(0, 256)})
