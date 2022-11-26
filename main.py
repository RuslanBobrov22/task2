import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        con = sqlite3.connect('coffee.sqlite')

        cur = con.cursor()

        result = cur.execute("""SELECT * FROM coffe_data
        """).fetchall()
        con.close()
        for elem in result:
            res = ''
            for i in elem:
                res += str(i) + ' '
            self.listWidget.addItem(res[:-1])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())