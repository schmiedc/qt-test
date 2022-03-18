import sys
import numpy as np
# This imports the previously generated UI file
from matplotlibwidget import Ui_MainWindow

from PyQt5.QtWidgets import QApplication, QMainWindow


# Define the the main window class
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # Initialize GUI
        self.setupUi(self)
        self.display_image()

    def plot_curve(self):
        # Plot a curve:
        x = np.linspace(0, np.pi, 100)

        # Read value from SpinBox
        value = 2

        y = value * np.sin(x)

        self.plotWidget.canvas.axes.clear()
        self.plotWidget.canvas.axes.plot(x, y, color='red')
        self.plotWidget.canvas.draw()

    def display_image(self):
        # Display an image:
        image = np.random.randint(0, 10, 100).reshape(10, -1)
        self.plotWidget.canvas.axes.clear()
        self.plotWidget.canvas.axes.imshow(image, cmap='gray')
        self.plotWidget.canvas.draw()

    def closeEvent(self, event):
        self.close()
        app.quit()


# Start the application
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
