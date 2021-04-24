from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt

#dick = {
##    Qt.Key_4 : "function4"
#}

def bind(window):
    window.keyPressEvent = keyFunc
   # window.key_4.mouseReleaseEvent = mouseFunc
    window.key_4.clicked.connect(mouseFunc)
    window.key_5.clicked.connect(mouseAnotherFunc)

# test button click even handler
def mouseFunc(event):
    print('4')

def mouseAnotherFunc(flag):
    print('5')


# test keypress event handler
def keyFunc(e):



    print(e.key())
    if e.key() == Qt.Key_Escape:
        print("MFS")