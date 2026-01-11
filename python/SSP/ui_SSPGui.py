# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SSPGuiMGDHgx.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                          QMetaObject, QObject, QPoint, QRect,
                          QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                         QFont, QFontDatabase, QGradient, QIcon,
                         QImage, QKeySequence, QLinearGradient, QPainter,
                         QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
                             QMenuBar, QPushButton, QSizePolicy, QStatusBar,
                             QTextBrowser, QWidget, QVBoxLayout)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        self.centralWidget = QWidget()
        self.layout = QVBoxLayout(MainWindow)
        self.layout.setObjectName(u"centralwidget")
        self.label = QLabel()
        self.layout.addWidget(self.label)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 301, 41))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
#       self.label.setLayoutDirection(Qt.LeftToRight)
#        self.label.setTextFormat(Qt.PlainText)
        self.textBrowser = QTextBrowser()
        self.layout.addWidget(self.textBrowser)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(0, 0, 431, 61))
        self.textBrowser_2 = QTextBrowser()
        self.layout.addWidget(self.textBrowser_2)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(10, 70, 231, 31))
        self.anzahlRunden = QLabel()
        self.layout.addWidget(self.anzahlRunden)
        self.anzahlRunden.setObjectName(u"anzahlRunden")
        self.anzahlRunden.setGeometry(QRect(260, 76, 141, 21))
        self.letzterZug = QLabel()
        self.layout.addWidget(self.letzterZug)
        self.letzterZug.setObjectName(u"letzterZug")
        self.letzterZug.setGeometry(QRect(10, 120, 401, 31))
        self.textBrowser_3 = QTextBrowser()
        self.layout.addWidget(self.textBrowser_3)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(20, 150, 141, 31))
        self.spielerWins = QLabel()
        self.layout.addWidget(self.spielerWins)
        self.spielerWins.setObjectName(u"spielerWins")
        self.spielerWins.setGeometry(QRect(28, 210, 81, 31))
        self.textBrowser_4 = QTextBrowser()
        self.layout.addWidget(self.textBrowser_4)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(260, 150, 141, 31))
        self.compWins = QLabel()
        self.layout.addWidget(self.compWins)
        self.compWins.setObjectName(u"compWins")
        self.compWins.setGeometry(QRect(280, 210, 81, 31))
        self.zugauswahl = QComboBox()
        self.layout.addWidget(self.zugauswahl)
        self.zugauswahl.addItem("")
        self.zugauswahl.addItem("")
        self.zugauswahl.addItem("")
        self.zugauswahl.setObjectName(u"zugauswahl")
        self.zugauswahl.setGeometry(QRect(140, 260, 121, 22))
        self.spielzugButton = QPushButton()
        self.layout.addWidget(self.spielzugButton)
        self.spielzugButton.setObjectName(u"spielzugButton")
        self.spielzugButton.setGeometry(QRect(290, 260, 101, 24))
        self.resetButton = QPushButton()
        self.layout.addWidget(self.resetButton)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setGeometry(QRect(34, 303, 91, 21))
        self.exitButton = QPushButton()
        self.layout.addWidget(self.exitButton)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(240, 300, 75, 24))
        self.centralWidget.setLayout(self.layout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 440, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.exitButton.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Schere, Stein, Papier!", None))
        self.label.setText("")
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700;\">Aktueller Spielstand</span></p></body></html>", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Runde:</span></p></body></html>", None))
        self.anzahlRunden.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.letzterZug.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Spieler</span></p></body></html>", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Computer</span></p></body></html>", None))
        self.spielerWins.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.compWins.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.zugauswahl.setItemText(0, QCoreApplication.translate("MainWindow", u"Schere", None))
        self.zugauswahl.setItemText(1, QCoreApplication.translate("MainWindow", u"Stein", None))
        self.zugauswahl.setItemText(2, QCoreApplication.translate("MainWindow", u"Papier", None))

        self.spielzugButton.setText(QCoreApplication.translate("MainWindow", u"Spielzug", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.exitButton.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

