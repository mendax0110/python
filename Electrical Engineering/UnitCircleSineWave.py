import math

from PyQt5.QtCore import QRectF
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPainter, QPen, QColor, QPainterPath
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsItem, QMainWindow, QVBoxLayout, \
    QHBoxLayout, QWidget, QLabel, QSlider, QGraphicsPathItem


class PointerItem(QGraphicsItem):
    def __init__(self, angle=0):
        super().__init__()
        self.angle = angle

    def boundingRect(self):
        return QRectF(-1, -1, 2, 2)

    def paint(self, painter, option, widget=None):
        painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen(QColor(0, 0, 0))
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawLine(QPointF(0, 0), QPointF(math.cos(self.angle), math.sin(self.angle)))


class UnitCircleView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)
        self.setRenderHint(QPainter.HighQualityAntialiasing)
        self.setRenderHint(QPainter.TextAntialiasing)

        self.setScene(QGraphicsScene(self))
        self.setSceneRect(-1, -1, 2, 2)

        self.pointer_item = PointerItem()
        self.pointer_item.setPos(0, 0)
        self.scene().addItem(self.pointer_item)

        self.sine_wave_item = QGraphicsPathItem()
        self.scene().addItem(self.sine_wave_item)

        self.setMinimumSize(200, 200)

    def update_sine_wave(self):
        path = QPainterPath()
        num_points = 100
        for i in range(num_points):
            x = -1 + i * 2 / num_points
            y = math.sin(x)
            if i == 0:
                path.moveTo(x, y)
            else:
                path.lineTo(x, y)
        self.sine_wave_item.setPath(path)

    def resizeEvent(self, event):
        self.fitInView(self.sceneRect(), Qt.KeepAspectRatio)

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self.viewport())
        pen = QPen(QColor(0, 0, 0))
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawLine(QPointF(-1, 0), QPointF(1, 0))  # Draw the x-axis
        painter.drawLine(QPointF(0, -1), QPointF(0, 1))  # Draw the y-axis


class SineGraphView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)
        self.setRenderHint(QPainter.HighQualityAntialiasing)
        self.setRenderHint(QPainter.TextAntialiasing)

        self.setScene(QGraphicsScene(self))
        self.setSceneRect(-1, -1.2, 2, 2.4)
        self.setMinimumSize(200, 200)

        self.pointer_item = PointerItem()
        self.pointer_item.setPos(0, 0)
        self.scene().addItem(self.pointer_item)

    def resizeEvent(self, event):
        self.fitInView(self.sceneRect(), Qt.KeepAspectRatio)

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self.viewport())
        pen = QPen(QColor(0, 0, 0))
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawLine(QPointF(-1, 0), QPointF(1, 0))
        painter.drawLine(QPointF(0, -1), QPointF(0, 1))


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.unit_circle_view = UnitCircleView()
        self.sine_graph_view = SineGraphView()
        self.angle_slider = QSlider(Qt.Horizontal)
        self.angle_slider.setRange(0, 360)
        self.angle_slider.setSingleStep(1)
        self.angle_slider.setTickInterval(10)
        self.angle_slider.setTickPosition(QSlider.TicksBelow)
        self.angle_slider.valueChanged.connect(self.on_angle_slider_value_changed)
        self.angle_label = QLabel("Angle: 0")
        self.angle_label.setAlignment(Qt.AlignCenter)
        self.angle_label.setMinimumWidth(100)
        self.angle_label.setMaximumWidth(100)
        self.angle_label.setMinimumHeight(30)
        self.angle_label.setMaximumHeight(30)

        self.main_widget = QWidget()
        self.main_layout = QHBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

        self.left_layout = QVBoxLayout()
        self.main_layout.addLayout(self.left_layout)
        self.left_layout.addWidget(self.unit_circle_view)
        self.left_layout.addWidget(self.angle_slider)
        self.left_layout.addWidget(self.angle_label)

        self.right_layout = QVBoxLayout()
        self.main_layout.addLayout(self.right_layout)
        self.right_layout.addWidget(self.sine_graph_view)
        self.angle_slider.valueChanged.connect(self.update_angle)

    def update_angle(self, value):
        self.unit_circle_view.pointer_item.angle = math.radians(value)
        self.sine_graph_view.pointer_item.angle = math.radians(value)
        self.unit_circle_view.update()
        self.unit_circle_view.update_sine_wave()
        self.sine_graph_view.update()

    def on_angle_slider_value_changed(self, value):
        angle = math.radians(value)
        self.unit_circle_view.pointer_item.angle = angle
        self.unit_circle_view.pointer_item.update()
        self.angle_label.setText("Angle: {}".format(value))

    def timerEvent(self, event):
        self.pointer_angle += self.pointer_angle_delta
        self.pointer_item.angle = self.pointer_angle
        self.unit_circle_view.update()
        self.update_pointer()


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
