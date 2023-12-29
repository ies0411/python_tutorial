# concurrency
# iterator, generator
# python 반복가능한 type : collections, text file, list, dict, set,tuple, unpacking, *args ... -> iterable

t = "ABCDEFG"

print(dir(t))

for x in t:
    print(x)
# 내부적으로 iter(x)함수 호출

w = iter(t)
print(dir(w))

print(next(w))
print(next(w))
print(next(w))

while True:
    try:
        print(next(w))
    except StopIteration:
        break


# 반복 확인
print(dir(t))
print(hasattr(t, "__iter__"))
from collections import abc

print(isinstance(t, abc.Iterable))


class WordSplitter(object):
    def __init__(self, text: str) -> None:
        self._idx = 0
        self._text = text.split(" ")

    def __next__(self):
        print("call __call__")
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration("stopped iteration")
        self._idx += 1
        return word

    def __repr__(self):
        return "wordsplit(%s)" % (self._text)


wi = WordSplitter("Do today what you could do tmr")
print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))

# generator pattern
# 1. comprehension list, dict, set
# 2. corotine
# 3. 작은 메모리 조각 사용


class WordSplitGenerator(opject):
    def __init__(self, text):
        self._text = text.split(" ")

    def __iter__(self):
        for word in self._text:
            yield word  # generator

    def __repr__(self):
        return "wordsplit(%s)" % (self._text)


wg = WordSplitGenerator("Do today waht yuo s")

wt = iter(wg)

print(wt, wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
