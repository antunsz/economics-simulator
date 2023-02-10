"""
This module contains the Individual class.
"""
from uuid import uuid4
from datetime import date
from .Position import Position
from .MaritalStatus import MaritalStatus
from .Age import Age
from .Race import Race
from .StudyLevel import StudyLevel

from src import world

class Individual:
    """
    Individual class have a set of attributes and
    it's methods to take actions in the environment
    """


    def __init__(
        self,
        position: Position,
        marital_status: MaritalStatus,
        age: Age = Age(),
        race: Race = Race(),
        study_level: StudyLevel = StudyLevel()
    ):
        self.uid = uuid4()
        self.position = position
        self.marital_status = marital_status
        self.age = age
        self.race = race
        self.study_level = study_level
        self.assets = []
        self.world = world

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

    def buy_asset(self, asset_uid: str) -> str:
        if not asset_uid in world.available_assets():
            return f'Asset not available: {asset_uid}'














