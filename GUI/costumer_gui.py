# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'costumer_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CostumerWindow(object):
    def setupUi(self, CostumerWindow):
        CostumerWindow.setObjectName("CostumerWindow")
        CostumerWindow.resize(794, 814)
        CostumerWindow.setStyleSheet("background-color:#F0F0F0;")
        self.tabWidget = QtWidgets.QTabWidget(CostumerWindow)
        self.tabWidget.setGeometry(QtCore.QRect(10, 185, 771, 621))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_Books = QtWidgets.QWidget()
        self.tab_Books.setObjectName("tab_Books")
        self.tableWidget_books = QtWidgets.QTableWidget(self.tab_Books)
        self.tableWidget_books.setGeometry(QtCore.QRect(20, 160, 721, 371))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_books.setFont(font)
        self.tableWidget_books.setStyleSheet("background-color:#FAFAFA")
        self.tableWidget_books.setAutoScrollMargin(20)
        self.tableWidget_books.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_books.setAlternatingRowColors(True)
        self.tableWidget_books.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_books.setGridStyle(QtCore.Qt.CustomDashLine)
        self.tableWidget_books.setObjectName("tableWidget_books")
        self.tableWidget_books.setColumnCount(7)
        self.tableWidget_books.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_books.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_books.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_books.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_books.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_books.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_books.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_books.setHorizontalHeaderItem(6, item)
        self.tableWidget_books.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_books.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_books.horizontalHeader().setHighlightSections(True)
        self.tableWidget_books.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget_books.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_books.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_books.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_books.verticalHeader().setDefaultSectionSize(38)
        self.tableWidget_books.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget_books.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_books.verticalHeader().setStretchLastSection(False)
        self.comboBox_books = QtWidgets.QComboBox(self.tab_Books)
        self.comboBox_books.setGeometry(QtCore.QRect(240, 100, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_books.setFont(font)
        self.comboBox_books.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_books.setStyleSheet("background-color:white")
        self.comboBox_books.setObjectName("comboBox_books")
        self.comboBox_books.addItem("")
        self.comboBox_books.addItem("")
        self.comboBox_books.addItem("")
        self.frame_2 = QtWidgets.QFrame(self.tab_Books)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 741, 561))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("background-color:#F6F8FA;border-radius:0.7em;border :1px solid #DAE5EA;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setMidLineWidth(4)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_reserve = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_reserve.setGeometry(QtCore.QRect(470, 90, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.pushButton_reserve.setFont(font)
        self.pushButton_reserve.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_reserve.setStyleSheet("border-radius:0.4em;border :1px solid #D7DDE3;background-color:#2DA44E;color:white")
        self.pushButton_reserve.setObjectName("pushButton_reserve")
        self.pushButton_borrow = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_borrow.setGeometry(QtCore.QRect(600, 90, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.pushButton_borrow.setFont(font)
        self.pushButton_borrow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_borrow.setStyleSheet("border-radius:0.4em;border :1px solid #D7DDE3;background-color:#2DA44E;color:white")
        self.pushButton_borrow.setObjectName("pushButton_borrow")
        self.label_9 = QtWidgets.QLabel(self.tab_Books)
        self.label_9.setGeometry(QtCore.QRect(30, 100, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color:#F6F8FA")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.line_3 = QtWidgets.QFrame(self.tab_Books)
        self.line_3.setGeometry(QtCore.QRect(220, 70, 321, 16))
        self.line_3.setStyleSheet("background-color:#F6F8FA")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_8 = QtWidgets.QLabel(self.tab_Books)
        self.label_8.setGeometry(QtCore.QRect(40, 40, 681, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color:#F6F8FA")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_error = QtWidgets.QLabel(self.tab_Books)
        self.label_error.setGeometry(QtCore.QRect(20, 540, 711, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_error.setFont(font)
        self.label_error.setStyleSheet("background-color:#F6F8FA;color:red")
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        self.frame_2.raise_()
        self.tableWidget_books.raise_()
        self.comboBox_books.raise_()
        self.label_9.raise_()
        self.line_3.raise_()
        self.label_8.raise_()
        self.label_error.raise_()
        self.tabWidget.addTab(self.tab_Books, "")
        self.tab_My_Books = QtWidgets.QWidget()
        self.tab_My_Books.setObjectName("tab_My_Books")
        self.frame_3 = QtWidgets.QFrame(self.tab_My_Books)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 741, 561))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.frame_3.setFont(font)
        self.frame_3.setStyleSheet("background-color:#F6F8FA;border-radius:0.7em;border :1px solid #D9DFE5;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(2)
        self.frame_3.setMidLineWidth(4)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_return = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_return.setGeometry(QtCore.QRect(610, 90, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.pushButton_return.setFont(font)
        self.pushButton_return.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_return.setStyleSheet("border-radius:0.4em;border :1px solid #D7DDE3;background-color:#2DA44E;color:white")
        self.pushButton_return.setObjectName("pushButton_return")
        self.pushButton_add_days = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_add_days.setGeometry(QtCore.QRect(290, 90, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.pushButton_add_days.setFont(font)
        self.pushButton_add_days.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_add_days.setStyleSheet("border-radius:0.4em;border :1px solid #D7DDE3;background-color:#2DA44E;color:white")
        self.pushButton_add_days.setObjectName("pushButton_add_days")
        self.line_5 = QtWidgets.QFrame(self.tab_My_Books)
        self.line_5.setGeometry(QtCore.QRect(220, 70, 321, 16))
        self.line_5.setStyleSheet("background-color:#F6F8FA")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_13 = QtWidgets.QLabel(self.tab_My_Books)
        self.label_13.setGeometry(QtCore.QRect(40, 40, 681, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color:#F6F8FA")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.tableWidget_my_books = QtWidgets.QTableWidget(self.tab_My_Books)
        self.tableWidget_my_books.setGeometry(QtCore.QRect(20, 160, 721, 371))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_my_books.setFont(font)
        self.tableWidget_my_books.setStyleSheet("background-color:#FAFAFA")
        self.tableWidget_my_books.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget_my_books.setAutoScrollMargin(20)
        self.tableWidget_my_books.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_my_books.setAlternatingRowColors(True)
        self.tableWidget_my_books.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_my_books.setGridStyle(QtCore.Qt.CustomDashLine)
        self.tableWidget_my_books.setObjectName("tableWidget_my_books")
        self.tableWidget_my_books.setColumnCount(7)
        self.tableWidget_my_books.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_my_books.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_my_books.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_my_books.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_my_books.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_my_books.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_my_books.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_my_books.setHorizontalHeaderItem(6, item)
        self.tableWidget_my_books.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_my_books.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_my_books.horizontalHeader().setHighlightSections(True)
        self.tableWidget_my_books.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget_my_books.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_my_books.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_my_books.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_my_books.verticalHeader().setDefaultSectionSize(38)
        self.tableWidget_my_books.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget_my_books.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_my_books.verticalHeader().setStretchLastSection(False)
        self.label = QtWidgets.QLabel(self.tab_My_Books)
        self.label.setGeometry(QtCore.QRect(30, 100, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:#F6F8FA")
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(self.tab_My_Books)
        self.spinBox.setGeometry(QtCore.QRect(170, 100, 111, 40))
        self.spinBox.setStyleSheet("")
        self.spinBox.setMaximum(7)
        self.spinBox.setObjectName("spinBox")
        self.label_error_2 = QtWidgets.QLabel(self.tab_My_Books)
        self.label_error_2.setGeometry(QtCore.QRect(20, 540, 721, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_error_2.setFont(font)
        self.label_error_2.setStyleSheet("background-color:#F6F8FA;color:red")
        self.label_error_2.setText("")
        self.label_error_2.setObjectName("label_error_2")
        self.tabWidget.addTab(self.tab_My_Books, "")
        self.tab_My_Activity = QtWidgets.QWidget()
        self.tab_My_Activity.setObjectName("tab_My_Activity")
        self.label_6 = QtWidgets.QLabel(self.tab_My_Activity)
        self.label_6.setGeometry(QtCore.QRect(40, 30, 681, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color:#F6F8FA")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_My_Activity)
        self.textBrowser.setGeometry(QtCore.QRect(30, 340, 701, 191))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color:white")
        self.textBrowser.setObjectName("textBrowser")
        self.listWidget = QtWidgets.QListWidget(self.tab_My_Activity)
        self.listWidget.setGeometry(QtCore.QRect(30, 80, 701, 191))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.listWidget.setFont(font)
        self.listWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listWidget.setStyleSheet("background-color:white")
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setObjectName("listWidget")
        self.frame = QtWidgets.QFrame(self.tab_My_Activity)
        self.frame.setGeometry(QtCore.QRect(10, 10, 741, 561))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color:#F6F8FA;border-radius:0.7em;border :1px solid #DAE5EA;")
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(4)
        self.frame.setObjectName("frame")
        self.label_7 = QtWidgets.QLabel(self.tab_My_Activity)
        self.label_7.setGeometry(QtCore.QRect(40, 290, 681, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color:#F6F8FA")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.line_2 = QtWidgets.QFrame(self.tab_My_Activity)
        self.line_2.setGeometry(QtCore.QRect(220, 60, 321, 16))
        self.line_2.setStyleSheet("background-color:#F6F8FA")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_4 = QtWidgets.QFrame(self.tab_My_Activity)
        self.line_4.setGeometry(QtCore.QRect(220, 320, 321, 16))
        self.line_4.setStyleSheet("background-color:#F6F8FA")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_error_3 = QtWidgets.QLabel(self.tab_My_Activity)
        self.label_error_3.setGeometry(QtCore.QRect(30, 540, 711, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_error_3.setFont(font)
        self.label_error_3.setStyleSheet("background-color:#F6F8FA;color:red")
        self.label_error_3.setText("")
        self.label_error_3.setObjectName("label_error_3")
        self.frame.raise_()
        self.label_6.raise_()
        self.textBrowser.raise_()
        self.listWidget.raise_()
        self.label_7.raise_()
        self.line_2.raise_()
        self.line_4.raise_()
        self.label_error_3.raise_()
        self.tabWidget.addTab(self.tab_My_Activity, "")
        self.line = QtWidgets.QFrame(CostumerWindow)
        self.line.setGeometry(QtCore.QRect(180, 155, 441, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(CostumerWindow)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 761, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_logo = QtWidgets.QLabel(CostumerWindow)
        self.label_logo.setGeometry(QtCore.QRect(20, 15, 761, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.label_logo.setFont(font)
        self.label_logo.setText("")
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setObjectName("label_logo")

        self.retranslateUi(CostumerWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CostumerWindow)
        CostumerWindow.setTabOrder(self.tabWidget, self.tableWidget_books)
        CostumerWindow.setTabOrder(self.tableWidget_books, self.comboBox_books)
        CostumerWindow.setTabOrder(self.comboBox_books, self.pushButton_reserve)
        CostumerWindow.setTabOrder(self.pushButton_reserve, self.pushButton_borrow)
        CostumerWindow.setTabOrder(self.pushButton_borrow, self.spinBox)
        CostumerWindow.setTabOrder(self.spinBox, self.pushButton_add_days)
        CostumerWindow.setTabOrder(self.pushButton_add_days, self.pushButton_return)
        CostumerWindow.setTabOrder(self.pushButton_return, self.tableWidget_my_books)
        CostumerWindow.setTabOrder(self.tableWidget_my_books, self.listWidget)
        CostumerWindow.setTabOrder(self.listWidget, self.textBrowser)

    def retranslateUi(self, CostumerWindow):
        _translate = QtCore.QCoreApplication.translate
        CostumerWindow.setWindowTitle(_translate("CostumerWindow", "Costumer Partition"))
        self.tableWidget_books.setSortingEnabled(True)
        item = self.tableWidget_books.horizontalHeaderItem(0)
        item.setText(_translate("CostumerWindow", "📕 Name"))
        item = self.tableWidget_books.horizontalHeaderItem(1)
        item.setText(_translate("CostumerWindow", "👩🏻‍🎓 Author"))
        item = self.tableWidget_books.horizontalHeaderItem(2)
        item.setText(_translate("CostumerWindow", "🧾 State"))
        item = self.tableWidget_books.horizontalHeaderItem(3)
        item.setText(_translate("CostumerWindow", "🤙🏻 Reserved"))
        item = self.tableWidget_books.horizontalHeaderItem(4)
        item.setText(_translate("CostumerWindow", "👋🏻 Borrowed"))
        item = self.tableWidget_books.horizontalHeaderItem(5)
        item.setText(_translate("CostumerWindow", "📅 Borrowed"))
        item = self.tableWidget_books.horizontalHeaderItem(6)
        item.setText(_translate("CostumerWindow", "📅 Return"))
        self.comboBox_books.setStatusTip(_translate("CostumerWindow", "Select a book state to show books on table"))
        self.comboBox_books.setItemText(0, _translate("CostumerWindow", "Available"))
        self.comboBox_books.setItemText(1, _translate("CostumerWindow", "Borrowed"))
        self.comboBox_books.setItemText(2, _translate("CostumerWindow", "Reserved"))
        self.pushButton_reserve.setStatusTip(_translate("CostumerWindow", "Click to issue bill ..."))
        self.pushButton_reserve.setText(_translate("CostumerWindow", "Reserve"))
        self.pushButton_borrow.setStatusTip(_translate("CostumerWindow", "Click to issue receipt ..."))
        self.pushButton_borrow.setText(_translate("CostumerWindow", "Borrow"))
        self.label_9.setText(_translate("CostumerWindow", "Books with statement:"))
        self.label_8.setText(_translate("CostumerWindow", "Reserve or borrow the books"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Books), _translate("CostumerWindow", "📚 Books"))
        self.pushButton_return.setStatusTip(_translate("CostumerWindow", "Click to issue receipt ..."))
        self.pushButton_return.setText(_translate("CostumerWindow", "Return"))
        self.pushButton_add_days.setStatusTip(_translate("CostumerWindow", "Click to issue bill ..."))
        self.pushButton_add_days.setText(_translate("CostumerWindow", "Add Days"))
        self.label_13.setText(_translate("CostumerWindow", "Select a book bellow to add extension days to return the book"))
        self.tableWidget_my_books.setSortingEnabled(True)
        item = self.tableWidget_my_books.horizontalHeaderItem(0)
        item.setText(_translate("CostumerWindow", "📕 Name"))
        item = self.tableWidget_my_books.horizontalHeaderItem(1)
        item.setText(_translate("CostumerWindow", "🧾 State"))
        item = self.tableWidget_my_books.horizontalHeaderItem(2)
        item.setText(_translate("CostumerWindow", "📅 Borrowed"))
        item = self.tableWidget_my_books.horizontalHeaderItem(3)
        item.setText(_translate("CostumerWindow", "📅 Return[ed]"))
        item = self.tableWidget_my_books.horizontalHeaderItem(4)
        item.setText(_translate("CostumerWindow", "➕ Extension"))
        item = self.tableWidget_my_books.horizontalHeaderItem(5)
        item.setText(_translate("CostumerWindow", "⏳ Delay"))
        item = self.tableWidget_my_books.horizontalHeaderItem(6)
        item.setText(_translate("CostumerWindow", "💲 Bill"))
        self.label.setText(_translate("CostumerWindow", "Extension Days:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_My_Books), _translate("CostumerWindow", "📖 My Books"))
        self.label_6.setText(_translate("CostumerWindow", "Select a activity bellow to see full description"))
        self.textBrowser.setStatusTip(_translate("CostumerWindow", "Full description of notification"))
        self.textBrowser.setHtml(_translate("CostumerWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.listWidget.setStatusTip(_translate("CostumerWindow", "Select a notification to manage"))
        self.label_7.setText(_translate("CostumerWindow", "Full Description"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_My_Activity), _translate("CostumerWindow", "💼 My Activity"))
        self.label_3.setText(_translate("CostumerWindow", "Costumer Partition"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CostumerWindow = QtWidgets.QDialog()
    ui = Ui_CostumerWindow()
    ui.setupUi(CostumerWindow)
    CostumerWindow.show()
    sys.exit(app.exec_())
