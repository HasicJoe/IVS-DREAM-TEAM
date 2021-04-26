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
        #print([symb.display for symb in SymbolList])

# types of tokens to provide execution
class TokenType():
    NUMBER =                0x10
    # operations
    OPERATION_ADD =         0x20
    OPERATION_SUBSTRACT =   0x21
    OPERATION_MULTIPLY =    0x22
    OPERATION_DIVIDE =      0x23
    OPERATION_MODULO =      0x24
    OPERATION_EXP =         0x25
    # brackets
    LEFT_BRACKET =          0x30
    RIGHT_BRACKET =         0x31
    # functions
    FUNCTION_RAND =         0x40
    FUNCTION_FACTORIAL =    0x41
    FUNCTION_ROOT =         0x42

    # for syntax analysis
    DOLLAR =                0x50
    NON_TERMINAL =          0x51
    SHIFT =                 0x52

# list of tokens to be computed
class Token():
    #constructor
    def __init__(self, type, value):
        self.type = type
        self.value = value

# translate symbols into tokens
def PopulateTokens():
    TokenList = []
    numberBuffer = ''
    for symb in SymbolList:
        if symb.type in [SymbolType.COMMA, SymbolType.NUMBER]:
            numberBuffer+=str(symb.value)
        else:
            if numberBuffer:
                TokenList.append(Token(TokenType.NUMBER, float(numberBuffer)))
                numberBuffer = ''
            TokenList.append(Token(symb.type, symb.value))
    if numberBuffer:
        TokenList.append(Token(TokenType.NUMBER, float(numberBuffer)))
    return TokenList

def Compute():
    if SymbolList:
        PSA(PopulateTokens())

PrecedenceSyntaxTable = {         #   +    -    *     /   (    )    i    $
    TokenType.OPERATION_ADD :       [">", ">", "<", "<", "<", ">", "<", ">"],
    TokenType.OPERATION_SUBSTRACT : [">", ">", "<", "<", "<", ">", "<", ">"],
    TokenType.OPERATION_MULTIPLY :  [">", ">", ">", ">", "<", ">", "<", ">"],
    TokenType.OPERATION_DIVIDE :    [">", ">", ">", ">", "<", ">", "<", ">"],
    TokenType.LEFT_BRACKET :        ["<", "<", "<", "<", "<", "S", "S", "S"],
    TokenType.RIGHT_BRACKET :       [">", ">", ">", ">", "S", ">", ">", ">"],
    TokenType.NUMBER :              [">", ">", ">", ">", "S", ">", "S", ">"],
    TokenType.DOLLAR :              ["<", "<", "<", "<", "<", "S", "<", "S"]

    #TODO: add remaining operations
}

def toNonTerminal(tokenlist):
    return Token(TokenType.NON_TERMINAL, tokenlist[0].value)

def removeBrackets(tokenlist):
    return Token(TokenType.NON_TERMINAL, tokenlist[1].value)

def addTokens(tokenlist):
    return Token(TokenType.NON_TERMINAL, add(tokenlist[2].value, tokenlist[0].value))

def substractTokens(tokenlist):
    return Token(TokenType.NON_TERMINAL, sub(tokenlist[2].value, tokenlist[0].value))

def multiplyTokens(tokenlist):
    return Token(TokenType.NON_TERMINAL, mul(tokenlist[2].value, tokenlist[0].value))

def divideTokens(tokenlist):
    return Token(TokenType.NON_TERMINAL, div(tokenlist[2].value, tokenlist[0].value))

Grammar = {
    (TokenType.NUMBER,) : toNonTerminal,
    (TokenType.LEFT_BRACKET, TokenType.NON_TERMINAL, TokenType.RIGHT_BRACKET,) : toNonTerminal,
    (TokenType.NON_TERMINAL, TokenType.OPERATION_ADD, TokenType.NON_TERMINAL,) : addTokens,
    (TokenType.NON_TERMINAL, TokenType.OPERATION_SUBSTRACT, TokenType.NON_TERMINAL,) : substractTokens,
    (TokenType.NON_TERMINAL, TokenType.OPERATION_MULTIPLY, TokenType.NON_TERMINAL,) : multiplyTokens,
    (TokenType.NON_TERMINAL, TokenType.OPERATION_DIVIDE, TokenType.NON_TERMINAL,) : divideTokens

    #TODO: add remaining operations
}

# for debugging purposes
typeToTableMap = {
    TokenType.OPERATION_ADD :       0,
    TokenType.OPERATION_SUBSTRACT : 1,
    TokenType.OPERATION_MULTIPLY :  2,
    TokenType.OPERATION_DIVIDE :    3,
    TokenType.LEFT_BRACKET :        4,
    TokenType.RIGHT_BRACKET :       5,
    TokenType.NUMBER :              6,
    TokenType.DOLLAR :              7
}

def PSA(tokens):

    # temporary list for reduce operation
    templist = []    
    # add a '$' to the end of input
    tokens.append(Token(TokenType.DOLLAR, '$'))

    # stack holding the expression evaluation
    Stack = [Token(TokenType.DOLLAR, '$')]
    while(1):
        # ending condition
        if len(tokens) == 1 and tokens[0].type == TokenType.DOLLAR and len(Stack) == 2 and Stack[1].type == TokenType.NON_TERMINAL:
            print(Stack[1].value)
            return
        try:
            for StackTok in Stack[::-1]:
                if StackTok.type != TokenType.NON_TERMINAL and StackTok.type != TokenType.SHIFT:
                    break
            operation = PrecedenceSyntaxTable[StackTok.type][typeToTableMap[tokens[0].type]]
        except KeyError:
            print('PRECEDENCE SYNTAX TABLE NO OPERATION')
            return
        # operation shift
        if operation == "<":
            if Stack[-1].type == TokenType.NON_TERMINAL:
                temp = Stack.pop()
                Stack.append(Token(TokenType.SHIFT, '<'))
                Stack.append(temp)
            else:
                Stack.append(Token(TokenType.SHIFT, '<'))
            Stack.append(tokens.pop(0))
            print('stack after shift; ', [tok.value for tok in Stack])
        # operation reduce
        elif operation == ">":
            templist.clear()
            while Stack[-1].type != TokenType.SHIFT:
                templist.append(Stack.pop())
            try:
                action = Grammar[tuple([tok.type for tok in templist])]
            except KeyError:
                print('NON EXISTING GRAMMAR RULE')
                return
            else:
                
                if Stack[-1].type == TokenType.SHIFT:
                    Stack.pop()
                Stack.append(action(templist))
                print('stack after reduce;', [tok.value for tok in Stack])
        # syntax err
        else:
            print('SYNTAX ERR no operation in precedence table for this expression')
            exit(1)


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def exp(a, b):
    return a ** b

def root(a, b):
    return b ** (1/float(a))

def rand(n):
    return random.random()*n

def arith_average(sum,list):
    return sum / len(list)

def list_len(list):
    return len(list)

def mod(a,b):
    return a % b

def fact(n):
    if n < 0:
        raise ValueError
    n = int(n)
    return float(1) if n == 1 or n == 0 else float(n * fact(n-1))