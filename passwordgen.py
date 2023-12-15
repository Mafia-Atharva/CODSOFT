from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from random import randint
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Password Generator")
        width=600
        height=600
        self.setFixedHeight(height)
        self.setFixedWidth(width)
        
        #user input box
        self.input=QLineEdit(self)
        self.input.setGeometry(150,80,300,30)
        self.input.setAlignment(Qt.AlignCenter)

        #labels
        self.elabel = QLabel("Enter password length",self)
        self.elabel.setGeometry(150,30,300,35)
        self.ilabel=QLabel("Include: ",self)
        self.ilabel.setGeometry(150,120,115,40)
        self.plabel = QLabel("", self)
        self.plabel.setGeometry(50, 320, 500, 40)
        self.plabel.setMinimumSize(self.sizeHint())
        self.plabel.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.elabel.show()
        self.ilabel.show()

        #checkboxes
        self.CLcb = QCheckBox("Capital Letters",self)
        self.CLcb.setGeometry(270,130,110,20)
        self.SLcb = QCheckBox("Small Letters",self)
        self.SLcb.setGeometry(270,160,110,20)
        self.Ncb = QCheckBox("Numbers",self)
        self.Ncb.setGeometry(270,190,110,20)
        self.SScb = QCheckBox("Special symbols",self)
        self.SScb.setGeometry(270,210,130,40)

        #buttons
        self.submitbtn= QPushButton("Submit",self)
        self.submitbtn.setGeometry(150,270,250,40)
        self.submitbtn.setToolTip("Click to submit")
        self.submitbtn.clicked.connect(self.generate)
        self.copybtn = QPushButton("Copy Password",self)
        self.copybtn.clicked.connect(self.copyPass)
        self.copybtn.setGeometry(150,410,250,40)
        self.copybtn.hide()

    @pyqtSlot()
    def generate(self):
        Cletters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        Sletters="abcdefghijklmnopqrstuwxyz"
        numbers="1234567890"
        Specials="!@#$%^&*()+/"
        Chars=[]
        password=""
        if(self.CLcb.isChecked()): Chars += Cletters
        if(self.SLcb.isChecked()): Chars += Sletters
        if(self.Ncb.isChecked()): Chars += numbers
        if(self.SScb.isChecked()): Chars += Specials

         
        if(self.input.text()==''):
            return
        pwlength =int(self.input.text())
        for _ in range(pwlength):
            password += Chars[randint(0,len(Chars)-1)]

        self.plabel.setText(f"Password: {password}")
        self.plabel.show()
        self.copybtn.show()

    @pyqtSlot()
    def copyPass(self):
        clipboard=QApplication.clipboard()
        clipboard.setText(self.plabel.text().split(":")[1].strip())
        QMessageBox.information(self, "Password Copied", "Password copied to clipboard.")        

app=QApplication(sys.argv)
app.setStyleSheet("QLabel{font-size: 18pt;} QLineEdit{border-radius: 10px; border: 1px solid black;}")
window = Window()
window.show()

sys.exit(app.exec())