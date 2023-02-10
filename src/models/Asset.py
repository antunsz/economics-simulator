"""
This module contains the Asset class.
"""

class Asset:
    """
    Asset class have a uid and some attributes as
    price, depreciation_rate, age, and a method to
    compute the value of the asset
    """
    def __init__(
        self, uid: str,
        asset_id: str,
        price: float,
        depreciation_rate: float,
        age: int = 0
    ):
        self.uid = uid
        self.asset_id = asset_id
        self.price = price
        self.depreciation_rate = depreciation_rate
        self.age = age
        self.available = True
        self.owners = []

    def get_value(self) -> float:
        return self.price * (1 - self.depreciation_rate) ** self.age

    def get_uid(self) -> str:
        return self.uid

    def get_age(self) -> int:
        return self.age

    def get_price(self) -> float:
        return self.price

    def get_depreciation_rate(self) -> float:
        return self.depreciation_rate

    def get_available(self) -> bool:
        return self.available

    def get_owners(self) -> list:
        return self.owners

    def set_available(self, available: bool):
        self.available = available

    def set_age(self, age: int):
        self.age = age

    def set_price(self, price: float):
        self.price = price

    def set_depreciation_rate(self, depreciation_rate: float):
        self.depreciation_rate = depreciation_rate

    def __str__(self) -> str:
        return f'{self.uid} - {self.asset_id} - {self.price} - {self.depreciation_rate} - {self.age}'

