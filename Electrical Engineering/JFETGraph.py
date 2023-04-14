from PyQt5 import QtWidgets, QtGui, QtCore
import ltspice
import numpy as np
import matplotlib.pyplot as plt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.table_view = QtWidgets.QTableView()
        self.table_model = QtGui.QStandardItemModel()
        self.table_view.setModel(self.table_model)

        self.load_button = QtWidgets.QPushButton("Load LTSpice File")
        self.load_button.clicked.connect(self.load_ltspice_file)

        central_widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.table_view)
        layout.addWidget(self.load_button)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def load_ltspice_file(self):
        filepath = "C:/LTspiceXVII/.asc"
        lts = ltspice.Ltspice(filepath, max_header_size=1048576)  # Set max_header_size to 1MB
        lts.parse()

        time = lts.get_time()
        v1 = lts.get_data("V(N001)")
        i1 = lts.get_data("I(D1)")
        v2 = lts.get_data("V(N002)")
        p1 = v1 * i1
        p2 = v2 * -i1

        data = np.vstack((time, v1, i1, v2, p1, p2)).transpose()
        headers = ["Time", "V1", "I1", "V2", "P1", "P2"]
        self.table_model.clear()
        self.table_model.setHorizontalHeaderLabels(headers)
        for row in data:
            items = [QtGui.QStandardItem(str(item)) for item in row]
            self.table_model.appendRow(items)

        plt.plot(time, v1, label="V1")
        plt.plot(time, i1, label="I1")
        plt.plot(time, v2, label="V2")
        plt.plot(time, p1, label="P1")
        plt.plot(time, p2, label="P2")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
