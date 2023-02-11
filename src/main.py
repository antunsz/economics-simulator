import matplotlib.pyplot as plt
import random
from tqdm import tqdm
import time
import logging

#add the parent directory to the path
import sys
sys.path.append('..')

from src.market import Market

market = Market()

for i in tqdm(range(30)):
    # logging.info(f'world time: {market.world.get_global_time_in_days()}')
    market.world.reproduce_population()
    market.create_assets_to_be_available()
    market.make_individuals_buy_assets()
    # last_asset = market.world.assets[-1].age if market.world.assets else []
    # logging.info(f'last asset created: {last_asset}')
    market.world.next_day()
    time.sleep(1)

from IPython import embed; embed()    



