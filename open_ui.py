from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import sqlite3, os

from program import Ui_MainWindow

class Okno(Ui_MainWindow):
    def __init__(self):
        super(Okno).__init__()

        # loadUi("untitled.ui", self)
        # self.loaddata()
    def setupUi(self, MainWindow):
        super(Okno, self).setupUi(MainWindow)
        # Todo: add our own functions
        self.pushButton_5.clicked.connect(self.get_data)
        self.pushButton_2.clicked.connect(self.dodawanie)
        self.pushButton_3.clicked.connect(self.usuwanie)
        # self.pushButton_7.clicked.connect(self.usuwanie_glowna)
        self.tableWidget.selectionModel().selectionChanged.connect(self.odczyt)
        self.tableWidget_3.selectionModel().selectionChanged.connect(self.odczyt)
        self.lineEdit.textChanged.connect(self.activate)
        #self.lineEdit_2.textChanged.connect(self.activate)
        self.pushButton_9.setEnabled(False)

    def activate(self):
        if self.lineEdit.text()=='':
            self.pushButton_2.setEnabled(False)
        else:
            self.pushButton_2.setEnabled(True)
        # if self.lineEdit_2.text()=='':
        #     self.pushButton_3.setEnabled(False)
        # else:
        #     self.pushButton_3.setEnabled(True)
    def odczyt(self, selected):
         for ix in selected.indexes():
             self.a=ix.row()
             self.readtable=self.tableWidget.item(1,1).text()
        # print("Wybrano nr: {0}".format(ix.row()+1))
         print(self.tableWidget.item(self.a, 1).text())
         self.dane = []
         self.dane.append(self.tableWidget.item(self.a, 0).text())
         self.dane.append(self.tableWidget.item(self.a, 1).text())
         self.dane.append(self.tableWidget.item(self.a, 2).text())
         self.dane.append(self.tableWidget.item(self.a, 3).text())
         print(self.dane)
         #bz=self.tableWidget_3.item(self.a,0).text()
         #print (bz)


    def get_data(self):
        os.remove("wybrane.db")
        db=sqlite3.connect("rusztowania.db")
        cursor=db.cursor()
        command = "SELECT * from rusztowania"
        result=cursor.execute(command)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        self.conn = sqlite3.connect('wybrane.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS Wybrane([ID] INTEGER PRIMARY KEY AUTOINCREMENT, [ID_z_bazy] TEXT, [Nazwa] TEXT, [Szerokość] TEXT, [Długość] TEXT, [Ilość] TEXT, Unique (ID_z_bazy))''')
        self.conn.commit()
        self.licznik = 0
    def dodawanie(self):
        #   conn = sqlite3.connect('wybrane.db')
        # c = conn.cursor()
        # c.execute('''CREATE TABLE IF NOT EXISTS Wybrane([ID] INTEGER PRIMARY KEY, [Nazwa] TEXT, [Szerokość] TEXT, [Długość] TEXT, [Ilość] TEXT)''')
        self.licznik = self.licznik + 1
        command = ("INSERT OR IGNORE INTO Wybrane VALUES ({0},'{1}','{2}','{3}','{4}','{5}')".format(self.licznik,self.dane[0],self.dane[1],self.dane[2],self.dane[3],self.lineEdit.text()))
        result = self.c.execute(command)
        command = ("UPDATE Wybrane SET Ilość = {0} WHERE ID_z_bazy = {1}".format(self.lineEdit.text(),self.a+1))
        result = self.c.execute(command)
        self.conn.commit()
        command1 = "SELECT * FROM Wybrane"
        result = self.c.execute(command1)
        self.tableWidget_3.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget_3.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_3.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        print(self.tableWidget_3.rowCount())
        if self.tableWidget_3.rowCount() > 0:
            self.pushButton_9.setEnabled(True)
    def usuwanie(self):
        wiersz=self.tableWidget_3.item(self.a,0).text()
        print (wiersz)
        command = ("DELETE FROM Wybrane WHERE ID = {0}".format(wiersz))
        result = self.c.execute(command)
        self.conn.commit()
        command1 = "SELECT * FROM Wybrane"
        result = self.c.execute(command1)
        self.tableWidget_3.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget_3.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_3.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        if self.tableWidget_3.rowCount() < 1:
            self.pushButton_9.setEnabled(False)
    # def usuwanie_glowna(self):
    #     wiersz = self.tableWidget.item(self.a, 0).text()
    #     print(wiersz)
    #     command = ("DELETE FROM rusztowania WHERE ID = {0}".format(wiersz))
    #     result = self.c.execute(command)
    #     self.conn.commit()
    #     command1 = "SELECT * FROM rusztowania"
    #     result = self.c.execute(command1)
    #     self.tableWidget.setRowCount(0)
    #     for row_number, row_data in enumerate(result):
    #         self.tableWidget.insertRow(row_number)
    #         for column_number, data in enumerate(row_data):
    #             self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

# Uruchomienie GUI
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Okno()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
