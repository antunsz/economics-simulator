"""
This module contains the representation of the market
"""

import random
import logging
from uuid import uuid4

from src import world
from src.models import Asset

class Market:
    """
    This class contains the attributes and methods
    to control the market. This module will decides what assets create
    and what will be the prices according demand
    """

    def __init__(self):
        self.world = world

    def create_assets_to_be_available(self):
        """
        This function needs to do three main things.
        - one is to create new assets that will be available.
        - create more assets that exists, according demand.
        - update the price of the assets that are already available.
        """
        self.create_new_assets()
        self.create_more_assets()
        self.update_assets_price()

    def create_new_assets(self):
        """
        This function will create new assets that will be available
        """
        while random.random() < 0.5:
            asset_id = f"main-asset-{uuid4()}"
            price=round(random.uniform(0.00, 1000.00), 2)
            depreciation_rate=random.random()
            while random.random() < 0.5:
                asset = Asset(
                    uid=f'asset-{uuid4()}',
                    asset_id=asset_id,
                    price=price,
                    depreciation_rate=depreciation_rate
                )
                self.world.add_asset(asset)
                logging.info(f'New asset created: {asset}')

    def create_more_assets(self):
        """
        This function will create more assets based on demand
        """
        pass

    def update_assets_price(self):
        """
        This method will update the price of the assets on world
        """
        pass



