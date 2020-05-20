from PySide2.QtWidgets import  *
from PySide2.QtGui import *
import random

class IHM(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")
        self.layout = QHBoxLayout()
        self.Bar=QProgressBar()

        self.slider=QSlider()

        self.layout.addWidget(self.Bar)
        self.layout.addWidget(self.slider)
        self.slider.valueChanged.connect(self.Slot)

        self.setLayout(self.layout)
    def signal(self):
        val = self.slider.value()
        return val

    def Slot(self):
        self.Bar.setValue(self.signal())








if __name__ == "__main__":
   app = QApplication([])
   win = IHM()
   win.show()
   app.exec_()

