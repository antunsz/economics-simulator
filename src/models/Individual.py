"""
This module contains the Individual class.
"""
import random
import logging
from uuid import uuid4
from datetime import date
from .Position import Position
from .MaritalStatus import MaritalStatus
from .Age import Age
from .Race import Race
from .StudyLevel import StudyLevel
from .Asset import Asset

class Individual:
    """
    Individual class have a set of attributes and
    it's methods to take actions in the environment
    """


    def __init__(
        self,
        position: str, 
        marital_status: MaritalStatus = MaritalStatus(),
        age: Age = Age(),
        race: Race = Race(),
        study_level: StudyLevel = StudyLevel()
    ):
        from src import _world
        self.uid = f'individual-{uuid4()}'
        position = Position(position)
        self.position = position
        self.marital_status = marital_status
        self.age = age
        self.race = race
        self.study_level = study_level
        self.assets = []
        self.world = _world
        self.money = 0

    def get_uid(self) -> str:
        return self.uid

    def get_position(self) -> Position:
        return self.position

    def get_marital_status(self) -> MaritalStatus:
        return self.marital_status

    def get_age(self) -> int:
        return self.age.get_age()

    def get_race(self) -> Race:
        return self.race

    def get_study_level(self) -> StudyLevel:
        return self.study_level

    def get_assets(self) -> list:
        return self.assets

    def set_position(self, position: str):
        self.position.set_position(position)

    def set_marital_status(self, status: str):
        self.marital_status.set_status(status)

    def set_study_level(self, study_level: str):
        self.study_level.set_study_level(study_level)

    def buy_assets(self):
        available_assets_to_buy = self.world.get_available_assets()
        for asset in available_assets_to_buy:
            if self.money > 0 and self._buy_heuristic(asset):
                logging.info(f'Buy: {self.uid} bought {asset.get_uid()}')
                self.assets.append(asset)
                asset.set_available(False)
                asset.set_owner(self)

                self.money -= asset.get_price()
                if self.money <= 0:
                    break

    def _buy_heuristic(self, asset: Asset) -> bool:
        """
        This method is the heuristic to buy an asset
        """
        price = asset.get_price()
        real_value = asset.get_value() / price
        if real_value > 0.7 and self.money >= price and random.random() > 0.5:
            return True
        return False

    def __str__(self) -> str:
        return f'{self.get_uid()} - {self.get_position()} - {self.get_marital_status()} - {self.get_age()} - {self.get_race()} - {self.get_study_level()}'

    def __repr__(self) -> str:
        return self.__str__()
