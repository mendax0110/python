import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("KW21_EinstiegArrays")

        self.labelEingabeArray = QLabel("Eingabe Array:", self)
        self.labelEingabeArray.setGeometry(20, 20, 100, 20)

        self.textEditEingabeArray = QTextEdit(self)
        self.textEditEingabeArray.setGeometry(20, 40, 200, 100)

        self.buttonBerechnen = QPushButton("Berechnen", self)
        self.buttonBerechnen.setGeometry(20, 160, 100, 30)
        self.buttonBerechnen.clicked.connect(self.buttonBerechnen_Click)

        self.labelAusgabeWerte = QLabel(self)
        self.labelAusgabeWerte.setGeometry(20, 200, 200, 100)

    def buttonBerechnen_Click(self):
        inputText = self.textEditEingabeArray.toPlainText()
        valueStrings = inputText.split(',')

        values = []
        for valueString in valueStrings:
            try:
                value = int(valueString)
                values.append(value)
            except ValueError:
                self.labelAusgabeWerte.setText("Ungültige Eingabe.")
                return

        if len(values) > 0:
            maximum = max(values)
            sum = 0
            for value in values:
                sum += value
            average = sum / len(values)

            self.labelAusgabeWerte.setText(f"Maximum: {maximum}\nSum: {sum}\nAverage: {average}")
        else:
            self.labelAusgabeWerte.setText("Please enter values in the array.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 240, 320)
    window.show()
    sys.exit(app.exec_())
