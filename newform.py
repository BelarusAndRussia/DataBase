# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit, QPushButton
import psycopg2, time

conn = psycopg2.connect(dbname='test', user='postgres', password='101010', host='localhost', port='1234')
conn.autocommit = True
cur = conn.cursor()


class Ui_Form(object):
    def setupUi(self, Form):
#mainWindow
        Form.setObjectName("Messenger")
        Form.resize(860, 531)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(860, 531))
        Form.setMaximumSize(QtCore.QSize(860, 531))
        Form.setSizeIncrement(QtCore.QSize(860, 531))
        self.chat = QtWidgets.QTextEdit(Form)
        self.chat.setGeometry(QtCore.QRect(50, 70, 511, 321))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chat.sizePolicy().hasHeightForWidth())
        self.chat.setSizePolicy(sizePolicy)
        self.chat.setReadOnly(True)
        self.chat.setObjectName("textEdit")
        self.sendLine = QtWidgets.QLineEdit(Form)
        self.sendLine.setGeometry(QtCore.QRect(70, 431, 351, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendLine.sizePolicy().hasHeightForWidth())
        self.sendLine.setSizePolicy(sizePolicy)
        self.sendLine.setObjectName("lineEdit")
        self.sendButton = QtWidgets.QPushButton(Form)
        self.sendButton.setGeometry(QtCore.QRect(450, 430, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.sendButton.setFont(font)
        self.sendButton.setObjectName("pushButton")
        #self.sendButton.setStyleSheet("background-color: black; color: white;")
        self.change_userButton = QtWidgets.QPushButton(Form)
        self.change_userButton.setGeometry(QtCore.QRect(630, 430, 200, 31))
        self.change_userButton.setFont(font)
        self.change_userButton.setObjectName("change_userButton")


        self.sendFileButton = QtWidgets.QPushButton(Form)
        self.sendFileButton.setGeometry(QtCore.QRect(450, 480, 93, 31))
        self.sendFileButton.setFont(font)
        self.sendFileButton.setObjectName("change_userButton")

 #onlineTable
        self.online = QtWidgets.QTableWidget(Form)
        self.online.setColumnCount(1)
        self.online.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.online.setHorizontalHeaderItem(0, item)
        self.online.setColumnWidth(0, 181)
        self.online.setGeometry(QtCore.QRect(640, 80, 171, 261))
        self.online.setObjectName("textEdit_2")
        self.online.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(700, 360, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)

        font = self.chat.font()
        font.setPointSize(12)
        self.chat.setFont(font)

        self.label_username = QtWidgets.QLabel(Form)
        self.label_username.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.label_username.setGeometry(QtCore.QRect(50, -105, 511, 321))

        self.lineSearch = QtWidgets.QLineEdit(Form)
        self.lineSearch.setGeometry(QtCore.QRect(250, 13, 230, 22))
        self.lineSearch.setObjectName("lineEdit_Search")

        self.combo = QtWidgets.QComboBox(Form)
        self.combo.setGeometry(QtCore.QRect(110, 13, 120, 22))
        self.combo.setEditable(False)
        self.combo.addItems(['Id', 'Login', 'Имя', 'Группа'])



        self.searchButton = QtWidgets.QPushButton(Form)
        self.searchButton.setGeometry(QtCore.QRect(500, 13, 100, 22))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle('Messenger')
        Form.setWindowIcon(QtGui.QIcon("icons\\chat_logo.png"))
        self.sendButton.setText(_translate("Form", "Отправить"))
        self.searchButton.setText(_translate("Form", "Найти"))
        item = self.online.horizontalHeaderItem(0)
        item.setText(_translate("Form", "online"))
        self.change_userButton.setText(_translate("Form", "Выйти из аккаунта"))
        self.sendFileButton.setText(_translate("Form", "Файл"))



class Identification(QtWidgets.QDialog):
    def __init__(self, parent=None):
        self.login = None
        self.password = None
        super(Identification, self).__init__(parent)
        self.setWindowTitle('Identification')
        self.resize(500, 120)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.setWindowIcon(QtGui.QIcon("icons\\ident.png"))
        layout = QGridLayout()

        label_name = QLabel('<font size="4"> Username </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please, enter your username')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('<font size="4"> Password </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setPlaceholderText('Please, enter your password')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button_login = QPushButton('Login')
        button_login.clicked.connect(self.loginIN)
        layout.addWidget(button_login, 2, 0, 1, 2)

        button_reg = QPushButton('Registration')
        button_reg.clicked.connect(self.registr)
        layout.addWidget(button_reg, 3, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

    def loginIN(self):
        self.login = self.lineEdit_username.text()
        self.password = self.lineEdit_password.text()
        cur.execute('select login from users')
        allLoginCort = cur.fetchall()
        allLogin = list(sum(allLoginCort, ()))
        cur.execute('select login from online')
        allLoginCortOnline = cur.fetchall()
        allLoginOnline = list(sum(allLoginCortOnline, ()))

        if self.login in allLogin:

            if self.check():
                if self.login in allLoginOnline:
                    d = ClassDialogFalse("User {0} is online!".format(self.login))
                    d.exec()
                    self.login = None
                    self.password = None

                else:
                    self.close()
            else:
                self.login = None
                self.password = None
                d = ClassDialogFalse("Incorrect password!")
                d.exec()
        else:
            self.login = None
            self.password = None
            d = ClassDialogFalse("Incorrect login!")
            d.exec()

    def registr(self):
        reg = Registration()
        reg.exec_()

    def check(self):
        cur.execute("select password from users where login = '{}'".format(self.login))
        checkPass = cur.fetchone()[0]
        if checkPass == self.password:
            return True
        return False


class Registration(QtWidgets.QDialog):
    def __init__(self, parent=None):
        self.login = None
        self.password = None
        self.name = None
        self.surname = None
        self.date = None
        super(Registration, self).__init__(parent)
        self.setWindowTitle('Registration')
        self.resize(500, 400)
        self.setWindowIcon(QtGui.QIcon("icons\\reg.jpg"))
        layout = QGridLayout()

        label_name = QLabel('<font size="4"> Username * </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please, enter your username')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        label_password = QLabel('<font size="4"> Password * </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Please, enter your password')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        label_name = QLabel('<font size="4"> Name * </font>')
        self.lineEdit_name = QLineEdit()
        self.lineEdit_name.setPlaceholderText('Please, enter your name')
        layout.addWidget(label_name, 2, 0)
        layout.addWidget(self.lineEdit_name, 2, 1)

        label_name = QLabel('<font size="4"> Surname * </font>')
        self.lineEdit_surname = QLineEdit()
        self.lineEdit_surname.setPlaceholderText('Please, enter your surname')
        layout.addWidget(label_name, 3, 0)
        layout.addWidget(self.lineEdit_surname, 3, 1)

        label_name = QLabel('<font size="4"> Birthday *</font>')
        self.lineEdit_bd = QLineEdit()
        self.lineEdit_bd.setPlaceholderText('Please, enter your birthday')
        layout.addWidget(label_name, 4, 0)
        layout.addWidget(self.lineEdit_bd, 4, 1)

        label_name = QLabel('<font size="4"> City* </font>')
        self.lineEdit_city = QLineEdit()
        self.lineEdit_city.setPlaceholderText('Please, enter your native city')
        layout.addWidget(label_name, 5, 0)
        layout.addWidget(self.lineEdit_city, 5, 1)

        label_name = QLabel('<font size="4"> Group* </font>')
        self.lineEdit_group = QLineEdit()
        self.lineEdit_group.setPlaceholderText('Please, enter your group')
        layout.addWidget(label_name, 6, 0)
        layout.addWidget(self.lineEdit_group, 6, 1)

        button_join = QPushButton('Join')
        button_join.clicked.connect(self.addUser)
        layout.addWidget(button_join, 7, 0, 1, 2)

        self.setLayout(layout)

    def addUser(self):
        cur.execute('select count (*) from users')
        id = cur.fetchone()[0] + 1
        cur.execute('select login from users')
        allLoginCort = cur.fetchall()
        allLogin = list(sum(allLoginCort, ()))
        login = self.lineEdit_username.text()
        fn = self.lineEdit_name.text()
        sn = self.lineEdit_surname.text()
        pw = self.lineEdit_password.text()
        bd = self.lineEdit_bd.text()
        city = self.lineEdit_city.text()
        group = self.lineEdit_group.text()


        date = time.strftime("%Y-%m-%d", time.localtime())
        if id != "" and login != "" and fn != "" and sn != "" and pw != "" and bd != "" and city != "" and group != "":
            if login not in allLogin:
                try:
                    cur.execute(f"insert into users (id, login, password) values ({id}, '{login}', '{pw}')")
                    cur.execute(f"insert into user_info (user_id, f_name, surname, birthday, group_n, city, date_registration) values ({id}, '{fn}', '{sn}', '{bd}', '{group}', '{city}', '{date}')")
                    d = ClassDialogTrue()
                    d.exec()
                    self.close()
                except:
                    cur.execute(f"delete from users where id = {id}")
                    cur.execute(f"delete from user_info where user_id = {id}")
                    d = ClassDialogFalse("Incorrect data!")
                    d.exec()
            else:
                d = ClassDialogFalse("User with username '{}' already exist".format(login))
                d.exec()
        else:
            d = ClassDialogFalse("Please, fill in all positions with *")
            d.exec()

class ClassDialogFalse(QtWidgets.QDialog):
    def __init__(self, text, parent=None):
        super(ClassDialogFalse, self).__init__(parent)
        self.setGeometry(710, 400, 500, 100)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.btnClosed)
        self.verticalLayout.addWidget(self.pushButton)
        self.setWindowTitle(text)
        self.pushButton.setText("Ok")
        self.setWindowIcon(QtGui.QIcon("icons\\false.jpg"))
        self.setWhatsThis('')

    def btnClosed(self):
        self.close()

class ClassDialogTrue(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClassDialogTrue, self).__init__(parent)
        self.setGeometry(710, 400, 500, 100)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.btnClosed)
        self.verticalLayout.addWidget(self.pushButton)
        self.setWindowTitle("Registration completed successfully!")
        self.pushButton.setText("Ok")
        self.setWindowIcon(QtGui.QIcon("icons\\true.jpg"))
        self.setWhatsThis('')

    def btnClosed(self):
        self.close()


class Find_user(QtWidgets.QDialog):
    def __init__(self, param, text, parent=None):
        super(Find_user, self).__init__(parent)
        self.setGeometry(810, 350, 250, 300)
        self.param = param
        self.text = text
        self.setWindowTitle("Search result")
        self.setWindowIcon(QtGui.QIcon("icons\\search.jpg"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableSearch = QtWidgets.QTableWidget(self)
        self.tableSearch.setGeometry(QtCore.QRect(120, 130, 300, 341))
        self.tableSearch.setObjectName("tableWidget")
        self.tableSearch.setColumnCount(1)
        self.tableSearch.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableSearch.setHorizontalHeaderItem(0, item)
        self.tableSearch.setColumnWidth(0, 250)
        self.verticalLayout.addWidget(self.tableSearch)
        self.setWhatsThis('')
        self.tableSearch.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableSearch.itemDoubleClicked.connect(self.on_cell_item_clicked)
        self.search_by()

    def on_cell_item_clicked(self):
        col = self.tableSearch.currentColumn()
        row = self.tableSearch.currentRow()
        login = self.tableSearch.item(row, col).text()
        cur.execute(f"select id from users where login = '{login}'")
        Id = cur.fetchone()[0]
        cur.execute(f"select f_name from user_info where user_id = {Id}")
        fn = cur.fetchone()[0]
        cur.execute(f'select surname from user_info where user_id = {Id}')
        sn = cur.fetchone()[0]
        cur.execute(f'select birthday from user_info where user_id = {Id}')
        bd = cur.fetchone()[0]
        cur.execute(f'select group_n from user_info where user_id = {Id}')
        group = cur.fetchone()[0]
        cur.execute(f'select city from user_info where user_id = {Id}')
        city = cur.fetchone()[0]
        cur.execute(f'select date_registration from user_info where user_id = {Id}')
        dr = cur.fetchone()[0]
        d = Info(Id, login, fn, sn, bd, city, group, dr)
        d.exec()

    def load_search_res(self, data):
        self.tableSearch.setRowCount(0)
        for i, row in enumerate(data):
            self.tableSearch.insertRow(i)
            for j, cell in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(cell))
                self.tableSearch.setItem(i, j, item)
        return 0

    def search_by(self):
        try:
            if self.param == 'Id':
                cur.execute(f'select login from users where id = {self.text}')
                data = cur.fetchall()
            if self.param == 'Имя':
                t = self.text.split(' ')
                t[0] = t[0][0].upper() + t[0][1:].lower()
                t[1] = t[1][0].upper() + t[1][1:].lower()
                if len(t) == 2:
                    cur.execute(f"select login from users as a left join user_info as b on a.id = b.user_id"
                                f" where b.f_name = '{t[0]}' AND b.surname = '{t[1]}'")
                    data = cur.fetchall()
                    if len(data) == 0:
                        cur.execute(f"select login from users as a left join user_info as b on a.id = b.user_id"
                                    f" where b.f_name = '{t[1]}' AND b.surname = '{t[0]}'")
                        data = cur.fetchall()
                if len(t) == 1:
                    cur.execute(f"select login from users as a left join user_info as b on a.id = b.user_id"
                                f" where b.f_name = '{t[0]}'")
                    data = cur.fetchall()
                    if len(data) == 0:
                        cur.execute(f"select login from users as a left join user_info as b on a.id = b.user_id"
                                    f" where b.surname = '{t[0]}'")
                        data = cur.fetchall()
            if self.param == 'Группа':
                cur.execute(f"select login from users as a left join user_info as b on a.id = b.user_id"
                            f" where b.group_n = '{self.text}'")
                data = cur.fetchall()
            if self.param == 'Login':
                cur.execute(f"select login from users as a left join user_info as b on a.id = b.user_id"
                            f" where a.login = '{self.text}'")
                data = cur.fetchall()
            self.load_search_res(data)
        except:
            pass


    def btnClosed(self):
        self.close()


class Info(QtWidgets.QDialog):
    def __init__(self, Id, login, fn, sn, bd, city, group, dr, parent=None):
        self.login = None
        self.password = None
        self.name = None
        self.surname = None
        self.date = None
        super(Info, self).__init__(parent)
        self.setWindowTitle('Information')
        self.resize(500, 400)
        self.setWindowIcon(QtGui.QIcon("icons\\info.png"))
        layout = QGridLayout()

        label_id1 = QLabel('<font size="4"> Id:  </font>')
        label_id2 = QLabel(f'<font size="4"> {Id} </font>')
        layout.addWidget(label_id1, 0, 0)
        layout.addWidget(label_id2, 0, 1)

        label_un1 = QLabel('<font size="4"> Login:  </font>')
        label_un2 = QLabel(f'<font size="4"> {login}  </font>')
        layout.addWidget(label_un1, 1, 0)
        layout.addWidget(label_un2, 1, 1)

        label_name1 = QLabel('<font size="4"> Имя: </font>')
        label_name2 = QLabel(f'<font size="4"> {fn}  </font>')
        layout.addWidget(label_name1, 2, 0)
        layout.addWidget(label_name2, 2, 1)

        label_sn1 = QLabel('<font size="4"> Фамилия: </font>')
        label_sn2 = QLabel(f'<font size="4"> {sn}  </font>')
        layout.addWidget(label_sn1, 3, 0)
        layout.addWidget(label_sn2, 3, 1)

        label_bd1 = QLabel('<font size="4"> Дата рождения: </font>')
        label_bd2 = QLabel(f'<font size="4"> {bd}  </font>')
        layout.addWidget(label_bd1, 4, 0)
        layout.addWidget(label_bd2, 4, 1)

        label_city1 = QLabel('<font size="4"> Дата рождения: </font>')
        label_city2 = QLabel(f'<font size="4"> {city}  </font>')
        layout.addWidget(label_city1, 5, 0)
        layout.addWidget(label_city2, 5, 1)

        label_gr1 = QLabel('<font size="4"> Группа: </font>')
        label_gr2 = QLabel(f'<font size="4"> {group}  </font>')
        layout.addWidget(label_gr1, 6, 0)
        layout.addWidget(label_gr2, 6, 1)

        label_dr1 = QLabel('<font size="4"> Дата регистрации: </font>')
        label_dr2 = QLabel(f'<font size="4"> {dr}  </font>')
        layout.addWidget(label_dr1, 7, 0)
        layout.addWidget(label_dr2, 7, 1)

        self.setLayout(layout)

class ClassDialogReally(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClassDialogReally, self).__init__(parent)
        self.setGeometry(710, 400, 500, 100)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonYes = QtWidgets.QPushButton(self)
        self.pushButtonYes.setObjectName("pushButton")
        self.pushButtonYes.clicked.connect(self.btnClosed)
        self.verticalLayout.addWidget(self.pushButtonYes)
        self.pushButtonNo = QtWidgets.QPushButton(self)
        self.pushButtonNo.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButtonNo)
        self.setWindowTitle("Вы действительно хотите выйти из аккаунта?")
        self.pushButtonYes.setText("Да")
        self.pushButtonNo.setText("Нет")
        self.pushButtonNo.clicked.connect(self.flagOn)
        self.setWindowIcon(QtGui.QIcon("icons\\question.png"))
        self.setWhatsThis('')
        self.flag = False

    def btnClosed(self):
        self.close()

    def flagOn(self):
        self.flag = True
        self.close()

    def Getflag(self):
        return self.flag

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())