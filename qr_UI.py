import pyqrcode
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import random
import requests
import time

class MainWindow(QMainWindow):


    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
    
        self.counter = 0
        self.flag = False
        
        with open("MyFile.txt","r") as f:
        	self.t = f.read() 
        	print(self.t)
        	f.close()
        self.f1 = open("MyFile.txt", "w")
    
        layout = QHBoxLayout()
        
        self.l = QLabel("Loading....")
        # b = QPushButton("DANGER!")
        self.l1 = QLabel("add lebel")

    
        layout.addWidget(self.l)


        layout.addWidget(self.l1)
        Mypixmap = QPixmap('/home/rak3sh/rak3sh/py/feedback-bengalathon/Capture.PNG')
        Mypixmap1 = Mypixmap.scaled(400, 800)
        self.l1.setPixmap(Mypixmap1)
        layout.addWidget(self.l1)
    
        w = QWidget()
        w.setLayout(layout)
    
        self.setCentralWidget(w)
    
        self.showFullScreen()
        # self.show()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()
    def __del__(self):
    	print("Closing..")
    	# f = open("MyFile.txt","w")
    	self.f1.write(self.t) 
    	self.f1.close()
    	print("Sucess..")

    def getTempID_and_createNewQr(self):
        p = "1234"
        # t = "0000"
        self.newQr(p)
        time.sleep(2)

    def newQr(self,Purl):
    	baseUrl = "https://bengol.000webhostapp.com/call.php?update&id="+self.t
    	request = requests.post(baseUrl)
    	self.t = request.text
    	print("id UPDATED--->>" + request.text)
    	code = pyqrcode.create("bengazi" + self.t + "5l")
    	code.svg('uca.svg', scale=4)


    def recurring_timer(self):
    	if self.flag is not True:
    		self.timer.setInterval(60000)
    	self.getTempID_and_createNewQr()
    	pixmap = QPixmap('uca.svg')
    	pixmap1 = pixmap.scaled(800, 800)
    	self.l.setPixmap(pixmap1)
        # self.l.setText("Counter: %d" % self.counter)
    
    
app = QApplication([])
window = MainWindow()
app.exec_()