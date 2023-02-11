import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import matplotlib.pyplot as plt


class TransistorCurve(QtWidgets.QGraphicsItem):
    def __init__(self, x, y, transistor_type):
        super().__init__()
        self.x = x
        self.y = y
        self.transistor_type = transistor_type

    def boundingRect(self):
        return QtCore.QRectF(0, 0, 5, 25)

    def paint(self, painter, option, widget):
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setPen(QtGui.QPen(QtGui.QColor(0, 0, 0), 2))
        for i in range(1, len(self.x)):
            painter.drawLine(QtCore.QPointF(self.x[i - 1], self.y[i - 1]),
                             QtCore.QPointF(self.x[i], self.y[i]))
        painter.setPen(QtGui.QPen(QtGui.QColor(0, 0, 0), 5))
        painter.drawText(QtCore.QPointF(5, 25), self.transistor_type)


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Transistor Curves')

        # Create a central widget
        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Create a layout
        layout = QtWidgets.QVBoxLayout(self.central_widget)

        # Create a label
        label = QtWidgets.QLabel(self.central_widget)
        label.setText("Choose the type of transistor:")
        layout.addWidget(label)

        # Create a combo box
        self.combo_box = QtWidgets.QComboBox(self.central_widget)
        self.combo_box.addItem("NPN")
        self.combo_box.addItem("PNP")
        layout.addWidget(self.combo_box)

        # Create a button
        button = QtWidgets.QPushButton(self.central_widget)
        button.setText("Show curve")
        layout.addWidget(button)

        # Connect the button to a function
        button.clicked.connect(self.show_curve)

        # Create a graphics view
        self.graphics_view = QtWidgets.QGraphicsView(self.central_widget)
        layout.addWidget(self.graphics_view)

        # Show the window
        self.show()

    def show_curve(self):
        # get the transistor type and plot the curve with matplotlib
        transistor_type = self.combo_box.currentText()
        if transistor_type == "NPN":
            x = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
            y = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
        else:
            x = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
            y = [5, 4.5, 4, 3.5, 3, 2.5, 2, 1.5, 1, 0.5, 0]
        plt.plot(x, y)
        plt.show()

        # create a scene
        scene = QtWidgets.QGraphicsScene(self.graphics_view)
        self.graphics_view.setScene(scene)

        # create a transistor curve
        transistor_curve = TransistorCurve(x, y, transistor_type)

        # add the transistor curve to the scene
        scene.addItem(transistor_curve)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
