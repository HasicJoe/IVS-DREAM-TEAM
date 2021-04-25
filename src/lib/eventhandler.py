from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
import PyQt5.QtGui as gui
import lib.mathlib as math

class EventHandler():
    # bind mouse and keyboard events to the main window 
    def __init__(self, window):
        self.window = window
        self.enteredList = []
        # keyboard input handler
        self.window.keyPressEvent = self.keyboardEventHandler

        # mouse input handler (left click)
        self.window.key_0.clicked.connect(self.addNumberZero)
        self.window.key_1.clicked.connect(self.addNumberOne)
        self.window.key_2.clicked.connect(self.addNumberTwo)
        self.window.key_3.clicked.connect(self.addNumberThree)
        self.window.key_4.clicked.connect(self.addNumberFour)
        self.window.key_5.clicked.connect(self.addNumberFive)
        self.window.key_6.clicked.connect(self.addNumberSix)
        self.window.key_7.clicked.connect(self.addNumberSeven)
        self.window.key_8.clicked.connect(self.addNumberEight)
        self.window.key_9.clicked.connect(self.addNumberNine)
        self.window.key_point.clicked.connect(self.addDecimalPoint)
        
        # operators
        self.window.key_add.clicked.connect(self.addPlus)
        self.window.key_sub.clicked.connect(self.addMinus)
        self.window.key_mul.clicked.connect(self.addMultiply)
        self.window.key_div.clicked.connect(self.addDivide)
        self.window.key_mod.clicked.connect(self.addModulo)
        
        # math functions
        self.window.key_exp.clicked.connect(self.addExp)
        self.window.key_root.clicked.connect(self.addNthRoot)
        self.window.key_fact.clicked.connect(self.addFactorial)
        self.window.key_rand.clicked.connect(self.addRandom)
        
        # brackets
        self.window.key_lb.clicked.connect(self.addLeftBracket)
        self.window.key_rb.clicked.connect(self.addRightBracket)
        
        # command buttons
        self.window.key_eq.clicked.connect(self.Execute)
        self.window.key_c.clicked.connect(self.Clear)

    # add Number symbols to stack
    def addNumberZero(self):
        math.Symbol(math.SymbolType.NUMBER, 0, '0')

    def addNumberOne(self):
        math.Symbol(math.SymbolType.NUMBER, 1, '1')

    def addNumberTwo(self):
        math.Symbol(math.SymbolType.NUMBER, 2, '2')

    def addNumberThree(self):
        math.Symbol(math.SymbolType.NUMBER, 3, '3')

    def addNumberFour(self):
        math.Symbol(math.SymbolType.NUMBER, 4, '4')

    def addNumberFive(self):
        math.Symbol(math.SymbolType.NUMBER, 5, '5')

    def addNumberSix(self):
        math.Symbol(math.SymbolType.NUMBER, 6, '6')

    def addNumberSeven(self):
        math.Symbol(math.SymbolType.NUMBER, 7, '7')

    def addNumberEight(self):
        math.Symbol(math.SymbolType.NUMBER, 8, '8')

    def addNumberNine(self):
        math.Symbol(math.SymbolType.NUMBER, 9, '9')

    def addDecimalPoint(self):
        math.Symbol(math.SymbolType.COMMA, ',', ',')

    # add math operators to the stack
    def addPlus(self):
        math.Symbol(math.SymbolType.OPERATOR, math.OperatorType.PLUS, '+')

    def addMinus(self):
        math.Symbol(math.SymbolType.OPERATOR, math.OperatorType.MINUS, '-')

    def addMultiply(self):
        math.Symbol(math.SymbolType.OPERATOR, math.OperatorType.MULTIPLY, '*')

    def addDivide(self):
        math.Symbol(math.SymbolType.OPERATOR, math.OperatorType.DIVIDE, '/')

    def addModulo(self):
        math.Symbol(math.SymbolType.OPERATOR, math.OperatorType.MODULO, 'mod')

    # add math Functions to the stack
    def addExp(self):
        math.Symbol(math.SymbolType.FUNCTION, math.FunctionType.EXP, '^')

    def addNthRoot(self):
        math.Symbol(math.SymbolType.FUNCTION, math.FunctionType.NTHROOT, '√')

    def addFactorial(self):
        math.Symbol(math.SymbolType.FUNCTION, math.FunctionType.FACTORIAL, '!')

    def addRandom(self):
        math.Symbol(math.SymbolType.FUNCTION, math.FunctionType.RANDOM, 'rand')

    # add math brackets to the stack
    def addLeftBracket(self):
        math.Symbol(math.SymbolType.LEFT_BRACKET, '(', '(')

    def addRightBracket(self):
        math.Symbol(math.SymbolType.RIGHT_BRACKET, ')', ')')

    # TODO:clear the console display (clear the display label and the symbol stack)
    def Clear(self):
        print('clear display')

    # TODO: execute the computation (call mathlib)
    def Execute(self):
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

    # key handler which perform actions upon entered multiple keys
    MultiCharActionDict = {
        'FACT' : addFactorial,
        'RAND' : addRandom, 
        'MOD'  : addModulo,
        'EXP'  : addExp,
        'ROOT' : addNthRoot,
        'CLEAR': Clear
    }
    def multiCharacterEventHandler(self, event):
        #FACT, RAND, SQRT
        try:
            self.enteredList.append(chr(event.key()))
        except ValueError:
            # key is not from alphabet range
            pass
        else:
            sequence = ''.join(self.enteredList)
            for key, action in EventHandler.MultiCharActionDict.items():
                if key in sequence:
                    action(self)
                    self.enteredList.clear()

    # general keyboard handler
    def keyboardEventHandler(self, event):
        # get action from the action dictionary
        try:
            function = EventHandler.ActionDict[event.key()]
        # handle multi character binds (may be changed)
        except KeyError:      
            self.multiCharacterEventHandler(event)
        # perform the action
        else:
            function(self)

