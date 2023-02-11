"""
This module contains the Asset class.
"""
import logging

from src.models import Individual

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
        age: int = 0,
    ):
        from src import _world
        self.uid = uid
        self.asset_id = asset_id
        self.price = [price]
        self.depreciation_rate = depreciation_rate
        self.age = _world.get_global_time_in_days() if age == 0 else age
        self.available = True
        self.world = _world
        self.owners = []

    def get_value(self) -> float:
        return self.get_price() * (1 - self.depreciation_rate) ** self.get_age()

    def get_uid(self) -> str:
        return self.uid

    def get_asset_id(self) -> str:
        return self.asset_id

    def get_age(self) -> int:
        return self.world.get_global_time_in_days() - self.age

    def get_price(self) -> float:
        return self.price[-1]

    def get_depreciation_rate(self) -> float:
        return self.depreciation_rate

    def get_available(self) -> bool:
        return self.available

    def get_owner(self) -> Individual:
        return self.owners[-1]

    def get_owners(self) -> list:
        return self.owners

    def set_available(self, available: bool):
        self.available = available

    def set_age(self, age: int):
        self.age = age

    def set_price(self, price: float):
        self.price.append(price)

    def set_depreciation_rate(self, depreciation_rate: float):
        self.depreciation_rate = depreciation_rate

    def set_owner(self, owner: Individual):
        self.owners.append(owner)

    def __str__(self) -> str:
        return f'{self.get_uid()} - {self.get_asset_id()} - {self.get_price()} - {self.get_depreciation_rate()} - {self.get_age()}'

