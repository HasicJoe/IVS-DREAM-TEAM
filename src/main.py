import sys
import lib.eventhandler as eh
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtCore import Qt
from gui.gui import Ui_MainWindow
import lib.profiler as pf
import cProfile



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)



if __name__ == "__main__":    
    
    if not sys.stdin.isatty():
        pr = cProfile.Profile()
        pf.Profiler(sys.stdin,pr)
    else:
        app = QtWidgets.QApplication(sys.argv)
        window = MainWindow()
        window.show()
        # bind event handler to the main window
        eh.EventHandler(window)
        app.exec()