import sqlite3
from PyQt5 import QtWidgets
import sys
import widgets


if __name__ == "__main__":
    database = sqlite3.connect("quiz.db")

    app = QtWidgets.QApplication(sys.argv)
    playQuidWidget = None
    createQuizWidget = None
    menuWidget = widgets.MenuWidget(database, playQuidWidget, createQuizWidget)

    menuWidget.show()
    app.exec()
    database.close()
