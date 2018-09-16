# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import time
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    submit=False
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 413)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(-4, 0, 555, 411))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(6, 0, 541, 381))
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.label_7.setScaledContents(False)
        self.label_7.setObjectName("label_7")
        self.label_7.raise_()
        
        
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(210, 30, 241, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(60, 40, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(210, 90, 241, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(60, 170, 81, 31))
        self.pushButton.hide()
        font = QtGui.QFont()
        font.setPointSize(9)

        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 170, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.hide()
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(60, 240, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(50, 320, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(170, 240, 320, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(True)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(170, 320, 320, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(True)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 170, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.pushButton_3.clicked.connect(self.button3Clicked)
        
        '''self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 140, 491, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")'''

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Nome/ID"))
        self.label_2.setText(_translate("Dialog", "Código de Serviço"))
        self.pushButton.setText(_translate("Dialog", "Exportar PDF"))
        self.pushButton_2.setText(_translate("Dialog", "Exportar CSV"))
        self.label_3.setText(_translate("Dialog", "Resultado"))
        self.label_4.setText(_translate("Dialog", "Observações"))
        self.pushButton_3.setText(_translate("Dialog", "Enviar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Tab 2"))
        
    def button3Clicked(self):
        #check if data input is correct and then runs code xxxx
        #submit=check_data()
        
        submit=True
        if submit:
            #self.verticalLayout.addWidget(, 0, QtCore.Qt.AlignRight)
            App("","Dados enviados!")
            #run code xxxx and checks database
            #resultado, obs=code()
            resultado="  Recomendação de exames futuros: Eletrocardiograma"
            obs = " 75% de chance de desenvolver problema cardíaco"          
            ########
            time.sleep(2)
            App("Resultado de Busca","Concluído")
            self.pushButton_3.hide()
            self.pushButton_2.show()
            self.pushButton.show()
            
            self.label_5.setText(resultado)
            self.label_6.setText(obs)
            
        else:
            App("","Dados incorretos. Preencha novamente.")

class App(QWidget):
 
    def __init__(self, title, message):
        super().__init__()
        self.title = title
        self.message = message
        self.left = 400
        self.top = 250
        
        self.width = 320
        self.height = 200

        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        QMessageBox.about(self, self.title, self.message)
        self.show()
        
app=QApplication(sys.argv)
Dialog= QDialog()
ui=Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
sys.exit(app.exec_())