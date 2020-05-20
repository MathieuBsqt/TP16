from PySide2.QtWidgets import  *
from PySide2.QtGui import *
import random

class Cycles(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Cycles de l'ISEN Yncrea Ouest")
        self.setMinimumSize(600,400)
        self.layout = QVBoxLayout()
        self.Button=QPushButton("Changer le cycle")

        self.text=QLabel()

        self.layout.addWidget(self.text)
        self.layout.addWidget(self.Button)

        self.Button.clicked.connect(self.randomlabel)


        self.setLayout(self.layout)


    def randomlabel(self):
        liste=["CSI", "CIR", "BIOST", "CENT", "BIAST", "EST"]
        text=random.choice(liste)
        print(text)
        self.text.setText(text)






if __name__ == "__main__":
   app = QApplication([])
   win = Cycles()
   win.show()
   app.exec_()

