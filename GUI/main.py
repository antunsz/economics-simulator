"""
This module contains the GUI for the economic simulator, developed with PyQt6.
"""
import sys

sys.path.append('..')

from PyQt6 import uic, QtWidgets 
from PyQt6.QtCore import QObject, QThread, pyqtSignal
from GUI.controller.main_controller import start_simulation
from src import _world

class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)

class Worker(QObject):
    """
    This class is used to run the simulation
    in a different thread
    """

    def __init__(self, main_window):
        super().__init__()
        self.signals = WorkerSignals()
        self.main_window = main_window
        self.fn = None

    def run(self):
        """
        This function runs the simulation
        """
        try:
            self.fn(gui=self.main_window)
        except Exception as e:
            self.signals.error.emit((type(e), e, None))
        else:
            self.signals.result.emit(None)
        finally:
            self.signals.finished.emit()

app = QtWidgets.QApplication(sys.argv)

# Load the UI file
main_window = uic.loadUi("./view/UI.ui")

thread = QThread()
worker = Worker(main_window)
# Connect the button to the function
main_window.pushButton.clicked.connect(
    lambda x: start_simulation(thread, worker)
)

# Show the main window
main_window.show()
app.exec()
