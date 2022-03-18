from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

import numpy as np


class MplCanvas(FigureCanvas):
    """
    Defines the canvas of the matplotlib window
    """

    def __init__(self):
        self.fig = Figure()  # create a figure
        self.axes = self.fig.add_subplot(111)  # create subplot

        FigureCanvas.__init__(self, self.fig)  # initialize canvas
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


class matplotlibWidget(QWidget):
    """
    The matplotlibWidget class based on QWidget
    """
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        # save canvas and toolbar
        self.canvas = MplCanvas()
        self.toolbar = NavigationToolbar(self.canvas, self)
        # set layout and add them to widget
        self.vbl = QVBoxLayout()
        self.vbl.addWidget(self.toolbar)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
