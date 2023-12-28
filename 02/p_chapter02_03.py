class Car(object):
    """
    car class
    author : Lim
    Data: .
    Description : Class, Static, Instance Method
    """

    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company  # instance variable
        self._details = details

    # 사용자용
    def __str__(self):
        return f"str : {self._company}, {self._details}"

    # 개발자용
    def __repr__(self):
        return f"repr : {self._company}, {self._details}"

    # instance method, unique value
    def detail_info(self):
        print(f"id : {id(self)}")
        print(f'car info : {self._details.get("color")}')

    # instance method
    def get_price(self):
        # pass
        return f'before : {self._details.get("price")}'

    def get_price_culc(self):
        return f'after : {self._details.get("price")*Car.price_per_raise}'

    @classmethod
    def raise_price(cls, per):
        cls.price_per_raise = per

    # static method vs class method ??, 필요성에 약간 논쟁이있음
    @staticmethod
    def is_bmw(instance):
        if instance._company == "bmw":
            return "ok"
        return "nop"


car1 = Car("fer", {"color": "white", "price": 1000})
car2 = Car("bmw", {"color": "white", "price": 2000})

print(car1._details.get("price"))  # 좋지않음 -> private으로 함 다른 언어에서
print(car1._details["price"])

# 위의 직접 접근보다 바람직
print(car1.get_price())
Car.price_per_raise = 1.4  # 바람직하지 않음
print(car1.get_price_culc)

# 위의 직접 접근보다 바람직
print(car1.get_price())
Car.raise_price(1.6)
print(car1.get_price_culc)

# static method
print(car1.is_bmw(car1))
print(Car.is_bmw(car1))
