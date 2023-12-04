import ply.lex as lex

# List of reserved words. 
reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'bool': 'BOOL',
    'string': 'STRING',
    'num': 'NUM',
    'true': 'TRUE',
    'false': 'FALSE',
    'input': 'INPUT',
    'print': 'PRINT',
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
}

# List of token names.
tokens = [
    'VARIABLE',
    'TYPE'
    'CODE_BLOCK'
    'OPERATION',
    'DECLARATION',
    'ATTRIBUTION',
    'ARITHMETIC',
    'RELATIONAL',
    'LOGICAL',
    'CONDITIONAL',
    'REPETITION'
] + list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LEFTPARENTHESES  = r'\('
t_RIGHTPARENTHESES  = r'\)'
t_BEGIN = r'{'
t_END = r'}'
t_DOT = r'.'
t_ATTRIBUTIONSIGN  = r'\='
t_EQUAL = r'=='
t_GREATERTHAN = r'>'
t_GREATEREQUALTHAN = r'>='
t_LESSTHAN = r'<'
t_LESSEQUALTHAN = r'<='
t_DIFFERENT = r'!='

# A regular expression rule with some action code
def t_VARIABLE(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'VARIAVEL')
    return t

def t_INT(t):
    r'(-)?\d+' 
    return t

def t_CHAR(t):
    r'[a-zA-Z0-9]' 
    return t

def t_STRING(t):
    r'[a-zA-Z0-9]+' 
    return t

def t_BOOL(t):
    r'true|false' 
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()