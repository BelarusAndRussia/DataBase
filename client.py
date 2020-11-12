import socket
import sys
import os
import time
from threading import Thread
import psycopg2

from PyQt5 import QtWidgets

import newform

tcpClientA = None
BUFFER = 536870912#2097152
conn = psycopg2.connect(dbname='test', user='postgres', password='101010', host='localhost', port='1234')
conn.autocommit = True
cur = conn.cursor()

Ui_Form = newform.Ui_Form
class appCorrectData(QtWidgets.QMainWindow, Thread, Ui_Form):

    def __init__(self, login, password):
        QtWidgets.QMainWindow.__init__(self)
        Thread.__init__(self)
        Ui_Form.__init__(self)
        self.setupUi(self)
        self.login = login
        self.password = password
        # init data

        # events
        self.sendButton.clicked.connect(self.send)
        self.sendLine.returnPressed.connect(self.send)
        self.searchButton.clicked.connect(self.search)
        self.sendFileButton.clicked.connect(self.sendFile)

        #form
    def send(self):
        text = self.sendLine.text()
        try:
            if text != "":
                self.chat.append("me: " + text)
                tcpClientA.send(("[" + self.login + "]" + ": " + text).encode())
                self.insert_message(text)
            self.sendLine.setText("")
        except:
            sys.exit()

    def run(self):
        host = socket.gethostname()
        port = 9090
        global tcpClientA, join
        tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        tcpClientA.connect((host, port))
        join = False
        if join == False:
            self.insert_online()
            data3 = self.select_online()
            self.load_data(data3)
            self.label_username.setText(f"User: {self.login}")
            tcpClientA.sendto(("[" + self.login + "] => join chat ").encode("utf-8"), (host, port))
            join = True
        try:
            flag = 0
            while True:
                data = tcpClientA.recv(BUFFER)
                if data.decode("utf-8").endswith(">>"):
                    buff_ = data.decode("utf-8")
                    char1 = '<<'
                    char2 = '>>'
                    file_name = buff_[buff_.find(char1)+2 : buff_.find(char2)]
                    flag = 1

                if flag == 2:
                    #b = data.decode("utf-8")[:-5]
                    f1 = open(file_name, "wb")
                    f1.write(data)
                    f1.close()
                    flag = 0

                elif flag == 0 or flag == 1:
                    self.chat.append(data.decode("utf-8"))
                    data1 = self.select_online()
                    self.load_data(data1)
                    if flag == 1:
                        flag = 2

        except:
            sys.exit()


    def sendFile(self):
        F = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file', '')[0]
        if F:
            self.SIZE = os.path.getsize(F)
            fname_ = F.split('/')
            fname = fname_[-1]
            self.chat.append("me: " + "<<" + fname + ">>")
            tcpClientA.send(("[" + self.login + "]" + ": " + "<<" + fname + ">>").encode())
            self.insert_message(fname)

            f = open(F, "rb")
            data = f.read(self.SIZE)
            while (data):
                if tcpClientA.send(data):
                    data = f.read(self.SIZE)
            f.close()

        #database

    def select_online(self):
        select = 'select * from online'
        cur.execute(select)
        data = cur.fetchall()
        return data

    def load_data(self, data):
        self.online.setRowCount(0)
        for i, row in enumerate(data):
            self.online.insertRow(i)
            for j, cell in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(cell))
                self.online.setItem(i, j, item)
        return 0

    def insert_online(self):
        cur.execute("insert into online (login) "
                    "values ('{0}')".format(self.login))
        return 0

    def insert_message(self, text):
        cur.execute("select count (*) from messages_common")
        message_id = cur.fetchone()[0] + 1
        date_and_time = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
        cur.execute("select id from users where login = '{0}'".format(self.login))
        from_who_id = cur.fetchone()[0]
        cur.execute("insert into messages_common (message_id, message, date_departure, fk_from_who_id) "
                    "values ({0}, '{1}', '{2}', {3})".format(message_id, text, date_and_time, from_who_id))
        return 0


    def delete_online(self, delete_log):
        cur.execute("delete from online where login = '{0}'".format(delete_log))
        return 0

    def search(self):
        text = self.lineSearch.text()
        param = self.combo.currentText()
        if text:
            d = newform.Find_user(param, text)
            d.exec()
            self.lineSearch.setText("")


    def closeEvent(self, event):
        self.delete_online(self.login)
        tcpClientA.send(("[" + self.login + "] <= left chat ").encode())
        tcpClientA.close()

def show_chat(login, password):
    a = appCorrectData(login, password)
    a.start()
    a.show()
    a.change_userButton.clicked.connect(lambda : show_form(a))

def show_form(a=False):
    if a:
        a.close()
    log = newform.Identification()
    log.exec_()
    login = log.login
    password = log.password
    if login != None and password != None:
        show_chat(login, password)
    if (login == None and password == None):
        sys.exit()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    show_form(a=False)
    sys.exit(app.exec_())
