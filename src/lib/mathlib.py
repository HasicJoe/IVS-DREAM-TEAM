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

PrecedenceSyntaxTable = {         #   +    -    *     /   %    ^    √    !    R    (    )    i    $
    TokenType.OPERATION_ADD :       [">", ">", "<", "<", "<", "<", "<", "<", "<", "<", ">", "<", ">"],
    TokenType.OPERATION_SUBSTRACT : [">", ">", "<", "<", "<", "<", "<", "<", "<", "<", ">", "<", ">"],
    TokenType.OPERATION_MULTIPLY :  [">", ">", ">", ">", ">", "<", "<", "<", "<", "<", ">", "<", ">"],
    TokenType.OPERATION_DIVIDE :    [">", ">", ">", ">", ">", "<", "<", "<", "<", "<", ">", "<", ">"],
    TokenType.OPERATION_MODULO :    [">", ">", ">", ">", ">", "<", "<", "<", "<", "<", ">", "<", ">"],
    TokenType.OPERATION_EXP :       [">", ">", ">", ">", ">", "<", "<", "<", "<", "<", ">", "<", ">"],

    TokenType.FUNCTION_ROOT :       [">", ">", ">", ">", ">", ">", ">", "<", "<", "<", ">", "<", ">"],
    TokenType.FUNCTION_FACTORIAL :  [">", ">", ">", ">", ">", ">", ">", ">", ">", "<", ">", "<", ">"],
    TokenType.FUNCTION_RAND :       [">", ">", ">", ">", ">", ">", ">", ">", ">", "<", ">", "<", ">"],

    TokenType.LEFT_BRACKET :        ["<", "<", "<", "<", "<", "<", "<", "<", "<", "<", "=", "<", "S"],
    TokenType.RIGHT_BRACKET :       [">", ">", ">", ">", ">", ">", ">", ">", ">", "S", ">", ">", ">"],
    
    TokenType.NUMBER :              [">", ">", ">", ">", ">", ">", ">", ">", ">", "S", ">", "S", ">"],
    
    TokenType.DOLLAR :              ["<", "<", "<", "<", "<", "<", "<", "<", "<", "<", "S", "<", "S"]
}

def toNonTerminal(tokenlist):
    return Token(TokenType.NON_TERMINAL, tokenlist[0].value)

def removeBrackets(tokenlist):
    return Token(TokenType.NON_TERMINAL, tokenlist[1].value)

def addTokens(tokenlist):
    return Token(TokenType.NON_TERMINAL, add(tokenlist[0].value, tokenlist[2].value))

def substractTokens(tokenlist):
    return Token(TokenType.NON_TERMINAL, sub(tokenlist[0].value, tokenlist[2].value))

def multiplyTokens(tokenlist):
    return Token(TokenType.NON_TERMINAL, mul(tokenlist[0].value, tokenlist[2].value))

def divideTokens(tokenlist):
    return Token(TokenType.NON_TERMINAL, div(tokenlist[0].value, tokenlist[2].value))

def moduloTokens(tokenlist):
    return Token(TokenType.NON_TERMINAL, mod(tokenlist[0].value, tokenlist[2].value))

def expTokens(tokenlist):
    return Token(TokenType.NON_TERMINAL, exp(tokenlist[0].value, tokenlist[2].value))

def factToken(tokenlist):
    return Token(TokenType.NON_TERMINAL, fact(tokenlist[0].value))

def randToken(tokenlist):
    return Token(TokenType.NON_TERMINAL, rand(tokenlist[1].value))

def rootTokens(tokenlist):
    return Token(TokenType.NON_TERMINAL, root(tokenlist[0].value, tokenlist[2].value))

Grammar = {
    (TokenType.NUMBER,) : toNonTerminal,
    (TokenType.LEFT_BRACKET, TokenType.NON_TERMINAL, TokenType.RIGHT_BRACKET,) : removeBrackets,
    (TokenType.NON_TERMINAL, TokenType.OPERATION_ADD, TokenType.NON_TERMINAL,) : addTokens,
    (TokenType.NON_TERMINAL, TokenType.OPERATION_SUBSTRACT, TokenType.NON_TERMINAL,) : substractTokens,
    (TokenType.NON_TERMINAL, TokenType.OPERATION_MULTIPLY, TokenType.NON_TERMINAL,) : multiplyTokens,
    (TokenType.NON_TERMINAL, TokenType.OPERATION_DIVIDE, TokenType.NON_TERMINAL,) : divideTokens,
    (TokenType.NON_TERMINAL, TokenType.OPERATION_MODULO, TokenType.NON_TERMINAL,) : moduloTokens,
    (TokenType.NON_TERMINAL, TokenType.OPERATION_EXP, TokenType.NON_TERMINAL,) : expTokens,
    (TokenType.NON_TERMINAL, TokenType.FUNCTION_FACTORIAL,) : factToken,
    (TokenType.FUNCTION_RAND, TokenType.NON_TERMINAL,) : randToken,
    (TokenType.NON_TERMINAL, TokenType.FUNCTION_ROOT, TokenType.NON_TERMINAL,) : rootTokens,
}
# for debugging purposes
typeToTableMap = {
    TokenType.OPERATION_ADD :       0,
    TokenType.OPERATION_SUBSTRACT : 1,
    TokenType.OPERATION_MULTIPLY :  2,
    TokenType.OPERATION_DIVIDE :    3,
    TokenType.OPERATION_MODULO :    4,
    TokenType.OPERATION_EXP :       5,
    TokenType.FUNCTION_ROOT :       6,
    TokenType.FUNCTION_FACTORIAL :  7,
    TokenType.FUNCTION_RAND :       8,
    TokenType.LEFT_BRACKET :        9,
    TokenType.RIGHT_BRACKET :       10,
    TokenType.NUMBER :              11,
    TokenType.DOLLAR :              12
}

# Precedence Syntax Analysis
def PSA(tokens):
    # temporary list for reduce operation
    templist = []    
    # add a '$' to the end of input
    tokens.append(Token(TokenType.DOLLAR, '$'))
    # stack holding the expression evaluation, add '$' at the bottom of the stack
    Stack = [Token(TokenType.DOLLAR, '$')]
    while(True):
        # ending condition (successfull evaluation)
        if len(tokens) == 1 and tokens[0].type == TokenType.DOLLAR and len(Stack) == 2 and Stack[1].type == TokenType.NON_TERMINAL:
            print(Stack[1].value)
            return
        try:
            for StackTok in Stack[::-1]:
                if StackTok.type != TokenType.NON_TERMINAL and StackTok.type != TokenType.SHIFT:
                    break
            #print('stack',StackTok.value, 'input', tokens[0].value)
            operation = PrecedenceSyntaxTable[StackTok.type][typeToTableMap[tokens[0].type]]
            #print("operation",operation)
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
            #  print('stack after shift; ', [tok.value for tok in Stack])
        # operation reduce
        elif operation == ">" or operation == "=":
            if operation == "=":
                Stack.append(tokens.pop(0))
                # print('stack before reduce;',[tok.value for tok in Stack])
            templist.clear()
            while Stack[-1].type != TokenType.SHIFT:
                templist.append(Stack.pop())
            try:
                templist = templist[::-1]
                action = Grammar[tuple([tok.type for tok in templist])]
            except KeyError:
                print('NON EXISTING GRAMMAR RULE')
                return
            else:          
                if Stack[-1].type == TokenType.SHIFT:
                    Stack.pop()
                Stack.append(action(templist))
                # print('stack after reduce;', [tok.value for tok in Stack])
        # syntax err
        else:
            print('SYNTAX ERR no operation in precedence table for this expression')
            return


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
    n = int(n)
    if n < 0:
        raise ValueError
    result = 1
    for i in range(n):
        result *= (i+1)
    return result