import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("db.ui", self)
        self.con = sqlite3.connect("films_db.sqlite")
        self.show_btn.clicked.connect(self.update_result)
        self.change_btn.clicked.connect(self.change_item)
        self.titles = None

    def update_result(self):
        try:
            cur = self.con.cursor()
            query = "SELECT * FROM films WHERE " + self.query_edit.toPlainText()
            result = cur.execute(query).fetchall()
            self.tableWidget.setRowCount(len(result))
            if not result:
                self.statusBar().showMessage('Ничего не нашлось')
                return
            self.tableWidget.setColumnCount(len(result[0]))
            self.titles = [description[0] for description in cur.description]
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        except Exception as e:
            print(e)

    def change_item(self):
        try:
            rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
            selected_item = self.tableWidget.selectedItems()[0]
            srd = [self.tableWidget.item(selected_item.row(), i).text() for i in range(len(self.titles))]
            valid = QMessageBox.question(
                self, '', "Действительно изменить элемент с id " + srd[0],
                QMessageBox.Yes, QMessageBox.No)
            if valid == QMessageBox.Yes:
                cur = self.con.cursor()
                query = f"UPDATE films SET title = '{srd[1][::-1]}', " \
                        f"year = {int(srd[2]) + 1000}, duration = duration * 2 " \
                        f"WHERE id = {srd[0]}"
                cur.execute(query)
                self.con.commit()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
