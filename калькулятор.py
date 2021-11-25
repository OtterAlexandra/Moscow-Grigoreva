from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber
from PyQt5 import uic

import sys
from math import factorial, sqrt


class Window(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)

        self._first_number = list()
        self._second_number = list()
        self._op = None

        self.btn0.clicked.connect(self.btn_clicked)  # 1
        self.btn1.clicked.connect(self.btn_clicked)  # 2
        self.btn2.clicked.connect(self.btn_clicked)  # 3
        self.btn3.clicked.connect(self.btn_clicked)  # 4
        self.btn4.clicked.connect(self.btn_clicked)  # 5
        self.btn5.clicked.connect(self.btn_clicked)  # 6
        self.btn6.clicked.connect(self.btn_clicked)  # 7
        self.btn7.clicked.connect(self.btn_clicked)  # 8
        self.btn8.clicked.connect(self.btn_clicked)  # 9
        self.btn9.clicked.connect(self.btn_clicked)  # 10

        self.btn_fact.clicked.connect(self.unary_clicked)
        self.btn_sqrt.clicked.connect(self.unary_clicked)

        self.btn_clear.clicked.connect(self.clean)

        self.btn_plus.clicked.connect(self.twice_clicked())  # +
        self.btn_minus.clicked.connect(self.twice_clicked())  # -
        self.btn_mult.clicked.connect(self.twice_clicked())  # *
        self.btn_div.clicked.connect(self.twice_clicked())  # /
        self.btn_pow.clicked.connect(self.unary_clicked())  # .

        self.btn_dot.clicked.connect(self.clean)  # .
        self.btn_eq.clicked.connect(self.clean)  # =

    def btn_clicked(self):
        if self._op is None:
            self._first_number.append(self.sender().text())
            self.table.display(''.join(self._first_number))

        else:
            self._second_number.append(self.sender().taxt())
            self.table.display(''.join(self._second_number))

    def _to_number(self, lst):
        return float(''.join(lst))

    def _to_lst(self, number):
        return list(str(number))

    def unary_clicked(self):
        if self.sender().text() == '!':
            result = factorial(int(self._to_number(self._first_number)))
            self._first_number = self._to_lst(result)
        self.table.display(''.join(self._first_number))

        if self.sender().text() == '√':
            result = sqrt(self._to_number(self._first_number))
            self._first_number = self._to_lst(result)
        self.table.display(''.join(self._first_number))

    def twice_clicked(self):
        self._op = self.sender().text()

    def eq(self):
        if self._op == '+':
            pass

    def clean(self):
        self._first_number = []
        self.table.display('')


app = QApplication(sys.argv)

window = Window()
window.show()

exit(app.exec())
# записать в архив
