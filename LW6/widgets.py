from PyQt5 import QtWidgets, QtGui, QtCore


class MenuWidget(QtWidgets.QWidget):
    def __init__(self, database, playQuizWidget, quizResultWidget, createQuizWidget, parent=None):
        super().__init__(parent)
        self.database = database
        self.playQuizWidget = playQuizWidget
        self.quizResultWidget = quizResultWidget
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
            cursor = self.database.cursor()
            cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table'")
            result = cursor.fetchone()
            if result[0] == 0:
                quizzesNotFoundMessageBox = QtWidgets.QMessageBox()
                quizzesNotFoundMessageBox.setText("Викторины не найдены!")
                quizzesNotFoundMessageBox.setWindowTitle(self.windowTitle())
                quizzesNotFoundMessageBox.exec()
                return

            self.playQuizWidget = PlayQuizWidget(self.database, self.quizResultWidget)

        def processCreateQuizPushButton():
            self.createQuizWidget = CreateQuizWidget(self.database)

        playQuizPushButton.clicked.connect(processPlayQuizPushButton)
        createQuizPushButton.clicked.connect(processCreateQuizPushButton)

        menuLayout = QtWidgets.QVBoxLayout()
        menuLayout.addWidget(playQuizPushButton)
        menuLayout.addWidget(createQuizPushButton)

        self.setLayout(menuLayout)


class PlayQuizWidget(QtWidgets.QWidget):
    def __init__(self, database, quizResultWidget, parent=None):
        super().__init__(parent)
        self.database = database
        self.quizResultWidget = quizResultWidget

        self.setWindowTitle("Викторина")
        self.initGui()
        self.show()

    def initGui(self):
        quizNameLabel = QtWidgets.QLabel("Название викторины:")

        quizNameLineEdit = QtWidgets.QLineEdit()
        quizNameLineEdit.setPlaceholderText("Quiz")
        quizNameLineEdit.setValidator(QtGui.QRegularExpressionValidator(QtCore.QRegularExpression(r"^[a-zA-Z0-9 -]+")))

        quizNamePushButton = QtWidgets.QPushButton("Играть")
        quizNamePushButton.setDefault(True)

        quizNameLayout = QtWidgets.QHBoxLayout()
        quizNameLayout.addWidget(quizNameLabel)
        quizNameLayout.addWidget(quizNameLineEdit)
        quizNameLayout.addWidget(quizNamePushButton)

        quizNameGroupBox = QtWidgets.QGroupBox()
        quizNameGroupBox.setLayout(quizNameLayout)

        questionLayout = QtWidgets.QGridLayout()

        questionGroupBox = QtWidgets.QGroupBox()
        questionGroupBox.setLayout(questionLayout)

        def playQuiz(questions, answers, correctAnswers):
            questionLabel = QtWidgets.QLabel(f"{1}. {questions[0][0]}")

            questionButtonGroup = QtWidgets.QButtonGroup()

            questionPushButton = QtWidgets.QPushButton("Продолжить")
            questionPushButton.setDefault(True)

            questionLayout.addWidget(questionLabel, 0, 0, QtCore.Qt.AlignCenter)
            for i in range(1, 5):
                questionRadioButton = QtWidgets.QRadioButton(answers[0][i - 1])

                questionButtonGroup.addButton(questionRadioButton, i)
                questionLayout.addWidget(questionRadioButton, i, 0)
            questionButtonGroup.button(1).setChecked(True)
            questionLayout.addWidget(questionPushButton, 5, 0, QtCore.Qt.AlignCenter)

            userAnswers = []

            def processQuestionPushButtonClick():
                userAnswer = questionButtonGroup.checkedId()
                if userAnswer == -1:
                    # questionMessageBox = QtWidgets.QMessageBox()
                    # questionMessageBox.setText("Выберите правильный вариант ответа!")
                    # questionMessageBox.setWindowTitle(self.windowTitle())
                    # questionMessageBox.exec()
                    return
                userAnswers.append(userAnswer)

                currentQuestionNumber = len(userAnswers)

                if currentQuestionNumber == len(questions):
                    self.quizResultWidget = QuizResultWidget(questions, answers, correctAnswers, userAnswers)
                    self.close()
                    return

                questionLabel.setText(f"{currentQuestionNumber + 1}. {questions[currentQuestionNumber][0]}")

                for j in range(1, 5):
                    questionButtonGroup.button(j).setText(answers[currentQuestionNumber][j - 1])
                # questionButtonGroup.button(userAnswer).setChecked(False)

            questionPushButton.clicked.connect(processQuestionPushButtonClick)

        def processQuizNamePushButtonClick():
            tableName = quizNameLineEdit.text()
            if tableName == "":
                tableName = quizNameLineEdit.placeholderText()

            cursor = self.database.cursor()

            cursor.execute(
                f"SELECT name FROM sqlite_master WHERE type='table' and name={repr(tableName)}")
            result = cursor.fetchone()
            if result is None:
                quizNotFoundMessageBox = QtWidgets.QMessageBox()
                quizNotFoundMessageBox.setText(f"Викторина {tableName} не найдена!")
                quizNotFoundMessageBox.setWindowTitle(self.windowTitle())
                quizNotFoundMessageBox.exec()
                return

            quizNamePushButton.setEnabled(False)

            cursor.execute(f"SELECT question FROM {repr(tableName)}")
            questions = cursor.fetchall()

            cursor.execute(f"SELECT answer1,answer2,answer3,answer4 FROM {repr(tableName)}")
            answers = cursor.fetchall()

            cursor.execute(f"SELECT correct_answer FROM {repr(tableName)}")
            correctAnswers = cursor.fetchall()

            questionGroupBox.setTitle(tableName)

            playQuiz(questions, answers, correctAnswers)

        quizNamePushButton.clicked.connect(processQuizNamePushButtonClick)

        playQuizLayout = QtWidgets.QVBoxLayout()
        playQuizLayout.addWidget(quizNameGroupBox)
        playQuizLayout.addWidget(questionGroupBox)
        self.setLayout(playQuizLayout)


class QuizResultWidget(QtWidgets.QWidget):
    def __init__(self, questions, answers, correctAnswers, userAnswers, parent=None):
        super().__init__(parent)
        self.questions = questions
        self.answers = answers
        self.correctAnswers = correctAnswers
        self.userAnswers = userAnswers

        self.setWindowTitle("Результат викторины")
        self.initGui()
        self.show()

    def initGui(self):
        resultLabel = QtWidgets.QLabel()

        resultPushButton = QtWidgets.QPushButton("Показать подробный результат")
        resultPushButton.setDefault(True)

        resultLayout = QtWidgets.QVBoxLayout()
        resultLayout.addWidget(resultLabel, alignment=QtCore.Qt.AlignCenter)
        resultLayout.addWidget(resultPushButton, alignment=QtCore.Qt.AlignCenter)

        resultGroupBox = QtWidgets.QGroupBox()
        resultGroupBox.setLayout(resultLayout)

        detailedResultLayout = QtWidgets.QVBoxLayout()

        detailedResultGroupBox = QtWidgets.QGroupBox()
        detailedResultGroupBox.setLayout(detailedResultLayout)

        detailedResultScrollArea = QtWidgets.QScrollArea()
        detailedResultScrollArea.setWidget(detailedResultGroupBox)
        detailedResultScrollArea.setWidgetResizable(True)
        detailedResultScrollArea.setFixedHeight(600)

        def processResultPushButton():
            resultPushButton.setEnabled(False)

            result = 0
            questionsAmount = len(self.questions)

            for i in range(questionsAmount):
                answersLabels = []

                detailedQuestionResultLayout = QtWidgets.QGridLayout()
                detailedQuestionResultLayout.addWidget(QtWidgets.QLabel(f"Вопрос №{i + 1}:"), 0, 0)
                detailedQuestionResultLayout.addWidget(QtWidgets.QLabel(self.questions[i][0]), 0, 1, 1, 2)
                for j in range(1, 5):
                    answersLabels.append(QtWidgets.QLabel(self.answers[i][j - 1]))
                    detailedQuestionResultLayout.addWidget(QtWidgets.QLabel(f"Ответ №{j}:"), j, 0)
                    detailedQuestionResultLayout.addWidget(answersLabels[j - 1], j, 1)

                if self.userAnswers[i] == self.correctAnswers[i][0]:
                    answersLabels[self.userAnswers[i] - 1].setStyleSheet("QLabel { color: green }")
                    answersLabels[self.userAnswers[i] - 1].setText(answersLabels[i].text() + " \u2705")

                    result += 1
                else:
                    answersLabels[self.userAnswers[i] - 1].setStyleSheet("QLabel { color: red }")
                    answersLabels[self.userAnswers[i] - 1].setText(answersLabels[i].text() + " \u274E")

                resultLabel.setText(f"Ваш результат: {result}/{questionsAmount}")

                detailedQuestionResultGroupBox = QtWidgets.QGroupBox()
                detailedQuestionResultGroupBox.setLayout(detailedQuestionResultLayout)

                detailedResultLayout.addWidget(detailedQuestionResultGroupBox)

        resultPushButton.clicked.connect(processResultPushButton)

        quizResultLayout = QtWidgets.QVBoxLayout()
        quizResultLayout.addWidget(resultGroupBox)
        quizResultLayout.addWidget(detailedResultScrollArea)
        self.setLayout(quizResultLayout)


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

        quizData = QtWidgets.QGroupBox()
        quizData.setLayout(quizDataLayout)

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

        createQuizPushButton = QtWidgets.QPushButton("Создать")
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

                    correctAnswerRadioButton = QtWidgets.QRadioButton()
                    correctAnswersButtonGroups[questionNumber].addButton(correctAnswerRadioButton, j)
                    questionDataLayout.addWidget(correctAnswerRadioButton, j, 2)

                correctAnswersButtonGroups[questionNumber].button(1).setChecked(True)

                questionDataGroupBox = QtWidgets.QGroupBox()
                questionDataGroupBox.setLayout(questionDataLayout)

                return questionDataGroupBox

            if questionsAmountLineEdit.text() == "":
                questionsAmountMessageBox = QtWidgets.QMessageBox()
                questionsAmountMessageBox.setText("Введите количество вопросов в викторине!")
                questionsAmountMessageBox.setWindowTitle(self.windowTitle())
                questionsAmountMessageBox.exec()
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

            createQuizMessageBox = QtWidgets.QMessageBox()
            createQuizMessageBox.setText(f"Викторина {tableName} успешно создана!")
            createQuizMessageBox.setWindowTitle(self.windowTitle())
            createQuizMessageBox.exec()

            self.close()

        quizDataPushButton.clicked.connect(processQuizDataPushButtonClick)
        createQuizPushButton.clicked.connect(processCreateQuizPushButtonClick)

        createQuizBoxLayout = QtWidgets.QVBoxLayout()
        createQuizBoxLayout.addWidget(quizData)
        createQuizBoxLayout.addWidget(questionsDataScrollArea)
        createQuizBoxLayout.addWidget(createQuizPushButton)

        self.setLayout(createQuizBoxLayout)
