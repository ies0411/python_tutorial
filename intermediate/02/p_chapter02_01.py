# OOP -> 코드 재용, 코드 중복 방지, 유지보수
# 규모가 큰 프로젝트 -> 함수 중심 -> 코드 중복, 복잡
# 클래스 중심 -> 객체로 관리

# 기존
car_company_1 = "Ferrari"
car_detail_1 = [{"color": "white"}]

car_company_2 = "bmw"
car_detail_2 = [{"color": "black"}]

car_company_3 = "audi"
car_detail_3 = [{"color": "blue"}]

# list -> 데이터 삭제 불편
car_company_list = ["ferrari", "bmw", "audi"]
car_detail_list = [{"color": "white"}, {"color": "black"}]

del car_company_list[1]
del car_detail_list[1]
# dictio nary structure

car_dicts = [
    {"car_company": "Ferrari", "car_detail": {"color": "white"}},
    {"car_company": "bmw", "car_detail": {"color": "black"}},
    {"car_company": "audi", "car_detail": {"color": "blue"}},
]

# pop(key, "default")
del car_dicts[1]


class Car:
    def __init__(self, company, details):
        self._company = company
        self._details = details

    # 사용자용
    def __str__(self):
        return f"str : {self._company}, {self._details}"

    # 개발자용
    def __repr__(self):
        return f"repr : {self._company}, {self._details}"


car1 = Car("fer", {"color": "white"})

print(car1)
print(car1.__dict__)

car_list = []
car_list.append(car1)

for x in car_list:
    print(repr(x))
