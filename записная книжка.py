import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QListWidget


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Записная книжка')

        self.f_i = QLineEdit(self)
        self.f_i.setGeometry(100, 20, 125, 25)

        self.lb = QLabel(self)
        self.lb.setText("Имя")
        self.lb.move(20, 20)

        self.s_i = QLineEdit(self)
        self.s_i.setGeometry(100, 80, 125, 25)

        self.lb = QLabel(self)
        self.lb.setText("Телефон")
        self.lb.move(20, 80)

        self.btn = QPushButton('Добавить', self)
        self.btn.setGeometry(250, 50, 75, 30)
        self.btn.clicked.connect(self.toggle)

        self.lst = QListWidget(self)
        self.lst.setGeometry(20, 130, 250, 250)

    def toggle(self):
        self.lst.addItem(str(self.f_i) + ' ' + str(self.s_i))
        self.lst.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
