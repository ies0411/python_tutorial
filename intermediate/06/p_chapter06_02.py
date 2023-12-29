# concurrency : 한 cpu가 여러일을 동시에
# parallelism : 여로 cpu가 여러일을 동시에


# generator ex1
def generator_ex1():
    print("start")
    yield "A Point"  # 네이버에서 크롤링
    print("continue")
    yield "B Point"
    print("end")


temp = iter(generator_ex1)
print(temp)
print(next(temp))
print(next(temp))
print(next(temp))


for v in generator_ex1():
    print(v)

temp2 = [x * 3 for x in generator_ex1()]  # list
temp3 = (x * 3 for x in generator_ex1())  # generator
print(temp2)
print(temp3)
for i in temp3:
    print(i)

# generator ex3 : filterfalse, accumulate, chain, product, groupby

import itertools

gen1 = itertools.count(1, 2.5)

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))  # .. infinite

gen2 = itertools.takewhile(lambda n: n < 1000, itertools.count(1, 2.5))
for v in gen2:
    print(v)

# filter 반대
gen3 = itertools.filterfalse(lambda n: n < 3, [1, 2, 3, 4, 5])
for v in gen3:
    print(v)

gen4 = itertools.accumulate([x for x in range(1, 101)])

for v in gen4:
    print(v)

gen5 = itertools.chain("ABCDE", range(1, 11, 2))

print(list(gen5))

gen6 = itertools.chain(enumerate("ABCDE"))
print(list(gen6))

gen7 = itertools.product("ABCDE")
print(list(gen7))

gen8 = itertools.product("ABCDE", repeat=3)
print(list(gen8))

gen9 = itertools.groupby("AAABBBCCCDDEEEE")
for a, group in gen9:
    print(a, ":", list(group))
