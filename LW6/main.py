import sqlite3
from PyQt5 import QtWidgets
import sys
import widgets


if __name__ == "__main__":
    database = sqlite3.connect("quiz.db")

#     cursor.execute("""
# CREATE TABLE IF NOT EXISTS quizzes(
#     name TEXT,
#     questions_amount INTEGER,
# """)
#     cursor.execute("""
# CREATE TABLE IF NOT EXISTS quizzes(
#     question TEXT,
#     answer1 TEXT,
#     answer2 TEXT,
#     answer3 TEXT,
#     answer4 TEXT,
#     correct_answer INTEGER,
# )""")

    app = QtWidgets.QApplication(sys.argv)
    playQuidWidget = widgets.PlayQuizWidget(database)
    createQuizWidget = widgets.CreateQuizWidget(database)
    menuWidget = widgets.MenuWidget(playQuidWidget, createQuizWidget)

    # menuWidget.resize(320, 240)
    menuWidget.show()
    app.exec()
    database.close()
