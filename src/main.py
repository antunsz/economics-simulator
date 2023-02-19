import matplotlib.pyplot as plt
import random
from tqdm import tqdm
import time
import logging

#add the parent directory to the path
import sys
sys.path.append('..')

from src.market import Market

def main(gui=None):
    market = Market()

    for i in tqdm(range(30)):
        market.world.reproduce_population()
        market.create_assets_to_be_available()
        market.make_individuals_buy_assets()
        market.world.next_day()
        if gui:
            gui.label_1.setText(str(market.world.get_global_time_in_days()))
            gui.label_5.setText(str(len(market.world.individuals)))
        time.sleep(1)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
    from IPython import embed; embed()    



