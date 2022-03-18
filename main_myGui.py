import sys
from MyGui import Ui_MainWindow
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


# Create a class MainWindow that is a QMainWindow
# inherits from QMainWindow has a title and has a central widget that is a button
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # initializes GUI
        self.setupUi(self)

        self.pushButton.clicked.connect(self.print2label_1)

        self.horizontalSlider.valueChanged.connect(self.print2label_2)

    def print2label_1(self):
        # read value from spinbox
        value = self.spinBox.value()

        # print value to textlabel
        self.label.setText(f'{value}')

    def print2label_2(self):
        value = self.horizontalSlider.value()

        self.label_2.setText(f'{value}')

    def closeEvent(self, event):
        self.close()
        app.quit()


# Start the application
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
