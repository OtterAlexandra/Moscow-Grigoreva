from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
import sys

import random


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self._init_ui()

        # figure type: 0 - circle, 1 - square, 2 - triangle
        self._figure = (None, None, None, None)  # type, size, color, position
        self._mouse_pos = (0, 0)

    def _gen_figure(self, type, position):
        return (type,
                random.randint(5, 100),
                (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                position)

    def _init_ui(self):
        self.setGeometry(100, 100, 640, 480)
        self.setWindowTitle('Супрематизм')

        self.setMouseTracking(True)

    def paintEvent(self, event):
        if self._figure[0] is None:
            return

        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(*self._figure[2]))

        if self._figure[0] == 0:
            qp.drawEllipse(self._figure[-1][0] - self._figure[1], self._figure[-1][1] - self._figure[1],
                           2 * self._figure[1], 2 * self._figure[1])
        elif self._figure[0] == 2:
            b = self._figure[1] // 2
            a = int((3 * self._figure[1] ** 2 / 4) ** 0.5)
            p1 = QPoint(self._figure[-1][0] - a, self._figure[-1][1] + b)
            p2 = QPoint(self._figure[-1][0], self._figure[-1][1] - self._figure[1])
            p3 = QPoint(self._figure[-1][0] + a, self._figure[-1][1] + b)
            qp.drawPolygon(p1, p2, p3)

        elif self._figure[0] == 1:
            qp.drawRect(self._figure[-1][0] - self._figure[1], self._figure[-1][1] - self._figure[1],
                        2 * self._figure[1], 2 * self._figure[1])
        qp.end()

    def mouseMoveEvent(self, event):
        self._mouse_pos = event.x(), event.y()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._figure = self._gen_figure(0, (event.x(), event.y()))
            self.repaint()
        if event.button() == Qt.RightButton:
            self._figure = self._gen_figure(1, (event.x(), event.y()))
            self.repaint()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self._figure = self._gen_figure(2, self._mouse_pos)
            self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    exit(app.exec())