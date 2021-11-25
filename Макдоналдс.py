import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QPlainTextEdit, QPushButton
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.f1 = QCheckBox('Чисбургер', self)
        self.f1.move(20, 20)
        self.f1.toggle()
        self.f1.stateChanged.connect(self.changeTitle)
        self.f1.setChecked(False)

        self.f2 = QCheckBox('Гамбургер', self)
        self.f2.move(20, 50)
        self.f2.toggle()
        self.f2.stateChanged.connect(self.changeTitle)
        self.f2.setChecked(False)

        self.f3 = QCheckBox('Кока-кола', self)
        self.f3.move(20, 80)
        self.f3.toggle()
        self.f3.stateChanged.connect(self.changeTitle)
        self.f3.setChecked(False)

        self.f4 = QCheckBox('Нагетсы', self)
        self.f4.move(20, 110)
        self.f4.toggle()
        self.f4.stateChanged.connect(self.changeTitle)
        self.f4.setChecked(False)

        self.buy = QPushButton('Заказать', self)
        self.buy.clicked.connect(self.click)
        self.buy.setGeometry(20, 150, 120, 30)

        self.showing = QPlainTextEdit(self)
        self.showing.setGeometry(20, 200, 300, 200)
        self.showing.setEnabled(False)

        self.setGeometry(300, 300, 420, 420)
        self.setWindowTitle('Заказ в Макдональдсе')
        self.show()

    def changeTitle(self, state):

        if state == Qt.Checked:
            self.setWindowTitle('Заказ в Макдональдсе')
        else:
            self.setWindowTitle('Заказ в Макдональдсе')

    def click(self):
        self.showing.setPlainText('Ваш заказ:' + '\n' + '')
        if self.f1.isChecked():
            self.showing.setPlainText(self.showing.toPlainText() + '\n' + self.f1.text())
        if self.f2.isChecked():
            self.showing.setPlainText(self.showing.toPlainText() + '\n' + self.f2.text())
        if self.f3.isChecked():
            self.showing.setPlainText(self.showing.toPlainText() + '\n' + self.f3.text())
        if self.f4.isChecked():
            self.showing.setPlainText(self.showing.toPlainText() + '\n' + self.f4.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
