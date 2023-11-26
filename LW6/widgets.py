from PyQt5 import QtWidgets, QtGui
import sqlite3


class MenuWidget(QtWidgets.QWidget):
    def __init__(self, playQuizWidget, createQuizWidget, parent=None):
        super().__init__(parent)
        self.playQuizWidget = playQuizWidget
        self.createQuizWidget = createQuizWidget

        self.setWindowTitle("Quiz Game")

        playQuizPushButton = QtWidgets.QPushButton("Играть в викторину")
        playQuizPushButton.setDefault(True)
        playQuizPushButton.clicked.connect(playQuizWidget.show)

        createQuizPushButton = QtWidgets.QPushButton("Создать викторину")
        createQuizPushButton.setDefault(True)
        createQuizPushButton.clicked.connect(createQuizWidget.show)

        menuBoxLayout = QtWidgets.QVBoxLayout()
        menuBoxLayout.addWidget(playQuizPushButton)
        menuBoxLayout.addWidget(createQuizPushButton)
        self.setLayout(menuBoxLayout)


class PlayQuizWidget(QtWidgets.QWidget):
    def __init__(self, database, parent=None):
        super().__init__(parent)
        self.database = database

        self.setWindowTitle("Викторина")


class CreateQuizWidget(QtWidgets.QWidget):
    def __init__(self, database, parent=None):
        super().__init__(parent)
        self.database = database
        self.questionsAmount = 0

        questionsAmountLabel = QtWidgets.QLabel("Количество вопросов:")
        questionsAmountLineEdit = QtWidgets.QLineEdit()
        questionsAmountLineEdit.setPlaceholderText("от 1 до 99")
        questionsAmountLineEdit.setValidator(QtGui.QIntValidator(1, 99))

        questionsAmountPushButton = QtWidgets.QPushButton("Продолжить")
        questionsAmountPushButton.setDefault(True)

        questionsAmountBoxLayout = QtWidgets.QHBoxLayout()
        questionsAmountBoxLayout.addWidget(questionsAmountLabel)
        questionsAmountBoxLayout.addWidget(questionsAmountLineEdit)
        questionsAmountBoxLayout.addWidget(questionsAmountPushButton)

        questionsAmountGroupBox = QtWidgets.QGroupBox()
        questionsAmountGroupBox.setLayout(questionsAmountBoxLayout)

        questionsTextGroupBox = QtWidgets.QGroupBox()

        QuestionsTextScrollArea = QtWidgets.QScrollArea()
        QuestionsTextScrollArea.setWidget(questionsTextGroupBox)
        QuestionsTextScrollArea.setWidgetResizable(True)
        QuestionsTextScrollArea.setFixedHeight(600)

        questionsTextBoxLayout = QtWidgets.QFormLayout()

        questionsTextGroupBox.setLayout(questionsTextBoxLayout)

        questionsTextLabels = []
        questionsTextLineEdits = []

        questionsTextPushButton = QtWidgets.QPushButton("Готово")
        questionsTextPushButton.setDefault(True)

        def processQuestionsAmountPushButtonClick():
            questionsAmount = int(questionsAmountLineEdit.text())

            if questionsAmount == 0:
                return
            if self.questionsAmount == 0:
                for i in range(questionsAmount):
                    questionsTextLabels.append(QtWidgets.QLabel(f"Вопрос №{i + 1}:"))
                    questionsTextLineEdits.append(QtWidgets.QLineEdit())
                    questionsTextBoxLayout.addRow(questionsTextLabels[i], questionsTextLineEdits[i])

                self.questionsAmount = questionsAmount
                questionsTextBoxLayout.addRow(questionsTextPushButton)
            elif self.questionsAmount < questionsAmount:
                for i in range(self.questionsAmount, questionsAmount):
                    questionsTextLabels.append(QtWidgets.QLabel(f"Вопрос №{i + 1}:"))
                    questionsTextLineEdits.append(QtWidgets.QLineEdit())
                    questionsTextBoxLayout.insertRow(i, questionsTextLabels[i], questionsTextLineEdits[i])

                self.questionsAmount = questionsAmount
            elif self.questionsAmount > questionsAmount:
                for i in reversed(range(questionsAmount, questionsTextBoxLayout.rowCount() - 1)):
                    del questionsTextLabels[i]
                    del questionsTextLineEdits[i]
                    questionsTextBoxLayout.removeRow(i)

                self.questionsAmount = questionsAmount

        questionsAmountPushButton.clicked.connect(processQuestionsAmountPushButtonClick)

        createQuizBoxLayout = QtWidgets.QVBoxLayout()
        createQuizBoxLayout.addWidget(questionsAmountGroupBox)
        createQuizBoxLayout.addWidget(QuestionsTextScrollArea)
        self.setLayout(createQuizBoxLayout)

        self.setWindowTitle("Создание викторины")
