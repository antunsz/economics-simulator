"""
This module conatins the World class. That will represent the space-time
"""
import datetime

class World:
    """
    This class contains the attributes and methods
    to constrol the time, space and the environment
    for the agents inside it
    """

    def __init__(self, time: datetime.date = datetime.date.today()):
        self.time = time
        self.assets = []

    def add_asset(self, asset):
        self.assets.append(asset)

    def get_global_time(self) -> datetime.date:
        return self.time

    def get_available_assets(self) -> list:
        return [asset.uid for asset in self.assets if asset.available]


