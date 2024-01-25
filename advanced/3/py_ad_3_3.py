"""
    meta: meta class
    type inheritance, custom metaclass

    1. type class상속
    2. meta class속성 사용
    3. 커스텀 메타 클래스 생성
"""
# custom metaclass (type상속x)


def cus_mul(self, d):
    for i in range(len(self)):
        self[i] = self[i] * d


def cus_replace(self, old, new):
    while old in self:
        self[self.index(old)] = new


# list상속받는 메소드 2개 추가
CustomList1 = type(
    "CustomList1",
    (list,),
    {"desc": "커스텀 리스트1", "cus_mul": cus_mul, "cus_replace": cus_replace},
)
c1 = CustomList1([1, 2, 3, 4, 5, 6, 7, 8, 9])
c1.cus_mul(1000)
c1.cus_replace(1000, 777)


# class MetaClassName(type):
#     def __new__(metacls,name,based,namesapce):
#         pass
class CustomListMeta(type):  # new -> init->call 순서
    def __init__(self, object_or_name, bases, dict):  # 생성된 인스턴스 초기화
        print("__ini__", self, object_or_name, bases, dict)
        super().__init__(object_or_name, bases, dict)

    def __call__(self, *args, **kwargs):  # 인스턴스 실행
        print(self, *args, **kwargs)
        super().__call__(*args, **kwargs)

    def __new__(metacls, name, bases, namespace):  # 클래스 인스턴스 생성(메모리 초기화)
        print("__ini__", metacls, name, bases, namespace)
        namespace["desc"] = "커스텀 리스트2"
        namespace["cus_mul"] = cus_mul
        namespace["cus_replace"] = cus_replace
        return type.__new__(metacls, name, bases, namespace)


CustomList2 = CustomListMeta("CustomList2", (list,), {})
c2 = CustomList2([1, 2, 3, 4, 5, 6, 7, 8, 9])
c2.cus_mul(1000)
c2.cus_replace(1000, 777)
