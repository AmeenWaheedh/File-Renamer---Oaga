# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(807, 610)
        icon = QIcon()
        icon.addFile(u":/InWindow.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAbout_Qt = QAction(MainWindow)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_locate = QPushButton(self.centralwidget)
        self.btn_locate.setObjectName(u"btn_locate")
        font = QFont()
        font.setPointSize(13)
        self.btn_locate.setFont(font)

        self.verticalLayout.addWidget(self.btn_locate)

        self.tree_payments = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(1, u"Generated payment name")
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignCenter)
        __qtreewidgetitem.setText(0, u"Current file name")
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter)
        self.tree_payments.setHeaderItem(__qtreewidgetitem)
        self.tree_payments.setObjectName(u"tree_payments")
        self.tree_payments.setAlternatingRowColors(True)
        self.tree_payments.setColumnCount(2)

        self.verticalLayout.addWidget(self.tree_payments)

        self.btn_rename = QPushButton(self.centralwidget)
        self.btn_rename.setObjectName(u"btn_rename")
        self.btn_rename.setFont(font)

        self.verticalLayout.addWidget(self.btn_rename)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 807, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addAction(self.actionAbout_Qt)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Payment Renamer", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.btn_locate.setText(QCoreApplication.translate("MainWindow", u"Step 1: Locate files", None))
        self.btn_rename.setText(QCoreApplication.translate("MainWindow", u"Step 2: Rename files", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

