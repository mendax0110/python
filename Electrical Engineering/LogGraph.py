import math
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
                             QPushButton, QWidget)


class LogGraph(QMainWindow):
    def __init__(self):
        super().__init__()

        self.max = None
        self.numPoints = None
        self.min = None
        self.updateButton = None
        self.numPointsInput = None
        self.maxInput = None
        self.minInput = None
        self.initUI()

    def initUI(self):
        # Create widgets
        self.minInput = QLineEdit()
        self.maxInput = QLineEdit()
        self.numPointsInput = QLineEdit()
        self.updateButton = QPushButton("Update")
        self.updateButton.clicked.connect(self.updatePlot)

        # Set default values for inputs
        self.minInput.setText("1")
        self.maxInput.setText("10")
        self.numPointsInput.setText("100")

        # Create layout and add widgets
        inputLayout = QGridLayout()
        inputLayout.addWidget(self.minInput, 0, 0)
        inputLayout.addWidget(self.maxInput, 0, 1)
        inputLayout.addWidget(self.numPointsInput, 0, 2)
        inputLayout.addWidget(self.updateButton, 0, 3)

        mainWidget = QWidget()
        mainWidget.setLayout(inputLayout)
        self.setCentralWidget(mainWidget)

        self.setGeometry(300, 300, 800, 450)
        self.setWindowTitle("Log Graph")
        self.show()

    def updatePlot(self):
        self.min = float(self.minInput.text())
        self.max = float(self.maxInput.text())
        self.numPoints = int(self.numPointsInput.text())

        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)

        x_step = (self.max - self.min) / (self.numPoints - 1)
        for i in range(self.numPoints):
            x = self.min + i * x_step
            ln_y = math.log(x)
            log_y = math.log10(x)
            qp.drawLine(self.xToScreen(x), self.yToScreen(ln_y),
                        self.xToScreen(x + x_step), self.yToScreen(ln_y))
            qp.drawLine(self.xToScreen(x), self.yToScreen(log_y),
                        self.xToScreen(x + x_step), self.yToScreen(log_y))

    def xToScreen(self, x):
        if self.max - self.min == 0:
            return 0
        return (x - self.min) / (self.max - self.min) * self.width()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    graph = LogGraph()
    sys.exit(app.exec_())
