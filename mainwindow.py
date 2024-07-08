
from PySide6.QtCore import Qt
from PySide6 import QtGui
from PySide6.QtWidgets import QMainWindow, QTreeWidgetItem, QFileDialog, QStatusBar, QMessageBox, QApplication, QInputDialog, QLineEdit
from ui_mainwindow import Ui_MainWindow
import os
from PyPDF2 import PdfReader
import pytesseract
from PIL import Image
import io
import pyodbc

class MainWindow(QMainWindow, Ui_MainWindow):
    def on_item_clicked(self, item, column):
        new_name, ok = QInputDialog.getText(self, "Input Dialog", "Enter new name                                                                                     ", text = self.tree_payments.currentItem().text(1))
        if ok:
            item.setText(1, new_name)

    def generatePaymentName(self, filePath):
        pytesseract.pytesseract.tesseract_cmd=r'C:\\Users\\' + os.getlogin() + r'\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
        
        with open(filePath, 'rb') as file:
            reader = PdfReader(file)
            first_page = reader.pages[0]
            xObject = first_page['/Resources']['/XObject'].get_object()
            for obj in xObject:
                if xObject[obj]['/Subtype'] == '/Image':
                    size = (xObject[obj])['/Width'], xObject[obj]['/Height']
                    data = xObject[obj].get_data()
                    image = Image.open(io.BytesIO(data))

                    #Crop image to the top 1/4. This is to reduce the time of OCR
                    width, height = image.size
                    #image.crop((left, top, right, bottom))... for reference
                    top_third = image.crop((width * 0.6,0,width, height/4))

                    text = pytesseract.image_to_string(top_third)
                  #  print (text)

            text = text[text.find('PAYMENT VOUCHER')+16:]
            loc = text.find("PV No: ")+7
            tempStrip = text[loc:loc + 20]
         #   print ("tempStrip is: " + tempStrip)
            Reference = tempStrip[0:tempStrip.find('\n',1)]
            dashPosition = Reference.find(" - ")+3
            pvNumber = Reference[dashPosition:]

            try:
                pvNumber = int(pvNumber)
        #        print (f"Payment Voucher number is: {pvNumber}")
            except:
                return os.path.basename(file.name)

            else:
                if Reference[0:3] == "BMK":
                    paymentAccount = 4
                elif Reference[0:3] == "BUK":
                    paymentAccount = 3
                elif Reference[0:2] == "BM":
                    paymentAccount = 2
                elif Reference[0:2] == "BU":
                    paymentAccount = 1
                conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=M:\Innovations\smartPV.accdb')
                cursor = conn.cursor()
                testout = cursor.execute(f'SELECT account_name, amount from payments WHERE pv_number = {pvNumber} AND payment_account_id = {paymentAccount}')
               # print("output is below: ")
                output = testout.fetchall()[0]
                testout.close()
                beneficiary = output[0]
             #   print (beneficiary)
                #remove common special characters in file name
                beneficiary = beneficiary.replace("/","")
                beneficiary = beneficiary.replace(":","")
                beneficiary = beneficiary.replace("\\","")

        #     print ("Beneficiary is: " + beneficiary)
                amount = output[1]
                #remove a new line character \n if it is in the amount string
                if Reference[0:2] == "BU":
                    amount = "USD " + f'{amount*1:.2f}'
                else:
                    amount = "MVR " + f'{amount*1:.2f}'
            #  print (Reference, beneficiary, amount)
            

        return Reference + " " + beneficiary + " " + str(amount) + ".pdf"

    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app

        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.sourceDir = "samples/"
        self.f = []
        self.n = []
        self.tree_payments.setColumnWidth(0,370)
        self.btn_rename.clicked.connect(self.renameFiles)
        self.btn_locate.clicked.connect(self.locateFiles)
        #Connect menu actions
        self.actionQuit.triggered.connect(self.quit)
        self.actionAbout.triggered.connect(self.about)
        self.actionAbout_Qt.triggered.connect(self.aboutQt)
        self.tree_payments.itemClicked.connect(self.on_item_clicked)

    def renameFiles(self):
        #get amended names in treeview object and feed it to self.n array as final file names are stored in self.n
        for i in range(self.tree_payments.topLevelItemCount()):
            item = self.tree_payments.topLevelItem(i)
            self.n[i] = item.text(1)
        #    print (item.text(1))

        totalFiles = len(self.f)
        renameCount = 0
        for fl in self.f:
            #Check if current file name is different from generated payment name
            if not fl == self.n[self.f.index(fl)]:
                #if there is an arror during renaming, if the user choses Retry, keep showing the dialog box. If the user choses Cancel, move to next file
                while True:
                    try:
                        os.rename(self.sourceDir + "/" + fl, self.sourceDir + "/" + self.n[self.f.index(fl)])
                    except Exception as e:
                        ret = QMessageBox.critical(self,"Error!", str(e),QMessageBox.Retry | QMessageBox.Cancel)
                        if ret == QMessageBox.Cancel:
                            break
                    else:
                        self.statusBar.showMessage(f"Renaming {self.f.index(fl)+1} of {totalFiles} files...")
                        renameCount += 1
                        break
        

          #  print(self.tree_payments.childAt(fl,1))
        #Clear list of files and generated file names from memory
        self.statusBar.showMessage(f"Successfully renamed {renameCount} of {len(self.f)} files")
        self.clearComponents()
        
    def locateFiles(self):
        #clear contents of file name array and payment name array i.e self.f and self.n
        self.clearComponents()

        fArray = QFileDialog.getOpenFileNames(self, "Select scanned files",self.sourceDir,"PDF Files (*.pdf)")
        #get source directory from the first element in fArray
        self.sourceDir = os.path.dirname(os.path.abspath(fArray[0][0]))
     #   print(self.sourceDir)

        #get file names of selected files
        for fileName in fArray[0]:
            self.f.append(os.path.basename(fileName))

        #add selected file names and processed file names to treeview
        fileCount = len(self.f)
        for i in range(0, fileCount):
            self.statusBar.showMessage(f"Analyzing {i + 1} of {fileCount} files")
            QApplication.processEvents() # Process pending events to update GUI.. Specifically the status bar.
            paymentName = self.generatePaymentName(self.sourceDir + r"\\" + self.f[i])
            itm = QTreeWidgetItem(self.tree_payments,[self.f[i], paymentName])
            self.n.append(paymentName)
        self.statusBar.showMessage(f"{len(self.f)} files loaded")

    def clearComponents(self):
        self.f.clear()
        self.n.clear()
        self.tree_payments.clear()

    #simple functions for menu bar
    def quit(self):
        self.app.quit()
    def about(self):
        QMessageBox.information(self,"About Payment Renamer", "Created by Ameen Waheed for convenient renaming of Payment Vouchers in Oaga Art Resort")
    def aboutQt(self):
        QApplication.aboutQt()

        