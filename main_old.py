import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


# Create a class MainWindow that is a QMainWindow
# inherits from QMainWindow has a title and has a central widget that is a button
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.button = QPushButton("Button!")

        # Set the central widget of the Window.
        self.setCentralWidget(self.button)

        self.number = 0
        self.button.clicked.connect(self.count_up)

    def count_up(self):
        """Count up the stored number"""
        self.number += 1
        print(f'New number: {self.number}')

    def closeEvent(self, event):
        self.close()
        app.quit()

# Start the application
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
