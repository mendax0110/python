from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.and1Clicked = False
        self.and2Clicked = False
        self.or1Clicked = False
        self.or2Clicked = False

        self.setGeometry(100, 100, 700, 400)
        self.setWindowTitle("Logic Gates")

        # AND gate
        self.andButton1 = QPushButton("InputAND 1", self)
        self.andButton1.setGeometry(100, 150, 100, 50)
        self.andButton1.clicked.connect(self.andButton1Clicked)

        self.andButton2 = QPushButton("InputAND 2", self)
        self.andButton2.setGeometry(100, 250, 100, 50)
        self.andButton2.clicked.connect(self.andButton2Clicked)

        self.andOutput = QPushButton("OutputAND", self)
        self.andOutput.setGeometry(250, 200, 100, 50)
        self.andOutput.setStyleSheet("background-color: gray;")
        self.andOutput.setEnabled(False)

        # OR gate
        self.orButton1 = QPushButton("InputOR 1", self)
        self.orButton1.setGeometry(400, 150, 100, 50)
        self.orButton1.clicked.connect(self.orButton1Clicked)

        self.orButton2 = QPushButton("InputOR 2", self)
        self.orButton2.setGeometry(400, 250, 100, 50)
        self.orButton2.clicked.connect(self.orButton2Clicked)

        self.orOutput = QPushButton("OutputOR", self)
        self.orOutput.setGeometry(550, 200, 100, 50)
        self.orOutput.setStyleSheet("background-color: gray;")
        self.orOutput.setEnabled(False)

    def andButton1Clicked(self):
        self.and1Clicked = not self.and1Clicked
        self.andButton1.setStyleSheet("background-color: green;" if self.and1Clicked else "background-color: red;")
        self.andOutput.setStyleSheet(
            "background-color: green;" if (self.and1Clicked and self.and2Clicked) else "background-color: gray;")
        self.andOutput.setEnabled(self.and1Clicked or self.and2Clicked)

    def andButton2Clicked(self):
        self.and2Clicked = not self.and2Clicked
        self.andButton2.setStyleSheet("background-color: green;" if self.and2Clicked else "background-color: red;")
        self.andOutput.setStyleSheet(
            "background-color: green;" if (self.and1Clicked and self.and2Clicked) else "background-color: gray;")
        self.andOutput.setEnabled(self.and1Clicked or self.and2Clicked)

    def orButton1Clicked(self):
        self.or1Clicked = not self.or1Clicked
        self.orButton1.setStyleSheet("background-color: green;" if self.or1Clicked else "background-color: red;")
        self.orOutput.setStyleSheet(
            "background-color: green;" if (self.or1Clicked or self.or2Clicked) else "background-color: gray;")
        self.orOutput.setEnabled(self.or1Clicked or self.or2Clicked)

    def orButton2Clicked(self):
        self.or2Clicked = not self.or2Clicked
        self.orButton2.setStyleSheet("background-color: green;" if self.or2Clicked else "background-color: red;")
        self.orOutput.setStyleSheet(
            "background-color: green;" if (self.or1Clicked or self.or2Clicked) else "background-color: gray;")
        self.orOutput.setEnabled(self.or1Clicked or self.or2Clicked)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
