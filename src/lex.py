import ply.lex as lex
import sys
import os

# List of reserved words. 
reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'True': 'TRUE',
    'False': 'FALSE',
    'input': 'INPUT',
    'print': 'OUTPUT',
    'float': 'TYPE_FLOAT',
    'int': 'TYPE_INT',
    'bool': 'TYPE_BOOL',
    'string': 'TYPE_STRING',
    'char': 'TYPE_CHAR',
    'num': 'TYPE_NUM',
    # 'then' : 'THEN',
    # 'main' : 'MAIN',
}

# List of token names.
tokens = [
    'BEGIN',
    'END',

    #ARITHMETIC
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',

    # LOGICAL
    'AND',
    'OR',
    'NOT',

    # RELATIONAL
    'EQUAL',
    'GREATEREQUALTHAN',
    'GREATERTHAN',
    'LESSEQUALTHAN',
    'LESSTHAN',
    'DIFFERENT',

    # SPECIAL CHARACTERE
    'LEFTPARENTHESES',
    'RIGHTPARENTHESES',
    # 'DOT',
    'ATTRIBUTIONSIGN',

    #TYPE VALUES
    'FLOAT',
    'INT',
    'BOOL',
    'STRING',
    'CHAR',
    'NUM',

    'VARIABLE',
    # 'CODE_BLOCK',
] + list(reserved.values())

# Regular expression rules for simple tokens
t_BEGIN = r'\{'
t_END = r'\}'
t_LEFTPARENTHESES  = r'\('
t_RIGHTPARENTHESES  = r'\)'

t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'

t_INPUT = r'input'
t_OUTPUT = r'print'

t_TRUE = r'True'
t_FALSE = r'False'

t_TYPE_FLOAT = r'float'
t_TYPE_INT = r'int'
t_TYPE_BOOL = r'bool'
t_TYPE_STRING = r'string'
t_TYPE_CHAR = r'char'
t_TYPE_NUM = r'num'

t_PLUS    = r'\+'
t_MINUS   = r'\-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'


t_EQUAL = r'\=\='
t_GREATEREQUALTHAN = r'\>\='
t_GREATERTHAN = r'\>'
t_LESSEQUALTHAN = r'\<\='
t_LESSTHAN = r'\<'
t_DIFFERENT = r'\!\='

t_AND = '\&\&'
t_OR = '\|\|'
t_NOT = '\!'

t_ATTRIBUTIONSIGN  = r'\='

# A regular expression rule with some action code
def t_VARIABLE(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t

def t_FLOAT(t):
    r'(-)?\d+(.)\d+' 
    t.value = float(t.value)
    return t

def t_INT(t):
    r'(-)?\d+' 
    t.value = int(t.value)
    return t

def t_NUM(t):
    r'(-)?\d+(.)\d+' 
    t.value = float(t.value)
    return t

def t_BOOL(t):
    r'True|False' 
    return t

def t_STRING(t):
    r'\"[a-zA-Z0-9]+\"' 
    return t

def t_CHAR(t):
    r'[a-zA-Z0-9]' 
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

precedence = (
    ('left','LEFTPARENTHESES','RIGHTPARENTHESES'),
    ('left','AND','OR'),
    ('left','GREATERTHAN','LESSTHAN', 'GREATEREQUALTHAN', 'LESSEQUALTHAN', 'EQUAL', 'DIFFERENT'),
    ('left','PLUS','MINUS'),
    ('left','TIMES', 'DIVIDE'),
    ('left', 'IF', 'ELSE')
)

lex_erros = []
def t_error(t):
    lex_erros.append((t.lineno,t.lexpos,t.type,t.value, f'Unrecognized character'))
    t.lexer.skip(1)

file, extension = os.path.splitext(sys.argv[1])

data = open(sys.argv[1], 'r')

text = ""
for line in data:
    text += line

lexer = lex.lex()
lexer.input(text)