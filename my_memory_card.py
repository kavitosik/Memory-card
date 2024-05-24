from PyQt5.QtWidgets import QButtonGroup, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QApplication, QGroupBox, QRadioButton, QLabel
from PyQt5.QtCore import Qt
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('В каком году Феликс пришел в Stray kids', '2018', '2019', '2020', '2017'))
question_list.append(Question('Какая песня Stray kids самая популярная', 'S-Class', 'Gods Menu', 'Case 143', 'Maniak'))
question_list.append(Question('Самая популярная к-поп группа', 'BTS', 'Stray kids', 'G-idol', 'ASTRO'))
question_list.append(Question('В каком году Уджин ушёл из Stray kids', '2019', '2018', '2020', '2017'))

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(300, 200)

def show_answer():
    rbtnGroup.hide()
    answerGroup.show()
    answer_btn.setText('Следующий вопрос')

def show_question():
    answerGroup.hide()
    rbtnGroup.show()
    answer_btn.setText('Ответить')
    resetrbtnGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    resetrbtnGroup.setExclusive(True)

def click_OK():
    if answer_btn.text() == 'Ответить':
        check_answer()
    else:
        next_question()

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    text.setText(q.question)
    ans_text.setText(q.right_answer)
    show_question()

def next_question():
    main_win.total += 1
    print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)
    rand_quest = randint(0, len(question_list)-1)
    ask(question_list[rand_quest])

def show_correct(result):
    ans_text2.setText(result)
    show_answer()

def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
        print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)
        print('Рейтинг: ', (main_win.score/main_win.total*100), '%')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверно')
            print('Рейтинг: ', (main_win.score/main_win.total*100), '%')

text = QLabel('Вопрос')
answer_btn = QPushButton('Ответить')

rbtnGroup = QGroupBox('Варианты ответов:')

answerGroup = QGroupBox('Результат теста')
ans_text = QLabel('Правильный ответ')
ans_text2 = QLabel('Правильно/Неправильно')
ansVline = QVBoxLayout()
ansVline.addWidget(ans_text2, alignment=(Qt.AlignLeft | Qt.AlignTop))
ansVline.addWidget(ans_text, alignment = Qt.AlignHCenter, stretch = 2)
answerGroup.setLayout(ansVline)

rbtn1 = QRadioButton('вар1')
rbtn2 = QRadioButton('вар2')
rbtn3 = QRadioButton('вар3')
rbtn4 = QRadioButton('вар4')
answer = [rbtn1, rbtn2, rbtn3, rbtn4]

resetrbtnGroup = QButtonGroup()
resetrbtnGroup.addButton(rbtn1)
resetrbtnGroup.addButton(rbtn2)
resetrbtnGroup.addButton(rbtn3)
resetrbtnGroup.addButton(rbtn4)

rbtnHline = QHBoxLayout()
rbtnVline1 = QVBoxLayout()
rbtnVline2 = QVBoxLayout()
Hline1 = QHBoxLayout()
Hline2 = QHBoxLayout()
Hline3 = QHBoxLayout()
general_line = QVBoxLayout()

rbtnVline1.addWidget(rbtn1)
rbtnVline1.addWidget(rbtn2)
rbtnVline2.addWidget(rbtn3)
rbtnVline2.addWidget(rbtn4)
rbtnHline.addLayout(rbtnVline1)
rbtnHline.addLayout(rbtnVline2)

rbtnGroup.setLayout(rbtnHline)

Hline1.addWidget(text, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
Hline2.addWidget(rbtnGroup)
Hline2.addWidget(answerGroup)
Hline3.addStretch(1)
Hline3.addWidget(answer_btn, stretch = 2)
Hline3.addStretch(1)

general_line.addLayout(Hline1, stretch = 2)
general_line.addLayout(Hline2, stretch = 8)
general_line.addStretch(1)
general_line.addLayout(Hline3, stretch = 1)
general_line.addStretch(1)
general_line.setSpacing(5)
main_win.setLayout(general_line)

main_win.score = 0
main_win.total = 0

answer_btn.clicked.connect(click_OK)
next_question()
answerGroup.hide()

main_win.show()
app.exec_()