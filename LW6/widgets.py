from PyQt5 import QtWidgets, QtGui, QtCore


class MenuWidget(QtWidgets.QWidget):
    def __init__(self, database, playQuizWidget, createQuizWidget, parent=None):
        super().__init__(parent)
        self.playQuizWidget = playQuizWidget
        self.createQuizWidget = createQuizWidget

        self.setWindowTitle("Quiz Game")
        self.initGui()
        self.show()

    def initGui(self):
        playQuizPushButton = QtWidgets.QPushButton("Играть в викторину")
        playQuizPushButton.setDefault(True)
        createQuizPushButton = QtWidgets.QPushButton("Создать викторину")
        createQuizPushButton.setDefault(True)

        def processPlayQuizPushButton():
            self.playQuizWidget = PlayQuizWidget(database)

        def processCreateQuizPushButton():
            self.createQuizWidget = CreateQuizWidget(database)

        playQuizPushButton.clicked.connect(processPlayQuizPushButton)
        createQuizPushButton.clicked.connect(processCreateQuizPushButton)
        menuLayout = QtWidgets.QVBoxLayout()
        menuLayout.addWidget(playQuizPushButton)
        menuLayout.addWidget(createQuizPushButton)
        self.setLayout(menuLayout)


class PlayQuizWidget(QtWidgets.QWidget):
    def __init__(self, database, parent=None):
        super().__init__(parent)
        self.database = database

        self.setWindowTitle("Викторина")
        self.initGui()
        self.show()

    def initGui(self):
        pass


class CreateQuizWidget(QtWidgets.QWidget):
    def __init__(self, database, parent=None):
        super().__init__(parent)
        self.database = database
        self.questionsAmount = 0

        self.setWindowTitle("Создание викторины")
        self.initGui()
        self.show()

    def initGui(self):
        self.questionsAmount = 0

        def getDefaultQuizName():
            cursor = self.database.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Quiz';")
            result = cursor.fetchone()
            if result is None:
                return "Quiz"

            i = 1
            while True:
                cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='Quiz{i}';")
                result = cursor.fetchone()
                if result is None:
                    return f"Quiz{i}"

                i += 1

        quizNameLabel = QtWidgets.QLabel("Название викторины:")
        quizNameLineEdit = QtWidgets.QLineEdit()
        quizNameLineEdit.setPlaceholderText(getDefaultQuizName())
        quizNameLineEdit.setValidator(QtGui.QRegularExpressionValidator(QtCore.QRegularExpression(r"^[a-zA-Z0-9 -]+")))

        questionsAmountLabel = QtWidgets.QLabel("Количество вопросов:")
        questionsAmountLineEdit = QtWidgets.QLineEdit()
        questionsAmountLineEdit.setPlaceholderText("от 1 до 99")
        questionsAmountLineEdit.setValidator(QtGui.QIntValidator(1, 99))

        quizDataPushButton = QtWidgets.QPushButton("Продолжить")
        quizDataPushButton.setDefault(True)

        quizDataLayout = QtWidgets.QGridLayout()
        quizDataLayout.addWidget(quizNameLabel, 0, 0)
        quizDataLayout.addWidget(quizNameLineEdit, 0, 1, 1, 2)
        quizDataLayout.addWidget(questionsAmountLabel, 1, 0)
        quizDataLayout.addWidget(questionsAmountLineEdit, 1, 1)
        quizDataLayout.addWidget(quizDataPushButton, 1, 2)

        questionsAmountGroupBox = QtWidgets.QGroupBox()
        questionsAmountGroupBox.setLayout(quizDataLayout)

        questionsDataLayout = QtWidgets.QVBoxLayout()

        questionsDataGroupBox = QtWidgets.QGroupBox()
        questionsDataGroupBox.setLayout(questionsDataLayout)

        questionsDataScrollArea = QtWidgets.QScrollArea()
        questionsDataScrollArea.setWidget(questionsDataGroupBox)
        questionsDataScrollArea.setWidgetResizable(True)
        questionsDataScrollArea.setFixedHeight(600)

        questionsDataLineEdits = []
        answersDataLineEdits = []
        correctAnswersButtonGroups = []

        createQuizPushButton = QtWidgets.QPushButton("Готово")
        createQuizPushButton.setDefault(True)
        createQuizPushButton.setEnabled(False)

        def processQuizDataPushButtonClick():
            def createQuestionDataGroupBox(questionNumber):
                questionsDataLineEdits.append(QtWidgets.QLineEdit())
                answersDataLineEdits.append(tuple(QtWidgets.QLineEdit() for _ in range(4)))
                correctAnswersButtonGroups.append(QtWidgets.QButtonGroup())

                questionDataLayout = QtWidgets.QGridLayout()
                questionDataLayout.addWidget(QtWidgets.QLabel(f"Вопрос №{questionNumber + 1}:"), 0, 0)
                questionDataLayout.addWidget(questionsDataLineEdits[questionNumber], 0, 1, 1, 2)
                for j in range(1, 5):
                    questionDataLayout.addWidget(QtWidgets.QLabel(f"Ответ №{j}:"), j, 0)
                    questionDataLayout.addWidget(answersDataLineEdits[questionNumber][j - 1], j, 1)

                    correctAnswerRadioButton = QtWidgets.QRadioButton("")
                    correctAnswersButtonGroups[questionNumber].addButton(correctAnswerRadioButton, j)
                    questionDataLayout.addWidget(correctAnswerRadioButton, j, 2)

                correctAnswersButtonGroups[questionNumber].button(1).setChecked(True)

                questionDataGroupBox = QtWidgets.QGroupBox()
                questionDataGroupBox.setLayout(questionDataLayout)

                return questionDataGroupBox

            if questionsAmountLineEdit.text() == "":
                return
            questionsAmountLineEdit.setText(questionsAmountLineEdit.text().lstrip("0"))
            questionsAmount = int(questionsAmountLineEdit.text())

            if self.questionsAmount == 0:
                for i in range(questionsAmount):
                    questionsDataLayout.addWidget(createQuestionDataGroupBox(i))

                self.questionsAmount = questionsAmount
                createQuizPushButton.setEnabled(True)
            elif self.questionsAmount < questionsAmount:
                for i in range(self.questionsAmount, questionsAmount):
                    questionsDataLayout.addWidget(createQuestionDataGroupBox(i))

                self.questionsAmount = questionsAmount
            elif self.questionsAmount > questionsAmount:
                for i in reversed(range(questionsAmount, questionsDataLayout.count())):
                    del questionsDataLineEdits[i]
                    del correctAnswersButtonGroups[i]
                    questionsDataLayout.removeWidget(questionsDataLayout.itemAt(i).widget())

                self.questionsAmount = questionsAmount

        def processCreateQuizPushButtonClick():
            tableName = quizNameLineEdit.text()
            if tableName == "":
                tableName = quizNameLineEdit.placeholderText()
            tableName = tableName.replace(" ", "_")

            cursor = self.database.cursor()
            cursor.execute(f"""
                CREATE TABLE {repr(tableName)}(
                    question TEXT,
                    answer1 TEXT,
                    answer2 TEXT,
                    answer3 TEXT,
                    answer4 TEXT,
                    correct_answer INTEGER
                )""")
            self.database.commit()

            for i in range(self.questionsAmount):
                answersData = answersDataLineEdits[i]

                cursor.execute(f"INSERT INTO {repr(tableName)} VALUES(?,?,?,?,?,?)",
                               (questionsDataLineEdits[i].text(),
                                answersData[0].text(), answersData[1].text(),
                                answersData[2].text(), answersData[3].text(),
                                correctAnswersButtonGroups[i].checkedId()))
                self.database.commit()

            self.close()

        quizDataPushButton.clicked.connect(processQuizDataPushButtonClick)
        createQuizPushButton.clicked.connect(processCreateQuizPushButtonClick)

        createQuizBoxLayout = QtWidgets.QVBoxLayout()
        createQuizBoxLayout.addWidget(questionsAmountGroupBox)
        createQuizBoxLayout.addWidget(questionsDataScrollArea)
        createQuizBoxLayout.addWidget(createQuizPushButton)
        self.setLayout(createQuizBoxLayout)
