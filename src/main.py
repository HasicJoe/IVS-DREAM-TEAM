import sys
import lib.eventhandler as evthandler
from PyQt5 import QtWidgets, uic
from gui.gui import Ui_MainWindow



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()

evthandler.bind(window)

app.exec()