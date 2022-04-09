# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("mainIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(6, 9, 791, 581))
        self.tabWidget.setStyleSheet("color: rgb(151, 0, 111);\n"
"background-color: rgb(255, 255, 255);")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(130, 130, 521, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(151, 0, 111);\n"
"border-color: rgb(151, 0, 111);\n"
"padding : 2px;")
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 1, 1, 1)
        self.nameL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.nameL.setStyleSheet("color: rgb(151, 0, 111);\n"
"background-color: rgb(255, 255, 255);")
        self.nameL.setAlignment(QtCore.Qt.AlignCenter)
        self.nameL.setObjectName("nameL")
        self.gridLayout.addWidget(self.nameL, 0, 2, 1, 1)
        self.number = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.number.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(151, 0, 111);\n"
"border-color: rgb(151, 0, 111);\n"
"padding : 2px;")
        self.number.setObjectName("number")
        self.gridLayout.addWidget(self.number, 2, 1, 1, 1)
        self.price = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.price.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(151, 0, 111);\n"
"border-color: rgb(151, 0, 111);\n"
"padding : 2px;")
        self.price.setObjectName("price")
        self.gridLayout.addWidget(self.price, 4, 1, 1, 1)
        self.quantityL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.quantityL.setStyleSheet("color: rgb(151, 0, 111);\n"
"background-color: rgb(255, 255, 255);")
        self.quantityL.setAlignment(QtCore.Qt.AlignCenter)
        self.quantityL.setObjectName("quantityL")
        self.gridLayout.addWidget(self.quantityL, 3, 2, 1, 1)
        self.priceL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.priceL.setStyleSheet("color: rgb(151, 0, 111);\n"
"background-color: rgb(255, 255, 255);")
        self.priceL.setAlignment(QtCore.Qt.AlignCenter)
        self.priceL.setObjectName("priceL")
        self.gridLayout.addWidget(self.priceL, 4, 2, 1, 1)
        self.quantity = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.quantity.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(151, 0, 111);\n"
"border-color: rgb(151, 0, 111);\n"
"padding : 2px;")
        self.quantity.setObjectName("quantity")
        self.gridLayout.addWidget(self.quantity, 3, 1, 1, 1)
        self.numberL = QtWidgets.QLabel(self.gridLayoutWidget)
        self.numberL.setStyleSheet("color: rgb(151, 0, 111);\n"
"background-color: rgb(255, 255, 255);")
        self.numberL.setAlignment(QtCore.Qt.AlignCenter)
        self.numberL.setObjectName("numberL")
        self.gridLayout.addWidget(self.numberL, 2, 2, 1, 1)
        self.clear = QtWidgets.QPushButton(self.tab)
        self.clear.setGeometry(QtCore.QRect(270, 390, 121, 24))
        self.clear.setStyleSheet("background-color: rgb(151, 0, 111);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Bernard MT Condensed\";\n"
"")
        self.clear.setObjectName("clear")
        self.boxAdd = QtWidgets.QLabel(self.tab)
        self.boxAdd.setGeometry(QtCore.QRect(90, 90, 600, 361))
        self.boxAdd.setStyleSheet("color: rgb(151, 0, 111);")
        self.boxAdd.setFrameShape(QtWidgets.QFrame.Box)
        self.boxAdd.setText("")
        self.boxAdd.setObjectName("boxAdd")
        self.addL = QtWidgets.QLabel(self.tab)
        self.addL.setGeometry(QtCore.QRect(620, 80, 61, 22))
        self.addL.setStyleSheet("color: rgb(151, 0, 111);\n"
"background-color: rgb(255, 255, 255);")
        self.addL.setAlignment(QtCore.Qt.AlignCenter)
        self.addL.setObjectName("addL")
        self.add = QtWidgets.QPushButton(self.tab)
        self.add.setGeometry(QtCore.QRect(392, 390, 121, 24))
        self.add.setStyleSheet("background-color: rgb(151, 0, 111);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Bernard MT Condensed\";\n"
"")
        self.add.setObjectName("add")
        self.boxAdd.raise_()
        self.gridLayoutWidget.raise_()
        self.clear.raise_()
        self.addL.raise_()
        self.add.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.boxEdit = QtWidgets.QLabel(self.tab_2)
        self.boxEdit.setGeometry(QtCore.QRect(90, 80, 600, 400))
        self.boxEdit.setStyleSheet("color: rgb(151, 0, 111);")
        self.boxEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.boxEdit.setText("")
        self.boxEdit.setObjectName("boxEdit")
        self.editL = QtWidgets.QLabel(self.tab_2)
        self.editL.setGeometry(QtCore.QRect(620, 70, 61, 22))
        self.editL.setStyleSheet("color: rgb(151, 0, 111);\n"
"background-color: rgb(255, 255, 255);")
        self.editL.setAlignment(QtCore.Qt.AlignCenter)
        self.editL.setObjectName("editL")
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setGeometry(QtCore.QRect(130, 120, 521, 321))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.search = QtWidgets.QPushButton(self.widget)
        self.search.setStyleSheet("background-color: rgb(151, 0, 111);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Bernard MT Condensed\";\n"
"")
        self.search.setObjectName("search")
        self.gridLayout_2.addWidget(self.search, 0, 0, 1, 1)
        self.enterID = QtWidgets.QLabel(self.widget)
        self.enterID.setStyleSheet("color: rgb(151, 0, 111);\n"
"background-color: rgb(255, 255, 255);")
        self.enterID.setAlignment(QtCore.Qt.AlignCenter)
        self.enterID.setObjectName("enterID")
        self.gridLayout_2.addWidget(self.enterID, 0, 4, 1, 1)
        self.nameLedit = QtWidgets.QLabel(self.widget)
        self.nameLedit.setStyleSheet("color: rgb(151, 0, 111);\n"
"background-color: rgb(255, 255, 255);")
        self.nameLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLedit.setObjectName("nameLedit")
        self.gridLayout_2.addWidget(self.nameLedit, 1, 4, 1, 1)
        self.quantityLedit = QtWidgets.QLabel(self.widget)
        self.quantityLedit.setStyleSheet("color: rgb(151, 0, 111);\n"
"background-color: rgb(255, 255, 255);")
        self.quantityLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.quantityLedit.setObjectName("quantityLedit")
        self.gridLayout_2.addWidget(self.quantityLedit, 2, 4, 1, 1)
        self.priceLedit = QtWidgets.QLabel(self.widget)
        self.priceLedit.setStyleSheet("color: rgb(151, 0, 111);\n"
"background-color: rgb(255, 255, 255);")
        self.priceLedit.setAlignment(QtCore.Qt.AlignCenter)
        self.priceLedit.setObjectName("priceLedit")
        self.gridLayout_2.addWidget(self.priceLedit, 3, 4, 1, 1)
        self.deleteItem = QtWidgets.QPushButton(self.widget)
        self.deleteItem.setStyleSheet("background-color: rgb(151, 0, 111);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Bernard MT Condensed\";\n"
"")
        self.deleteItem.setObjectName("deleteItem")
        self.gridLayout_2.addWidget(self.deleteItem, 4, 2, 1, 1)
        self.edit = QtWidgets.QPushButton(self.widget)
        self.edit.setStyleSheet("background-color: rgb(151, 0, 111);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Bernard MT Condensed\";\n"
"")
        self.edit.setObjectName("edit")
        self.gridLayout_2.addWidget(self.edit, 4, 3, 1, 1)
        self.idItem = QtWidgets.QLineEdit(self.widget)
        self.idItem.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(151, 0, 111);\n"
"border-color: rgb(151, 0, 111);\n"
"padding : 2px;")
        self.idItem.setObjectName("idItem")
        self.gridLayout_2.addWidget(self.idItem, 0, 1, 1, 3)
        self.nameEdit = QtWidgets.QLineEdit(self.widget)
        self.nameEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(151, 0, 111);\n"
"border-color: rgb(151, 0, 111);\n"
"padding : 2px;")
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout_2.addWidget(self.nameEdit, 1, 0, 1, 4)
        self.quantityEdit = QtWidgets.QLineEdit(self.widget)
        self.quantityEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(151, 0, 111);\n"
"border-color: rgb(151, 0, 111);\n"
"padding : 2px;")
        self.quantityEdit.setObjectName("quantityEdit")
        self.gridLayout_2.addWidget(self.quantityEdit, 2, 0, 1, 4)
        self.priceEdit = QtWidgets.QLineEdit(self.widget)
        self.priceEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(151, 0, 111);\n"
"border-color: rgb(151, 0, 111);\n"
"padding : 2px;")
        self.priceEdit.setObjectName("priceEdit")
        self.gridLayout_2.addWidget(self.priceEdit, 3, 0, 1, 4)
        self.clearEdit = QtWidgets.QPushButton(self.widget)
        self.clearEdit.setStyleSheet("background-color: rgb(151, 0, 111);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Bernard MT Condensed\";\n"
"")
        self.clearEdit.setObjectName("clearEdit")
        self.gridLayout_2.addWidget(self.clearEdit, 4, 0, 1, 2)
        self.idItem.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.widget1 = QtWidgets.QWidget()
        self.widget1.setObjectName("widget1")
        self.view = QtWidgets.QTableWidget(self.widget1)
        self.view.setEnabled(False)
        self.view.setGeometry(QtCore.QRect(180, 50, 401, 441))
        self.view.setStyleSheet("color: rgb(151, 0, 111);\n"
"background-color: rgb(255, 255, 255);")
        self.view.setObjectName("view")
        self.view.setColumnCount(4)
        self.view.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.view.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.view.setHorizontalHeaderItem(3, item)
        self.showA = QtWidgets.QPushButton(self.widget1)
        self.showA.setGeometry(QtCore.QRect(180, 510, 401, 22))
        self.showA.setStyleSheet("background-color: rgb(151, 0, 111);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Bernard MT Condensed\";\n"
"")
        self.showA.setObjectName("showA")
        self.tabWidget.addTab(self.widget1, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.idItemtable = QtWidgets.QLineEdit(self.tab_3)
        self.idItemtable.setGeometry(QtCore.QRect(430, 20, 141, 22))
        self.idItemtable.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(151, 0, 111);\n"
"border-color: rgb(151, 0, 111);\n"
"padding : 2px;")
        self.idItemtable.setObjectName("idItemtable")
        self.searchtable = QtWidgets.QPushButton(self.tab_3)
        self.searchtable.setGeometry(QtCore.QRect(140, 20, 61, 22))
        self.searchtable.setStyleSheet("background-color: rgb(151, 0, 111);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Bernard MT Condensed\";\n"
"")
        self.searchtable.setObjectName("searchtable")
        self.enterIDtable = QtWidgets.QLabel(self.tab_3)
        self.enterIDtable.setGeometry(QtCore.QRect(580, 20, 81, 22))
        self.enterIDtable.setStyleSheet("color: rgb(151, 0, 111);\n"
"background-color: rgb(255, 255, 255);")
        self.enterIDtable.setAlignment(QtCore.Qt.AlignCenter)
        self.enterIDtable.setObjectName("enterIDtable")
        self.table = QtWidgets.QTableWidget(self.tab_3)
        self.table.setEnabled(False)
        self.table.setGeometry(QtCore.QRect(150, 100, 501, 381))
        self.table.setStyleSheet("color: rgb(151, 0, 111);\n"
"background-color: rgb(255, 255, 255);")
        self.table.setObjectName("table")
        self.table.setColumnCount(5)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        self.total = QtWidgets.QLineEdit(self.tab_3)
        self.total.setEnabled(False)
        self.total.setGeometry(QtCore.QRect(420, 490, 161, 22))
        self.total.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(151, 0, 111);\n"
"border-color: rgb(151, 0, 111);\n"
"padding : 2px;")
        self.total.setObjectName("total")
        self.totalL = QtWidgets.QLabel(self.tab_3)
        self.totalL.setGeometry(QtCore.QRect(590, 490, 61, 22))
        self.totalL.setStyleSheet("color: rgb(151, 0, 111);\n"
"background-color: rgb(255, 255, 255);")
        self.totalL.setAlignment(QtCore.Qt.AlignCenter)
        self.totalL.setObjectName("totalL")
        self.count = QtWidgets.QLineEdit(self.tab_3)
        self.count.setEnabled(False)
        self.count.setGeometry(QtCore.QRect(150, 490, 171, 22))
        self.count.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(151, 0, 111);\n"
"border-color: rgb(151, 0, 111);\n"
"padding : 2px;")
        self.count.setObjectName("count")
        self.countL = QtWidgets.QLabel(self.tab_3)
        self.countL.setGeometry(QtCore.QRect(330, 490, 71, 22))
        self.countL.setStyleSheet("color: rgb(151, 0, 111);\n"
"background-color: rgb(255, 255, 255);")
        self.countL.setAlignment(QtCore.Qt.AlignCenter)
        self.countL.setObjectName("countL")
        self.printInvoice = QtWidgets.QPushButton(self.tab_3)
        self.printInvoice.setGeometry(QtCore.QRect(140, 530, 521, 22))
        self.printInvoice.setStyleSheet("background-color: rgb(151, 0, 111);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Bernard MT Condensed\";\n"
"")
        self.printInvoice.setObjectName("printInvoice")
        self.qu = QtWidgets.QLabel(self.tab_3)
        self.qu.setGeometry(QtCore.QRect(370, 20, 41, 22))
        self.qu.setStyleSheet("color: rgb(151, 0, 111);\n"
"background-color: rgb(255, 255, 255);")
        self.qu.setAlignment(QtCore.Qt.AlignCenter)
        self.qu.setObjectName("qu")
        self.quL = QtWidgets.QLineEdit(self.tab_3)
        self.quL.setGeometry(QtCore.QRect(210, 20, 151, 22))
        self.quL.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(151, 0, 111);\n"
"border-color: rgb(151, 0, 111);\n"
"padding : 2px;")
        self.quL.setObjectName("quL")
        self.dateTime = QtWidgets.QLabel(self.tab_3)
        self.dateTime.setGeometry(QtCore.QRect(580, 70, 71, 22))
        self.dateTime.setStyleSheet("color: rgb(151, 0, 111);\n"
"background-color: rgb(255, 255, 255);")
        self.dateTime.setAlignment(QtCore.Qt.AlignCenter)
        self.dateTime.setObjectName("dateTime")
        self.dateTimeL = QtWidgets.QLineEdit(self.tab_3)
        self.dateTimeL.setEnabled(False)
        self.dateTimeL.setGeometry(QtCore.QRect(430, 70, 141, 22))
        self.dateTimeL.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(151, 0, 111);\n"
"border-color: rgb(151, 0, 111);\n"
"padding : 2px;")
        self.dateTimeL.setText("")
        self.dateTimeL.setObjectName("dateTimeL")
        self.User = QtWidgets.QLabel(self.tab_3)
        self.User.setGeometry(QtCore.QRect(320, 70, 91, 22))
        self.User.setStyleSheet("color: rgb(151, 0, 111);\n"
"background-color: rgb(255, 255, 255);")
        self.User.setAlignment(QtCore.Qt.AlignCenter)
        self.User.setObjectName("User")
        self.UserL = QtWidgets.QLineEdit(self.tab_3)
        self.UserL.setEnabled(False)
        self.UserL.setGeometry(QtCore.QRect(150, 70, 171, 22))
        self.UserL.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(151, 0, 111);\n"
"border-color: rgb(151, 0, 111);\n"
"padding : 2px;")
        self.UserL.setText("")
        self.UserL.setObjectName("UserL")
        self.boxEdit_2 = QtWidgets.QLabel(self.tab_3)
        self.boxEdit_2.setGeometry(QtCore.QRect(140, 60, 521, 461))
        self.boxEdit_2.setStyleSheet("color: rgb(151, 0, 111);")
        self.boxEdit_2.setFrameShape(QtWidgets.QFrame.Box)
        self.boxEdit_2.setText("")
        self.boxEdit_2.setObjectName("boxEdit_2")
        self.boxEdit_2.raise_()
        self.idItemtable.raise_()
        self.searchtable.raise_()
        self.enterIDtable.raise_()
        self.table.raise_()
        self.total.raise_()
        self.totalL.raise_()
        self.count.raise_()
        self.countL.raise_()
        self.printInvoice.raise_()
        self.qu.raise_()
        self.quL.raise_()
        self.dateTime.raise_()
        self.dateTimeL.raise_()
        self.User.raise_()
        self.UserL.raise_()
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "منظومة مبيعات"))
        self.nameL.setText(_translate("MainWindow", "اسم المنتج :"))
        self.quantityL.setText(_translate("MainWindow", "كمية المنتج :"))
        self.priceL.setText(_translate("MainWindow", "سعر المنتج :"))
        self.numberL.setText(_translate("MainWindow", "رقم المنتج :"))
        self.clear.setText(_translate("MainWindow", "إلغاء"))
        self.addL.setText(_translate("MainWindow", "اضافة منتج"))
        self.add.setText(_translate("MainWindow", "إضافة"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "اضافة منتج"))
        self.editL.setText(_translate("MainWindow", "تعديل منتج"))
        self.search.setText(_translate("MainWindow", "بحث"))
        self.enterID.setText(_translate("MainWindow", "ادخل رقم المنتج :"))
        self.nameLedit.setText(_translate("MainWindow", "اسم المنتج :"))
        self.quantityLedit.setText(_translate("MainWindow", "كمية المنتج :"))
        self.priceLedit.setText(_translate("MainWindow", "سعر المنتج :"))
        self.deleteItem.setText(_translate("MainWindow", "حذف"))
        self.edit.setText(_translate("MainWindow", "تعديل"))
        self.clearEdit.setText(_translate("MainWindow", "إلغاء"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "تعديل / حذف منتج"))
        item = self.view.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "رقم المنتج"))
        item = self.view.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "اسم المنتج"))
        item = self.view.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "كمية المنتج"))
        item = self.view.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "سعر المنتج"))
        self.showA.setText(_translate("MainWindow", "عرض الكل"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget1), _translate("MainWindow", "عرض"))
        self.searchtable.setText(_translate("MainWindow", "بحث"))
        self.enterIDtable.setText(_translate("MainWindow", "ادخل رقم المنتج :"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "رقم المنتج"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "اسم المنتج"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "كمية المنتج"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "سعر المنتج"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "اجمالي السعر"))
        self.totalL.setText(_translate("MainWindow", "الاجمالي :"))
        self.countL.setText(_translate("MainWindow", "عدد الوحدات :"))
        self.printInvoice.setText(_translate("MainWindow", "طباعة الفاتورة"))
        self.qu.setText(_translate("MainWindow", "الكمية :"))
        self.dateTime.setText(_translate("MainWindow", "التاريخ و الوقت :"))
        self.User.setText(_translate("MainWindow", "اسم المستخدم :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "الفاتورة"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
