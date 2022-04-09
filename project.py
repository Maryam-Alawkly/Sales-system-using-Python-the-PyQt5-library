#--------------------------------------------------------Packge---------------------------------------------------------
#=======================================================================================================================
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from main import *
from Login import *
from newUser import *
import  sys
import sqlite3
# ======================================================================================================================


# ======================================================================================================================
#--------------------------------------------------------Databace-------------------------------------------------------

db = sqlite3.connect('data.db')
cr = db.cursor()
#Basic Table : ---------------------------------------------------------------------------------------------------------
cr.execute("CREATE TABLE if not exists Item(ID INTEGER PRIMARY KEY ,Name STRING,Quantity INTEGER,Price float)")
db.commit()

#Invoice Tables : ------------------------------------------------------------------------------------------------------
cr.execute("CREATE TABLE if not exists Temp(ID INTEGER PRIMARY KEY,Name STRING,Quantity INTEGER,Price float,amount float)")
db.commit()

#Admin Table : ---------------------------------------------------------------------------------------------------------

cr.execute("CREATE TABLE if not exists Admin(password INTEGER PRIMARY KEY ,userName STRING)")
db.commit()

#Users Table : ---------------------------------------------------------------------------------------------------------
cr.execute("CREATE TABLE if not exists User(password INTEGER PRIMARY KEY ,userName STRING)")
db.commit()

# ======================================================================================================================



# ======================================================================================================================
#-----------------------------------------------Gloable Variable & Function---------------------------------------------
userName = ''

def showPopup(text, titel=""):
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("{}".format(titel))
    msg.setText("{}".format(text))
    msg.exec_()
# ======================================================================================================================



# ======================================================================================================================
#----------------------------------------------------Class Login Page---------------------------------------------------
class Login(QMainWindow, Ui_Login):
    switch_project = QtCore.pyqtSignal()
    switch_new_user = QtCore.pyqtSignal()
    # ==================================================================================================================
    # --------------------------------------------------Validating User Data--------------------------------------------
    def checkUser(self):
        global userName #to change the value of the previous variable
        try:
            Name = self.user.text()
            Number = self.password.text()

            cr.execute("SELECT * FROM Admin WHERE password = (?) and userName = (?);", (Number,Name))
            dataAdmin = cr.fetchone()
            cr.execute("SELECT * FROM User WHERE password = (?) and userName = (?);", (Number, Name))
            dataUser = cr.fetchone()


            if (dataAdmin is None) and (dataUser is None):
                showPopup(text="اسم المستخدم او كلمة المرور غير صحيحة", titel="خطأ")
            else:
                showPopup(text="تم تسجيل الدخول", titel="مرحبا بك")
                userName = Name
                self.switch_project.emit()
        except Exception as error:
            print(error)

    def newUserButtun(self):
        self.switch_new_user.emit()
    # ==================================================================================================================



    # ==================================================================================================================
    # ---------------------------------------------Init Function & Connections------------------------------------------
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.ok.clicked.connect(self.checkUser)
        self.newAccountBtn.clicked.connect(self.newUserButtun)
    # ==================================================================================================================
# ======================================================================================================================



# ======================================================================================================================
#----------------------------------------------------Class New User Page------------------------------------------------
class new_User(QMainWindow, Ui_newUser):
    switch_login = QtCore.pyqtSignal()
    def newUser(self):
        try:
            Number = self.adminpassword.text()
            newName = self.NameText.text()
            newPassword = self.passwordText.text()

            cr.execute("SELECT * FROM Admin WHERE password = (?);", (Number,))
            dataItem = cr.fetchone()

            if dataItem is None:
                showPopup(text="رقم المدير غير صحيح", titel="خطأ")
            else:
                try:
                    cr.execute("SELECT * FROM User WHERE password = (?);", (newPassword,))
                    dataItem = cr.fetchone()

                    if dataItem is not None:
                        showPopup(text="ادخل كلمة سر قوية", titel="خطأ")
                    else:
                        try:
                            cr.execute("INSERT into User(password,userName) VALUES (?,?);", (newPassword, newName))
                            db.commit()
                            showPopup(text="تم انشاء الحساب بنجاح", titel="انشاء حساب")
                            self.switch_login.emit()
                        except Exception as error:
                            print(error)
                            showPopup(text="لم يتم انشاء الحساب", titel="خطأ")
                except Exception as error:
                    print(error)
                    cr.execute("INSERT into User(password,userName) VALUES (?,?);", (newPassword, newName))
                    db.commit()
                    showPopup(text="تم انشاء الحساب بنجاح", titel="انشاء حساب")

        except Exception as error:
            print(error)
            showPopup(text="تأكد من صحة المدخلات", titel="خطأ")

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.newAccount.clicked.connect(self.newUser)
# ======================================================================================================================



# ======================================================================================================================
#------------------------------------------------------Class Main Page--------------------------------------------------
class Project(QMainWindow,Ui_MainWindow):
    switch_login = QtCore.pyqtSignal()
    # ==================================================================================================================
    # -----------------------------------------------------Add a Product------------------------------------------------
    def addItem(self):
        try:
            Name = self.name.text()
            Number = self.number.text()
            Quantity = self.quantity.text()
            Price = self.price.text()
            Price = float(Price)
            Quantity = int(Quantity)
            Number = int(Number)

            try:
                cr.execute("SELECT * FROM Item WHERE ID = (?);", (Number,))
                dataItem = cr.fetchone()

                if dataItem[0] == Number:
                    showPopup(text="رقم المنتج موجود مسبقا", titel="خطأ")
                else:
                    try:
                        cr.execute("INSERT into Item(ID,Name,Quantity,Price) VALUES (?,?,?,?);",(Number, Name, Quantity, Price))
                        db.commit()
                        showPopup(text="تم اضافة الحقول", titel="اضافة عنصر")
                    except Exception as error:
                        print(error)
            except Exception as error:
                print(error)
                cr.execute("INSERT into Item(ID,Name,Quantity,Price) VALUES (?,?,?,?);",
                           (Number, Name, Quantity, Price))
                db.commit()
                showPopup(text="تم اضافة الحقول", titel="اضافة عنصر")

        except Exception as error:
            print(error)
            showPopup(text="تأكد من صحة البيانات",titel="خطأ")
    # ==================================================================================================================



    # ==================================================================================================================
    # -------------------------------------------------Search on Product------------------------------------------------
    def searchItem(self):
        idItem = self.idItem.text()
        try:
            cr.execute("SELECT * FROM Item WHERE ID = (?);", (idItem,))
            dataItem = cr.fetchone()
            self.nameEdit.setText(dataItem[1])
            self.quantityEdit.setText(str(dataItem[2]))
            self.priceEdit.setText(str(dataItem[3]))
        except Exception as error:
            print(error)
            showPopup(text="العنصر غير موجود", titel="بحث")
    # ==================================================================================================================



    # ==================================================================================================================
    # ----------------------------------------------------Edit a Product------------------------------------------------
    def editItem(self):
        ID = self.idItem.text()
        Name = self.nameEdit.text()
        Quantity = self.quantityEdit.text()
        Price = self.priceEdit.text()
        Price = float(Price)
        Quantity = int(Quantity)
        try:
            cr.execute("UPDATE Item SET Name = (?),Quantity = (?),Price = (?) Where ID=(?);", (Name, Quantity, Price, ID))
            db.commit()
            showPopup(text="تم تعديل الحقول ", titel="تعديل عنصر")
            self.clearEditAndRemove()
        except Exception as error:
            print(error)
    # ==================================================================================================================



    # ==================================================================================================================
    # --------------------------------------------------Delete a Product------------------------------------------------
    def deleteI(self):
        ID = self.idItem.text()
        Name = self.nameEdit.text()
        Quantity = self.quantityEdit.text()
        Price = self.priceEdit.text()
        Price = float(Price)
        Quantity = int(Quantity)
        try:
            cr.execute("DELETE FROM Item Where ID=(?);", (ID,))
            db.commit()
            showPopup(text="تم حذف الحقول ", titel="حذف عنصر")
            self.clearEditAndRemove()
        except Exception as error:
            print(error)
    # ==================================================================================================================



    # ==================================================================================================================
    # -----------------------------------------------------View a Produc------------------------------------------------
    def showAll(self):
        fetched = cr.execute("SELECT * FROM Item")
        self.view.setRowCount(0)
        for row_number, row_data in enumerate(fetched):
            self.view.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.view.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    # ==================================================================================================================



    # ==================================================================================================================
    # ---------------------------------------------View Products in the Invoice-----------------------------------------
    def loadItem(self):
        fetched = cr.execute("SELECT * FROM Temp")
        self.table.setRowCount(0)
        totalQuantity = 0
        totalamount = 0
        DateTime = time.asctime()

        for row_number, row_data in enumerate(fetched):
            self.table.insertRow(row_number)
            totalQuantity += int(row_data[2])
            totalamount += float(row_data[4])
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        self.total.setText(str(totalamount))
        self.count.setText(str(totalQuantity))
        self.dateTimeL.setText(str(DateTime))
        self.UserL.setText(str(userName))
    # ==================================================================================================================



    # ==================================================================================================================
    # ---------------------------------------------------Inventory Run Out----------------------------------------------
    def checkQuantity(self):
        try:
            check = 0
            check = float(check)
            cr.execute("DELETE FROM Item Where Quantity=(?);",(check,))
            db.commit()
        except Exception as error:
            print(error)
    # ==================================================================================================================



    # ==================================================================================================================
    # ---------------------------------------------------Sale of a Product----------------------------------------------
    def salesItems(self):
        ID = self.idItemtable.text()
        Quantity = self.quL.text()
        cr.execute("SELECT Name,Quantity,Price FROM Item WHERE ID = (?);", (ID,))
        dataItem = cr.fetchone()
        Quantity = int(Quantity)
        Name = dataItem[0]
        basicQuantity = int(dataItem[1])
        newQuantity = int(basicQuantity-Quantity)
        if newQuantity >= 0:
            Price = float(dataItem[2])
            ID = int(ID)
            amount = float(Quantity*Price)
            cr.execute("UPDATE Item SET Quantity = (?) Where ID=(?);", (newQuantity, ID))
            db.commit()

            try:
                cr.execute("INSERT into Temp(ID,Name,Quantity,Price,amount) VALUES (?,?,?,?,?);", (ID, Name, Quantity, Price,amount))
                db.commit()
            except Exception as error:
                print(error)
            self.loadItem()
            self.checkQuantity()
        else:
            quantityNow = basicQuantity
            quantityNow = "الكميه المتوفره حالياً ",str(quantityNow)
            showPopup(text=quantityNow,titel="تنبيه")


    # ==================================================================================================================



    # ==================================================================================================================
    # ---------------------------------------------------Deleat a Invoice-----------------------------------------------
    def drop(self):
        cr.execute('drop table if exists Temp')
        db.commit()
        cr.execute("CREATE TABLE if not exists Temp (ID INTEGER PRIMARY KEY,Name STRING,Quantity INTEGER,Price float,amount float)")
        db.commit()
        self.table.setRowCount(0)
        self.total.setText("")
        self.count.setText("")
        self.idItemtable.setText("")
        self.quL.setText("")
        self.dateTimeL.setText("")
    # ==================================================================================================================



    # ==================================================================================================================
    # ---------------------------------------------------Clear Line Text----------------------------------------------

    def clearAdd(self):
        self.name.setText("")
        self.number.setText("")
        self.quantity.setText("")
        self.price.setText("")

    def clearEditAndRemove(self):
        self.nameEdit.setText("")
        self.idItem.setText("")
        self.quantityEdit.setText("")
        self.priceEdit.setText("")
    # ==================================================================================================================



    # ==================================================================================================================
    # ---------------------------------------------Init Function & Connections------------------------------------------
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        # ==============================================================================================================
        # ---------------------------------------------------Connections------------------------------------------------
        self.search.clicked.connect(self.searchItem)
        self.edit.clicked.connect(self.editItem)
        self.clear.clicked.connect(self.clearAdd)
        self.clearEdit.clicked.connect(self.clearEditAndRemove)
        self.add.clicked.connect(self.addItem)
        self.deleteItem.clicked.connect(self.deleteI)
        self.searchtable.clicked.connect(self.salesItems)
        self.printInvoice.clicked.connect(self.drop)
        self.showA.clicked.connect(self.showAll)
        # ==============================================================================================================
# ======================================================================================================================


# ======================================================================================================================
#----------------------------------------------------Class Control Pages------------------------------------------------
class switchBetweenPages:
    def loginPage(self):
        self.login.switch_project.connect(self.showProject)
        self.login.switch_new_user.connect(self.newUserFun)
        self.login.show()
        self.newU.close()

    def newUserFun(self):
        self.newU.switch_login.connect(self.loginPage)
        self.login.close()
        self.newU.show()

    def showProject(self):
        self.project.switch_login.connect(self.loginPage)
        self.login.close()
        self.project.show()

    def __init__(self):
        self.project = Project()
        self.login = Login()
        self.newU = new_User()
# ======================================================================================================================

#global function
def Run():
    application = QtWidgets.QApplication(sys.argv)
    switchBtwPages = switchBetweenPages()
    switchBtwPages.loginPage()

    sys.exit(application.exec_())

if __name__ == "__main__":
    Run()
