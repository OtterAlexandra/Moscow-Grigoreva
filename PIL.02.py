import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QWidget, QApplication
from PyQt5 import uic

from PIL import Image
from PIL.ImageQt import I


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('PILL.ui', self)

        file_name = QFileDialog.getOpenFileName(self, '', '')[0]
        self.pil_image = Image.open(file_name)
        self._current_angle = 0
        self._current_image = None

        self.show_imange(self.pil_image)

        self.r_btn.clicked.connect(self.r_btn)
        self.ccw_btn.clicked.connect(self.ccw_btn)

    def show_imange(self, img):
        img = img.convert('RGBA')
        data = img.tobytes('raw', 'RGBA')
        qt_img = QImage(data, img.size[0], img.size[1], QImage.Format_RGBA8888)
        self.image.setPixmap(QPixmap.fromImage(qt_img))
        self._current_image = img

    def r_clicked(self):
        pi_copy = self.pil_image.copy().rotate(self._current_angle)
        pi_pixels = pi_copy.load()
        pi_size = pi_copy.size
        for i in range(pi_size[0]):
            for j in range(pi_size[1]):
                pi_pixels[i, j] = pi_pixels[i, j][0], 0, 0
        self.show_image(pi_copy)

    def ccw_clicked(self):
        self._current_angle += 90
        self.show_image(self._current_angle.rotate(90))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawStar()
    ex.show()
    sys.exit(app.exec())
