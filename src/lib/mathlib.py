import random 

class SymbolType():
    NUMBER =        0x10
    COMMA =         0x11
    
    PLUS =          0x20
    MINUS =         0x21
    MULTIPLY =      0x22
    DIVIDE =        0x23
    MODULO =        0x24
    EXP =           0x25
    
    LEFT_BRACKET =  0x30
    RIGHT_BRACKET = 0x31

    RANDOM =        0x40
    FACTORIAL =     0x41
    ROOT =          0x42       
    
   

# list of entered symbols
SymbolList = []
class Symbol():
    def __init__(self, type, value, display):
        self.type = type
        self.value = value
        self.display = display
        SymbolList.append(self)
        print([symb.display for symb in SymbolList])

# types of tokens to provide execution
class TokenType():
    NUMBER = 0x10
    # operations
    OPERATION_ADD = 0x20
    OPERATION_SUBSTRACT = 0x21
    OPERATION_MULTIPLY = 0x22
    OPERATION_DIVIDE = 0x23
    OPERATION_MODULO = 0x24
    OPERATION_EXP = 0x25
    # brackets
    LEFT_BRACKET = 0x30
    RIGHT_BRACKET = 0x31
    # functions
    FUNCTION_RAND = 0x40
    FUNCTION_FACTORIAL = 0x41
    FUNCTION_ROOT = 0x42

# list of tokens to be computed
TokenList = []
class Token():
    #constructor
    def __init__(self, type, value):
        self.type = type
        self.value = value

# translate symbols into tokens
def PopulateTokens():
    TokenList.clear()
    numberBuffer = ''
    for symb in SymbolList:
        if symb.type in [SymbolType.COMMA, SymbolType.NUMBER]:
            numberBuffer+=str(symb.value)
        else:
            if numberBuffer:
                TokenList.append(Token(TokenType.NUMBER, float(numberBuffer)))
                numberBuffer = ''
            TokenList.append(Token(symb.type, -1))
    if numberBuffer:
        TokenList.append(Token(TokenType.NUMBER, float(numberBuffer)))

def Compute():
    PopulateTokens()

    print([token.value for token in TokenList])



def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def exp(a, b):
    return a ** b

def root(a, b):
    return a ** (1/float(b))

def rand(n):
    return random.random()*n

def fact(n):
    if n < 0:
        raise ValueError
    n = int(n)
    return float(1) if n == 1 or n == 0 else float(n * fact(n-1))