"""
This module contains the representation of the market
"""

import random
import logging
logging.root.setLevel(logging.INFO)
from uuid import uuid4

from src.models import Asset

class Market:
    """
    This class contains the attributes and methods
    to control the market. This module will decides what assets create
    and what will be the prices according demand
    """

    def __init__(self):
        from src import _world
        self.world = _world

    def create_assets_to_be_available(self):
        """
        This function needs to do three main things.
        - one is to create new assets that will be available.
        - create more assets that exists, according demand.
        - update the price of the assets that are already available.
        """
        self._create_new_assets()
        self._create_more_assets()
        self._update_assets_price()

    def _create_new_assets(self):
        """
        This function will create new assets that will be available
        """
        while random.random() < 0.5:
            asset_id = f"main-asset-{uuid4()}"
            price=round(random.uniform(0.00, 1000.00), 2)
            depreciation_rate=random.uniform(0, 0.2)
            while random.random() < 0.5:
                asset = Asset(
                    uid=f'asset-{uuid4()}',
                    asset_id=asset_id,
                    price=price,
                    depreciation_rate=depreciation_rate
                )
                self.world.add_asset(asset)
                logging.info(f'New asset created: {asset}')

    def _create_more_assets(self):
        """
        This function will create more assets based on demand
        """
        assets_stats = self.world.get_assets_stats()
        for asset_id, stats in assets_stats.items():
            demand_rate = stats['available'] / stats['total']
            if demand_rate <= 0.5:
                generation_counter = 0
                while random.random() > demand_rate:
                    asset = Asset(
                        uid=f'asset-{uuid4()}',
                        asset_id=asset_id,
                        price=stats['average_price'],
                        depreciation_rate=stats['depreciation_rate']
                    )
                    self.world.add_asset(asset)
                    generation_counter += 1
                    demand_rate = stats['available'] + generation_counter / stats['total'] + generation_counter
                    logging.info(f"Asset created: {asset} - {asset_id}")


    def _update_assets_price(self):
        """
        This method will update the price of the assets on world
        """
        assets_stats = self.world.get_assets_stats()
        for asset_id, stats in assets_stats.items():
            demand_rate = 2 * (1 - (stats['available'] / stats['total']) - 0.5)
            for asset in self.world.assets:
                if asset.asset_id == asset_id:
                    asset.set_price(stats['average_price'] * (1 + (demand_rate * stats['depreciation_rate'])))

    def make_individuals_buy_assets(self):
        """
        This method reproduce the buy behavior from individuals for all
        population available in world
        """
        for individual in self.world.individuals:
            individual.buy_assets()
        



