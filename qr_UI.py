import pyqrcode
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import random
import urllib.request

import time

class MainWindow(QMainWindow):


    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
    
        self.counter = 0
    
        layout = QHBoxLayout()
        
        self.l = QLabel("Loading....")
        # b = QPushButton("DANGER!")
        self.l1 = QLabel("add lebel")

    
        layout.addWidget(self.l)

        self.download_add()
        layout.addWidget(self.l1)
        Mypixmap = QPixmap('add.png')
        Mypixmap1 = Mypixmap.scaled(400, 800)
        self.l1.setPixmap(Mypixmap1)
        # layout.addWidget(b)
    
        w = QWidget()
        w.setLayout(layout)
    
        self.setCentralWidget(w)
    
        self.showFullScreen()

        self.timer = QTimer()
        self.timer.setInterval(5000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()
    def getTempID_and_createNewQr(self):
    	p = "1234"
    	t = str(random.randint(1111,9999))
    	self.newQr(p,t)
    	time.sleep(2)

    def newQr(self,Purl, Turl):
    	baseUrl = "https:://bengol.000webhostapp.com/call.php?Screennum="+Turl+"temp="+Purl
    	code = pyqrcode.create(baseUrl)
    	code.svg('uca.svg', scale=4)


    def recurring_timer(self):
        self.getTempID_and_createNewQr()
        pixmap = QPixmap('uca.svg')
        pixmap1 = pixmap.scaled(800, 800)
        self.l.setPixmap(pixmap1)
        # self.l.setText("Counter: %d" % self.counter)

    def download_add(self):
    	urllib.request.urlretrieve("https://raw.guthubusercontent.com/rakeshseal0/feedback-bengalathon/master/Capture.PNG", "add.png")

    
    
app = QApplication([])
window = MainWindow()
app.exec_()