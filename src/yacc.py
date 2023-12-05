import ply.yacc as yacc

# Get the token map from the lexer.
from lex import *
import utils

# def p_empty(p): 
#     '''empty :
#     '''
#     p[0] = ""

def p_type(p):
    """
        type : TYPE_INT
            | TYPE_FLOAT
            | TYPE_CHAR
            | TYPE_BOOL
            | TYPE_STRING
            | TYPE_NUM
    """
    p[0] = p[1]

def p_type_value(p):
    """
        type_value : INT
                | FLOAT
                | CHAR
                | BOOL
                | STRING
                | NUM
    """
    p[0] = p[1]

def p_main(p):
    'main : BEGIN operations END'
    with open(f"{file}.py", "w") as file0, open(f"./logs/erros_{file}.txt", "w") as file1:
        file0.write(f"{p[2]}")
    file0.close()
    file1.close()

def p_operation(p):
    """operation : declaration
                | attribution
                | arithmetic
                | relational
                | logical
                | input
                | output
                | conditional
                | repetition
    """
    p[0] = p[1]

def p_operations_unit(p):
    """
        operations : operation
    """
    p[0] = p[1]

def p_operations(p):
    """
        operations : operations operation
    """
    p[0] = f'{p[1]}\n{p[2]}'

# def p_code_block(p):
#     'codeBlock : LEFTPARENTHESES operationS RIGHTPARENTHESES'
#     p[0] = p[2]

def p_declaration(p):
    'declaration : type VARIABLE'
    type = utils.type_python_converter[p[1]]
    utils.add_var(p[2], type)
    p[0] = f'{p[2]}: {type}'

def p_attribution(p):
    'attribution : VARIABLE ATTRIBUTIONSIGN type_value'
    utils.check_attribution(p[1], p[3])
    p[0] = f'{p[1]} = {p[3]}'

def p_arithmetic(p):
    """arithmetic : NUM PLUS NUM
                | NUM MINUS NUM
                | NUM TIMES NUM
                | NUM DIVIDE NUM
    """
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    else:
        p[0] = p[1] / p[3]

def p_relational(p):
    """relational : NUM EQUAL NUM
                | NUM GREATEREQUALTHAN NUM
                | NUM GREATERTHAN NUM
                | NUM LESSEQUALTHAN NUM
                | NUM LESSTHAN NUM
                | NUM DIFFERENT NUM
    """
    if p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]
    elif p[2] == '<':
        p[0] = p[1] <= p[3]
    else:
        p[0] = p[1] != p[3]

def p_logical_unit(p):
    """
        logical_unit : NOT BOOL
                    | BOOL
    """
    if p[1] == '!':
        p[0] = not p[2]
    else:
        p[0] = p[1]

def p_logical_expression(p):
    """p_logical_expression : logical_unit AND logical_unit
            | logical_unit OR logical_unit
    """
    if p[2] == '&&':
        p[0] = p[1] and p[3]
    else:
        p[0] = p[1] or p[3]

def p_logical(p):
    """logical : logical_unit AND p_logical_expression
            | logical_unit OR p_logical_expression
            | p_logical_expression AND p_logical_expression
            | p_logical_expression OR p_logical_expression
    """
    if p[2] == '&&':
        p[0] = p[1] and p[3]
    else:
        p[0] = p[1] or p[3]

def p_input(p):
    'input : INPUT LEFTPARENTHESES RIGHTPARENTHESES'
    p[0] = f'input()'

def p_output(p):
    """
        output : OUTPUT LEFTPARENTHESES type_value RIGHTPARENTHESES
    """
    p[0] = f'print({p[3]})'

def p_conditional(p):
    """
        conditional : IF LEFTPARENTHESES logical RIGHTPARENTHESES BEGIN operations END
                    | IF LEFTPARENTHESES logical RIGHTPARENTHESES BEGIN operations END ELSE BEGIN operations END
    """
    if_operations = p[6]
    else_operations = p[10]

    if_operations_ident = utils.indent_code(if_operations)
    else_operations_ident = utils.indent_code(else_operations)

    if len(p) == 8:
        p[0] = f'if {p[3]}:\n    {if_operations_ident}'
    else:
        p[0] = f'if {p[3]}:\n    {if_operations_ident}\nelse:    {else_operations_ident}'

def p_repetition(p):
    'repetition : WHILE LEFTPARENTHESES logical RIGHTPARENTHESES BEGIN operations END'
    operations = p[6]
    operations_ident = utils.indent_code(operations)

    p[0] = f'while {p[3]}:\n    {operations_ident}'


syntatic_errors = []
def p_error(p):
    if(p):
        syntatic_errors.append(p)
        print("ERROR: ", p)

parser = yacc.yacc(start = 'main')
errorlog=lex.NullLogger(),
result = parser.parse(text)