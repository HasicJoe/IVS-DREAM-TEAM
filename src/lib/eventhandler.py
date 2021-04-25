from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
import PyQt5.QtGui as gui
import lib.mathlib as math

# add Number symbols to stack
def addNumberZero():
   math.Symbol(math.SymbolType.NUMBER, 0, '0')

def addNumberOne():
    math.Symbol(math.SymbolType.NUMBER, 1, '1')

def addNumberTwo():
    math.Symbol(math.SymbolType.NUMBER, 2, '2')

def addNumberThree():
   math.Symbol(math.SymbolType.NUMBER, 3, '3')

def addNumberFour():
    math.Symbol(math.SymbolType.NUMBER, 4, '4')

def addNumberFive():
   math.Symbol(math.SymbolType.NUMBER, 5, '5')

def addNumberSix():
    math.Symbol(math.SymbolType.NUMBER, 6, '6')

def addNumberSeven():
   math.Symbol(math.SymbolType.NUMBER, 7, '7')

def addNumberEight():
   math.Symbol(math.SymbolType.NUMBER, 8, '8')

def addNumberNine():
   math.Symbol(math.SymbolType.NUMBER, 9, '9')

def addDecimalPoint():
    math.Symbol(math.SymbolType.COMMA, ',', ',')

# add math operators to the stack
def addPlus():
    math.Symbol(math.SymbolType.OPERATOR, math.OperatorType.PLUS, '+')

def addMinus():
    math.Symbol(math.SymbolType.OPERATOR, math.OperatorType.MINUS, '-')

def addMultiply():
    math.Symbol(math.SymbolType.OPERATOR, math.OperatorType.MULTIPLY, '*')

def addDivide():
    math.Symbol(math.SymbolType.OPERATOR, math.OperatorType.DIVIDE, '/')

def addModulo():
    math.Symbol(math.SymbolType.OPERATOR, math.OperatorType.MODULO, 'mod')

# add math Functions to the stack

def addExp():
    math.Symbol(math.SymbolType.FUNCTION, math.FunctionType.EXP, '^')

def addNthRoot():
    math.Symbol(math.SymbolType.FUNCTION, math.FunctionType.NTHROOT, '√')

def addFactorial():
    math.Symbol(math.SymbolType.FUNCTION, math.FunctionType.FACTORIAL, '!')

def addRandom():
    math.Symbol(math.SymbolType.FUNCTION, math.FunctionType.RANDOM, 'rand')

# add math brackets to the stack
def addLeftBracket():
    math.Symbol(math.SymbolType.LEFT_BRACKET, '(', '(')

def addRightBracket():
    math.Symbol(math.SymbolType.RIGHT_BRACKET, ')', ')')

# TODO:clear the console display (clear the display label and the symbol stack)
def Clear():
    print('clear display')

# TODO: execute the computation (call mathlib)
def Execute():
    print('execute')

# key to action binding
ActionDict = {
    # numbers
    Qt.Key_0 : addNumberZero,
    Qt.Key_1 : addNumberOne,
    Qt.Key_2 : addNumberTwo,
    Qt.Key_3 : addNumberThree,
    Qt.Key_4 : addNumberFour,
    Qt.Key_5 : addNumberFive,
    Qt.Key_6 : addNumberSix,
    Qt.Key_7 : addNumberSeven,
    Qt.Key_8 : addNumberEight,
    Qt.Key_9 : addNumberNine,
    Qt.Key_Period : addDecimalPoint,
    Qt.Key_Comma : addDecimalPoint,

    # operators
    Qt.Key_Plus : addPlus,
    Qt.Key_Minus : addMinus,
    Qt.Key_Asterisk : addMultiply,
    Qt.Key_Slash : addDivide,
    # key_'%' == 37
    37 : addModulo,

    #  math operations (done with multiCharacterEventHandler)

    # brackets
    # key_'(' == 40
    40 : addLeftBracket,
    # key_')' == 41 
    41 : addRightBracket,

    # commands
    Qt.Key_Escape : Clear,
    Qt.Key_Enter : Execute,
    Qt.Key_Return : Execute
}

def updateDisplay(event):
    print(event)

# bind mouse and keyboard events to the main window 
def bind_event(window):
    # keyboard input handler
    window.keyPressEvent = keyboardEventHandler

    # mouse input handler (left click)
    window.key_0.clicked.connect(addNumberZero)
    window.key_1.clicked.connect(addNumberOne)
    window.key_2.clicked.connect(addNumberTwo)
    window.key_3.clicked.connect(addNumberThree)
    window.key_4.clicked.connect(addNumberFour)
    window.key_5.clicked.connect(addNumberFive)
    window.key_6.clicked.connect(addNumberSix)
    window.key_7.clicked.connect(addNumberSeven)
    window.key_8.clicked.connect(addNumberEight)
    window.key_9.clicked.connect(addNumberNine)
    window.key_point.clicked.connect(addDecimalPoint)
    
    # operators
    window.key_add.clicked.connect(addPlus)
    window.key_sub.clicked.connect(addMinus)
    window.key_mul.clicked.connect(addMultiply)
    window.key_div.clicked.connect(addDivide)
    window.key_mod.clicked.connect(addModulo)
    
    # math functions
    window.key_exp.clicked.connect(addExp)
    window.key_root.clicked.connect(addNthRoot)
    window.key_fact.clicked.connect(addFactorial)
    window.key_rand.clicked.connect(addRandom)
    
    # brackets
    window.key_lb.clicked.connect(addLeftBracket)
    window.key_rb.clicked.connect(addRightBracket)
    
    # command buttons
    window.key_eq.clicked.connect(Execute)
    window.key_c.clicked.connect(Clear)

# key handler which perform actions upon entered multiple keys
enteredList = []
MultiCharActionDict = {
    'FACT' : addFactorial,
    'RAND' : addRandom, 
    'MOD'  : addModulo,
    'EXP'  : addExp,
    'ROOT' : addNthRoot,
    'CLEAR': Clear
}
def multiCharacterEventHandler(event):
    #FACT, RAND, SQRT
    try:
        enteredList.append(chr(event.key()))
    except ValueError:
        # key is not from alphabet range
        pass
    else:
        sequence = ''.join(enteredList)
        for key, action in MultiCharActionDict.items():
            if key in sequence:
                action()
                enteredList.clear()

# general keyboard handler
def keyboardEventHandler(event):
    print(event.count())
    for k, v in gui.QKeyEvent.__dict__.items():
        pass
        print(k, v)
    # get action from the action dictionary
    try:
        function = ActionDict[event.key()]
    # handle multi character binds (may be changed)
    except KeyError:      
        multiCharacterEventHandler(event)
    # perform the action
    else:
        function()

