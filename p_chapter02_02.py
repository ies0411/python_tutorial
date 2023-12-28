class Car(object):
    """
    car class
    author : Lim
    Data: .
    """

    car_count = 0  # class variable -> 모든 인스턴스(객체)가 공유

    def __init__(self, company, details):
        self._company = company  # instance variable
        self._details = details
        Car.car_count += 1

    # 사용자용
    def __str__(self):
        return f"str : {self._company}, {self._details}"

    # 개발자용
    def __repr__(self):
        return f"repr : {self._company}, {self._details}"

    def detail_info(self):
        print(f"id : {id(self)}")
        print(f'car info : {self._details.get("color")}')

    def __del__(self):
        Car.car_count -= 1


car1 = Car("fer", {"color": "white"})
car2 = Car("bmw", {"color": "white"})
car3 = Car("audi", {"color": "white"})


# ID -> 각각다름 고유 -> self : c++의 this (객체)
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)  # false 값을비교
print(car1 is car2)  # false (id를 비교)

print(dir(car1))  # 모든 magic method
print(car1.__dict__)  # 객체 내부 value
print(car1.__doc__)  # docs

car1.detail_info()
car2.detail_info()

print(car1.__class__, car2.__class__)
print(id(car1.__class__, id(car2.__class__)))  # class의 id는 같음

# class variable, instance variable

Car.detail_info()  # 불가능
Car.detail_info(car2)  # 가능


# class variable
print(car1.car_count)
print(car2.car_count)
print(car1.__dict__)
print(car2.__dict__)
print(dir(car1))

print(car1.car_count)
print(Car.car_count)

del car2
print(Car.car_count)

# instance variable먼저검색후 -> class variable 검색함 ; 같으면 overriding
