import sys
from PyQt5.QtWidgets import* 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title  = "BMI Calculator"
        self.left   = 200
        self.top    = 200
        self.width  = 400
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        mainMenu    = self.menuBar()
        fileMenu    = mainMenu.addMenu("File")

        exitButton = QAction('Exit', self)
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)



        L0 = QLabel(self)
        L0.setText("Body Mass Index (BMI) Calculator") 
        L0.setGeometry(0,80,1000,100)
        L0.move(50,0)
        
        L1 = QLabel(self)
        L1.setText("Enter height:")
        L1.move(30,95)
        
        L2 = QLabel(self)
        L2.setText("Enter weight:")
        L2.move(30,145)

        #create a textbox for input
        self.height = QLineEdit(self)
        self.height.move(100, 100)
        self.height.resize(50, 20)

        self.weight = QLineEdit(self)
        self.weight.move(100, 150)
        self.weight.resize(50, 20)

        #creat a Calculate Button in the window
        self.cal_button = QPushButton("Calculate", self)
        self.cal_button.setToolTip("Calculate result") 
        self.cal_button.move(100, 180)

        

        L3 = QLabel(self)
        L3.setText("kgs")
        L3.move(160,145)

        L4 = QLabel(self)
        L4.setText("meters")
        L4.move(160,95)
        
        # L5 
        #connect button to function on_click
        self.cal_button.clicked.connect(self.on_click)
        
        self.show()

   
    def on_click(self):    
        
        if str(self.weight.text()) =="" and str(self.height.text()) =="":
            QMessageBox.warning(self, 'Oops...No Data to calculate!', "You didn't key in any data at all. Please fill in again! ", QMessageBox.Ok)

        elif str(self.weight.text()) =="" and str(self.height.text()) !="":            
            QMessageBox.warning(self, 'Oops...No Weight value!', "You didn't key in your weight value into the textbox! ", QMessageBox.Ok)

        elif str(self.height.text()) =="" and str(self.weight.text()) !="":            
            QMessageBox.warning(self, 'Oops...No Height value!', "You didn't key in your height value into the textbox! ", QMessageBox.Ok)
       
        else:
            weight = float(self.weight.text())
            height = float(self.height.text())
            if ((weight / (height * height))) < 18.5:

                QMessageBox.information(self, 'Result', "Your BMI result is: " + str('%.2f' %(weight / (height * height))) + "\n Category: Underweight", QMessageBox.Ok)

            
            elif ((weight / (height * height))) < 25 and ((weight / (height * height))) >= 18.5:
                
                QMessageBox.information(self, 'Result', "Your BMI result is: " + str('%.2f' %(weight / (height * height))) + "\n Category: Normal weight", QMessageBox.Ok)


            elif ((weight / (height * height))) < 30 and ((weight / (height * height))) >= 25:
                
                QMessageBox.information(self, 'Result', "Your BMI result is: " + str('%.2f' %(weight / (height * height))) + "\n Category: Overweight", QMessageBox.Ok)

            else:
                QMessageBox.information(self, 'Result', "Your BMI result is: " + str('%.2f' %(weight / (height * height))) + "\n Category: Obesity", QMessageBox.Ok)
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())