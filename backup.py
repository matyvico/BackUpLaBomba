# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'backup.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(291, 357)
        MainWindow.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radioCada = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioCada.setObjectName("radioCada")
        self.gridLayout_3.addWidget(self.radioCada, 1, 0, 1, 1)
        self.timeCada = QtWidgets.QTimeEdit(self.groupBox_2)
        self.timeCada.setTime(QtCore.QTime(0, 30, 0))
        self.timeCada.setMinimumTime(QtCore.QTime(0, 30, 0))
        self.timeCada.setObjectName("timeCada")
        self.gridLayout_3.addWidget(self.timeCada, 1, 1, 1, 2)
        self.radioDiario = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioDiario.setChecked(True)
        self.radioDiario.setObjectName("radioDiario")
        self.gridLayout_3.addWidget(self.radioDiario, 0, 0, 1, 1)
        self.timeDiario = QtWidgets.QTimeEdit(self.groupBox_2)
        self.timeDiario.setTime(QtCore.QTime(23, 30, 0))
        self.timeDiario.setObjectName("timeDiario")
        self.gridLayout_3.addWidget(self.timeDiario, 0, 1, 1, 2)
        self.gridLayout.addWidget(self.groupBox_2, 5, 0, 2, 1)
        self.pushProgramar = QtWidgets.QPushButton(self.centralwidget)
        self.pushProgramar.setObjectName("pushProgramar")
        self.gridLayout.addWidget(self.pushProgramar, 8, 0, 1, 1)
        self.pushCopiar = QtWidgets.QPushButton(self.centralwidget)
        self.pushCopiar.setObjectName("pushCopiar")
        self.gridLayout.addWidget(self.pushCopiar, 9, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelDestino = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDestino.sizePolicy().hasHeightForWidth())
        self.labelDestino.setSizePolicy(sizePolicy)
        self.labelDestino.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelDestino.setObjectName("labelDestino")
        self.gridLayout_2.addWidget(self.labelDestino, 2, 0, 1, 1)
        self.labelOrigen = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelOrigen.sizePolicy().hasHeightForWidth())
        self.labelOrigen.setSizePolicy(sizePolicy)
        self.labelOrigen.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelOrigen.setObjectName("labelOrigen")
        self.gridLayout_2.addWidget(self.labelOrigen, 0, 0, 1, 1)
        self.toolDestino = QtWidgets.QToolButton(self.groupBox)
        self.toolDestino.setObjectName("toolDestino")
        self.gridLayout_2.addWidget(self.toolDestino, 2, 2, 1, 1)
        self.lineOrigen = QtWidgets.QLineEdit(self.groupBox)
        self.lineOrigen.setObjectName("lineOrigen")
        self.gridLayout_2.addWidget(self.lineOrigen, 0, 1, 1, 1)
        self.toolOrigen = QtWidgets.QToolButton(self.groupBox)
        self.toolOrigen.setObjectName("toolOrigen")
        self.gridLayout_2.addWidget(self.toolOrigen, 0, 2, 1, 1)
        self.lineDestino = QtWidgets.QLineEdit(self.groupBox)
        self.lineDestino.setObjectName("lineDestino")
        self.gridLayout_2.addWidget(self.lineDestino, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 291, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineOrigen, self.toolOrigen)
        MainWindow.setTabOrder(self.toolOrigen, self.lineDestino)
        MainWindow.setTabOrder(self.lineDestino, self.toolDestino)
        MainWindow.setTabOrder(self.toolDestino, self.radioDiario)
        MainWindow.setTabOrder(self.radioDiario, self.timeDiario)
        MainWindow.setTabOrder(self.timeDiario, self.radioCada)
        MainWindow.setTabOrder(self.radioCada, self.timeCada)
        MainWindow.setTabOrder(self.timeCada, self.pushProgramar)
        MainWindow.setTabOrder(self.pushProgramar, self.pushCopiar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BackUp La Bomba"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Diagrama de copiado"))
        self.radioCada.setText(_translate("MainWindow", "Todo el tiempo cada:"))
        self.radioDiario.setText(_translate("MainWindow", "Todos los días a las:"))
        self.pushProgramar.setText(_translate("MainWindow", "Programar"))
        self.pushCopiar.setText(_translate("MainWindow", "Copiar"))
        self.groupBox.setTitle(_translate("MainWindow", "Archivos a asegurar"))
        self.labelDestino.setText(_translate("MainWindow", "Destino:"))
        self.labelOrigen.setText(_translate("MainWindow", "Origen:"))
        self.toolDestino.setText(_translate("MainWindow", "..."))
        self.toolOrigen.setText(_translate("MainWindow", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

