from PySide2.QtWidgets import  *
from PySide2.QtGui import *
import random

class IHM(QWidget):
    def __init__(self,nombre):
        QWidget.__init__(self)
        self.nombre=nombre
        self.setWindowTitle("IHM")
        self.setMinimumSize(400,300)
        self.layout = QVBoxLayout()


        self.button=QPushButton("Changer mon texte!")
        self.layout.addWidget(self.button)

        self.zonetexte=QTextEdit()
        self.layout.addWidget((self.zonetexte))

        self.button.clicked.connect(self.clic)

        self.setLayout(self.layout)


    def clic(self):
        self.zonetexte.setText("clic "+str(self.nombre))

        self.button.setText("clic "+str(self.nombre))
        self.nombre+=1


if __name__ == "__main__":
   app = QApplication([])
   win = IHM(1)
   win.show()
   app.exec_()

