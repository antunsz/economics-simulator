"""
This module contains the main controller 
for the economic simulator GUI
"""

from src.main import main


def start_simulation(thread, worker):
    """
    This function starts the thread of the simulation
    """
    worker.fn = main
    worker.moveToThread(thread)
    thread.started.connect(worker.run)
    thread.start()
