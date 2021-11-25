import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.ed1 = QCheckBox('edit1', self)
        self.ed1.move(20, 20)
        self.ed1.toggle()
        self.ed1.setChecked(True)
        self.ed1.stateChanged.connect(lambda: self.func(self.w1))

        self.ed2 = QCheckBox('edit2', self)
        self.ed2.move(20, 50)
        self.ed2.toggle()
        self.ed2.setChecked(True)
        self.ed2.stateChanged.connect(lambda: self.func(self.w2))

        self.ed3 = QCheckBox('edit3', self)
        self.ed3.move(20, 80)
        self.ed3.toggle()
        self.ed3.setChecked(True)
        self.ed3.stateChanged.connect(lambda: self.func(self.w3))

        self.ed4 = QCheckBox('edit4', self)
        self.ed4.move(20, 110)
        self.ed4.toggle()
        self.ed4.setChecked(True)
        self.ed4.stateChanged.connect(lambda: self.func(self.w4))

        self.w1 = QLineEdit('Поле edit1', self)
        self.w2 = QLineEdit('Поле edit2', self)
        self.w3 = QLineEdit('Поле edit3', self)
        self.w4 = QLineEdit('Поле edit4', self)

        self.w1.move(80, 20)
        self.w2.move(80, 50)
        self.w3.move(80, 80)
        self.w4.move(80, 110)

        self.w1.setEnabled(False)
        self.w2.setEnabled(False)
        self.w3.setEnabled(False)
        self.w4.setEnabled(False)

        self.setGeometry(150, 150, 300, 150)
        self.setWindowTitle('Прятки для виджетов')
        self.show()

    def func(self, window):
        if window.isHidden():
            window.show()
        else:
            window.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
