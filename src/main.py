import sys
import lib.eventhandler as evthandler
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtCore import Qt
from gui.gui import Ui_MainWindow



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    evthandler.bind_event(window)

    app.exec()