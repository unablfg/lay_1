import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.uic import loadUi
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("UI.ui", self)
        self.setWindowTitle("Random Circles")
        self.button.clicked.connect(self.draw_circle)

    def draw_circle(self):
        diameter = random.randint(10, 100)
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))
        painter.drawEllipse(random.randint(0, self.width() - diameter), 
                            random.randint(0, self.height() - diameter), 
                            diameter, diameter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
