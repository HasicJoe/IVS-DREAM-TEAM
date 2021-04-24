
class OperatorType():
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    MODULO = 5

class FunctionType():
    SQUARE = 1
    NTHROOT = 2
    FACTORIAL = 3
    RANDOM = 4

class SymbolType():
    NUMBER = 1
    COMMA = 2
    OPERATOR = 3
    FUNCTION = 4
    LEFT_BRACKET = 5
    RIGHT_BRACKET = 6

class Symbol():
    SymbolList = []
    def __init__(self, type, value, display):
        self.type = type
        self.value = value
        self.display = display
        Symbol.SymbolList.append(self)
        print([symb.display for symb in Symbol.SymbolList])
