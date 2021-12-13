from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMainWindow, QFrame, QLabel, QHBoxLayout, QLineEdit, QComboBox
import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QPixmap
import numpy as np
import model
class ModelGui(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.UI()
        self.header()
        self.bodycontent()
        self.framecontent_()
        self.kilom()
        self.fuel_()
        self.sellertype_()
        self.transmission_()
        self.owner_()
        self.mileage_()
        self.engine_()
        self.maxpower_()
        self.seat_()
        self.age_()
        self.predict_()


    def initUI(self):
        self.setWindowTitle('CAR PRICE ESTIMATOR')
        self.setGeometry(300, 200, 445, 1000)

    def UI(self):
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setObjectName("centralWidget")
        self.layvertical = QVBoxLayout(self.centralWidget)
        self.layvertical.setObjectName("layvertical")
    
    def header(self):
        self.frameheader = QFrame(self.centralWidget)
        self.frameheader.setMaximumSize(QtCore.QSize(1515545451, 200))
        self.frameheader.setFrameShape(QFrame.StyledPanel)
        self.frameheader.setFrameShadow(QFrame.Raised)
        self.frameheader.setObjectName("frameheader")
        self.layvertical.addWidget(self.frameheader) 
        self.layvertical2 = QVBoxLayout(self.frameheader)
        self.layvertical2.setObjectName("layvertical2")
        self.title = QLabel(self.frameheader)
        self.title.setText("CAR PRICE ESTIMATOR")
        self.title.setObjectName("title")
        self.title.setFont(QFont("Arial", 20))
        self.title.setStyleSheet("color: #02659D")
        self.layvertical2.addWidget(self.title, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.pixmap = QLabel(self.frameheader)
        self.pixmap.setPixmap(QPixmap("car.png"))
        self.pixmap.setObjectName("pixmap")
        self.layvertical2.addWidget(self.pixmap, 0, QtCore.Qt.AlignHCenter)
    
    def bodycontent(self):
        self.framebody = QFrame(self.centralWidget)
        self.framebody.setFrameShape(QFrame.StyledPanel)
        self.framebody.setFrameShadow(QFrame.Raised)
        self.framebody.setObjectName("framebody")
        self.layvertical.addWidget(self.framebody)
        self.layvertical3 = QVBoxLayout(self.framebody)
        self.layvertical3.setObjectName("layvertical3")

        self.framecontent = QFrame(self.framebody)
        self.framecontent.setFrameShape(QFrame.StyledPanel)
        self.framecontent.setFrameShadow(QFrame.Raised)
        self.framecontent.setObjectName("framecontent")
        self.layvertical3.addWidget(self.framecontent)

        self.frambottom = QFrame(self.framebody)
        self.frambottom.setFrameShape(QFrame.StyledPanel)
        self.frambottom.setFrameShadow(QFrame.Raised)
        self.frambottom.setObjectName("frambottom")
        self.frambottom.setMaximumSize(QtCore.QSize(1515545451, 50))
        self.layvertical3.addWidget(self.frambottom)
        self.complain = QLabel(self.frambottom)
        self.complain.setText("SETUX CORPORATION GROUP")
        self.complain.setObjectName("complain")
        self.complain.setFont(QFont("Arial", 20))
        self.complain.setStyleSheet("color: #02659D")
        self.laybottom = QVBoxLayout(self.frambottom)
        self.laybottom.addWidget(self.complain, 0, QtCore.Qt.AlignHCenter)

    def framecontent_(self):
        
        self.kilometer = QFrame(self.framecontent)
        self.kilometer.setFrameShape(QFrame.StyledPanel)
        self.kilometer.setFrameShadow(QFrame.Raised)
        self.kilometer.setObjectName("kilometer")
        

        self.fuel = QFrame(self.framecontent)
        self.fuel.setFrameShape(QFrame.StyledPanel)
        self.fuel.setFrameShadow(QFrame.Raised)
        self.fuel.setObjectName("fuel")

        self.sellertype = QFrame(self.framecontent)
        self.sellertype.setFrameShape(QFrame.StyledPanel)
        self.sellertype.setFrameShadow(QFrame.Raised)
        self.sellertype.setObjectName("sellertype")


        self.transmission = QFrame(self.framecontent)
        self.transmission.setFrameShape(QFrame.StyledPanel)
        self.transmission.setFrameShadow(QFrame.Raised)
        self.transmission.setObjectName("transmission")

        self.owner = QFrame(self.framecontent)
        self.owner.setFrameShape(QFrame.StyledPanel)
        self.owner.setFrameShadow(QFrame.Raised)
        self.owner.setObjectName("owner")

        self.mileage = QFrame(self.framecontent)
        self.mileage.setFrameShape(QFrame.StyledPanel)
        self.mileage.setFrameShadow(QFrame.Raised)
        self.mileage.setObjectName("mileage")

        self.engine = QFrame(self.framecontent)
        self.engine.setFrameShape(QFrame.StyledPanel)
        self.engine.setFrameShadow(QFrame.Raised)
        self.engine.setObjectName("engine")

        self.power = QFrame(self.framecontent)
        self.power.setFrameShape(QFrame.StyledPanel)
        self.power.setFrameShadow(QFrame.Raised)
        self.power.setObjectName("power")

        self.seat = QFrame(self.framecontent)
        self.seat.setFrameShape(QFrame.StyledPanel)
        self.seat.setFrameShadow(QFrame.Raised)
        self.seat.setObjectName("seat")
        
        self.age = QFrame(self.framecontent)
        self.age.setFrameShape(QFrame.StyledPanel)
        self.age.setFrameShadow(QFrame.Raised)
        self.age.setObjectName("age")

        self.predict = QFrame(self.framecontent)
        self.predict.setFrameShape(QFrame.StyledPanel)
        self.predict.setFrameShadow(QFrame.Raised)
        self.predict.setObjectName("predict")

        
        self.layvertical4 = QVBoxLayout(self.framecontent)
        
        self.list = [self.kilometer, self.fuel, self.sellertype, self.transmission, self.owner, 
                    self.mileage, self.engine, self.power, self.seat, self.age, self.predict]
        
        for i in self.list:
            self.layvertical4.addWidget(i)

    def kilom(self):
        self.layhor1 = QHBoxLayout(self.kilometer)
        self.label = QLabel(self.kilometer)
        self.label.setText("Kilometer")
        self.label.setObjectName("label")
        self.label.setFont(QFont("Arial", 10))
        self.label.setStyleSheet("color: #02659D")
        self.layhor1.addWidget(self.label, 0, QtCore.Qt.AlignLeft)
        self.lineEdit1 = QLineEdit(self.kilometer)
        self.lineEdit1.setObjectName("lineEdit")
        self.lineEdit1.setFont(QFont("Arial", 10))
        self.layhor1.addWidget(self.lineEdit1, 0, QtCore.Qt.AlignHCenter)

    def fuel_(self):
        self.layhor2 = QHBoxLayout(self.fuel)
        self.label = QLabel(self.fuel)
        self.label.setText("Fuel")
        self.label.setObjectName("label")
        self.label.setFont(QFont("Arial", 10))
        self.label.setStyleSheet("color: #02659D")
        self.layhor2.addWidget(self.label, 0, QtCore.Qt.AlignLeft)
        self.combo = QComboBox(self.fuel)
        self.combo.setObjectName("combo")
        self.combo.setFont(QFont("Arial", 10))
        self.fuelitems = {"Petrol": 1, "Diesel": 2, "CNG": 3, "LPG": 4}
        self.combo.addItems(list(self.fuelitems.keys()))
        self.combo.resize(100, 100)
        self.layhor2.addWidget(self.combo, 0, QtCore.Qt.AlignHCenter)

    def sellertype_(self):
        self.layhor3 = QHBoxLayout(self.sellertype)
        self.label = QLabel(self.sellertype)
        self.label.setText("Seller Type")
        self.label.setObjectName("label")
        self.label.setFont(QFont("Arial", 10))
        self.label.setStyleSheet("color: #02659D")
        self.layhor3.addWidget(self.label, 0, QtCore.Qt.AlignLeft)
        self.combo2 = QComboBox(self.sellertype)
        self.combo2.setObjectName("combo")
        self.combo2.setFont(QFont("Arial", 10))
        self.selleritems = {"Individual": 1, "Company": 2}
        self.combo2.addItems(list(self.selleritems.keys()))
        self.combo2.resize(100, 100)
        self.layhor3.addWidget(self.combo2, 0, QtCore.Qt.AlignHCenter)

    def transmission_(self):
        self.layhor4 = QHBoxLayout(self.transmission)
        self.label = QLabel(self.transmission)
        self.label.setText("Transmission")
        self.label.setObjectName("label")
        self.label.setFont(QFont("Arial", 10))
        self.label.setStyleSheet("color: #02659D")
        self.layhor4.addWidget(self.label, 0, QtCore.Qt.AlignLeft)
        self.combo3 = QComboBox(self.transmission)
        self.combo3.setObjectName("combo")
        self.combo3.setFont(QFont("Arial", 10))
        self.transmissionitems = {"Manual": 1, "Automatic": 2}
        self.combo3.addItems(list(self.transmissionitems.keys()))
        self.combo3.resize(100, 100)
        self.layhor4.addWidget(self.combo3, 0, QtCore.Qt.AlignHCenter)

    def owner_(self):
        self.layhor5 = QHBoxLayout(self.owner)
        self.label = QLabel(self.owner)
        self.label.setText("Owner")
        self.label.setObjectName("label")
        self.label.setFont(QFont("Arial", 10))
        self.label.setStyleSheet("color: #02659D")
        self.layhor5.addWidget(self.label, 0, QtCore.Qt.AlignLeft)
        self.combo4 = QComboBox(self.owner)
        self.combo4.setObjectName("combo")
        self.combo4.setFont(QFont("Arial", 10))
        self.owneritems = {"First Owner": 1, "Second Owner": 2, "Third Owner": 3, "Fourth & Above": 4, "Test drive": 5}
        self.combo4.addItems(list(self.owneritems.keys()))
        self.combo.resize(100, 100)
        self.layhor5.addWidget(self.combo4, 0, QtCore.Qt.AlignHCenter)

    def mileage_(self):
        self.layhor6 = QHBoxLayout(self.mileage)
        self.label = QLabel(self.mileage)
        self.label.setText("Mileage")
        self.label.setObjectName("label")
        self.label.setFont(QFont("Arial", 10))
        self.label.setStyleSheet("color: #02659D")
        self.layhor6.addWidget(self.label, 0, QtCore.Qt.AlignLeft)
        self.lineEdit2 = QLineEdit(self.mileage)
        self.lineEdit2.setObjectName("lineEdit")
        self.lineEdit2.setFont(QFont("Arial", 10))
        self.layhor6.addWidget(self.lineEdit2, 0, QtCore.Qt.AlignHCenter)
    
    def engine_(self):
        self.layhor7 = QHBoxLayout(self.engine)
        self.label = QLabel(self.engine)
        self.label.setText("Engine")
        self.label.setObjectName("label")
        self.label.setFont(QFont("Arial", 10))
        self.label.setStyleSheet("color: #02659D")
        self.layhor7.addWidget(self.label, 0, QtCore.Qt.AlignLeft)
        self.lineEdit3 = QLineEdit(self.engine)
        self.lineEdit3.setObjectName("lineEdit")
        self.lineEdit3.setFont(QFont("Arial", 10))
        self.layhor7.addWidget(self.lineEdit3, 0, QtCore.Qt.AlignHCenter)
    
    
    def maxpower_(self):
        self.layhor9 = QHBoxLayout(self.power)
        self.label = QLabel(self.power)
        self.label.setText("Max Power")
        self.label.setObjectName("label")
        self.label.setFont(QFont("Arial", 10))
        self.label.setStyleSheet("color: #02659D")
        self.layhor9.addWidget(self.label, 0, QtCore.Qt.AlignLeft)
        self.lineEdit4 = QLineEdit(self.power)
        self.lineEdit4.setObjectName("lineEdit")
        self.lineEdit4.setFont(QFont("Arial", 10))
        self.layhor9.addWidget(self.lineEdit4, 0, QtCore.Qt.AlignHCenter)
    
    def seat_(self):
        self.layhor10 = QHBoxLayout(self.seat)
        self.label = QLabel(self.seat)
        self.label.setText("Seat")
        self.label.setObjectName("label")
        self.label.setFont(QFont("Arial", 10))
        self.label.setStyleSheet("color: #02659D")
        self.layhor10.addWidget(self.label, 0, QtCore.Qt.AlignLeft)
        self.lineEdit5 = QLineEdit(self.seat)
        self.lineEdit5.setObjectName("lineEdit")
        self.lineEdit5.setFont(QFont("Arial", 10))
        self.layhor10.addWidget(self.lineEdit5, 0, QtCore.Qt.AlignHCenter)

    def age_(self):
        self.layhor11 = QHBoxLayout(self.age)
        self.label = QLabel(self.age)
        self.label.setText("Age")
        self.label.setObjectName("label")
        self.label.setFont(QFont("Arial", 10))
        self.label.setStyleSheet("color: #02659D")
        self.layhor11.addWidget(self.label, 0, QtCore.Qt.AlignLeft)
        self.lineEdit6 = QLineEdit(self.age)
        self.lineEdit6.setObjectName("lineEdit")
        self.lineEdit6.setFont(QFont("Arial", 10))
        self.layhor11.addWidget(self.lineEdit6, 0, QtCore.Qt.AlignHCenter)

    def predict_(self):
        self.layhor12 = QHBoxLayout(self.predict)
        self.butt = QPushButton(self.predict)
        self.butt.setText("Predict")
        self.butt.setObjectName("label")
        self.butt.setFont(QFont("Arial", 10))
        self.butt.setStyleSheet("color: #02659D")
        self.butt.clicked.connect(self.predict_action)
        self.layhor12.addWidget(self.butt, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit7 = QLineEdit(self.predict)
        self.lineEdit7.setObjectName("lineEdit")
        self.lineEdit7.setFont(QFont("Arial", 10))
        self.layhor12.addWidget(self.lineEdit7, 0, QtCore.Qt.AlignHCenter)

    
    def predict_action(self):
        self.lstval = []
        self.lstval.append(int(self.lineEdit1.text()))
        self.lstval.append(self.fuelitems[self.combo.currentText()])
        self.lstval.append(self.selleritems[self.combo2.currentText()])
        self.lstval.append(self.transmissionitems[self.combo3.currentText()])
        self.lstval.append(self.owneritems[self.combo4.currentText()])
        self.lstval.append(int(self.lineEdit2.text()))
        self.lstval.append(int(self.lineEdit3.text()))
        self.lstval.append(int(self.lineEdit4.text()))
        self.lstval.append(int(self.lineEdit5.text()))
        self.lstval.append(int(self.lineEdit6.text()))

        self.lstval = np.array(self.lstval)
        predicted = model.prediction([self.lstval])
        self.lineEdit7.setText(str(predicted))






def main():
    app = QApplication([sys.argv])
    gui = ModelGui()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
