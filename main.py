import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QPainter, QColor
import random


class CircleDrawer(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 300)
        self.setWindowTitle("Random Circles")
        self.button = QPushButton('Draw Circle', self)
        self.button.clicked.connect(self.draw_circle)
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def draw_circle(self):
        diameter = random.randint(10, 100)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        painter = QPainter(self)
        painter.setBrush(color)
        painter.drawEllipse(random.randint(0, self.width() - diameter), 
                            random.randint(0, self.height() - diameter), 
                            diameter, diameter)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = CircleDrawer()
        self.setCentralWidget(self.central_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
