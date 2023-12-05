from lex import reserved

type_python_converter = {
    'int': 'int',
    'float': 'float',
    'char': 'str',
    'bool': 'bool',
    'string': 'str',
    'num': 'float',
}

vars_list = []
def add_var(new_var, new_var_type):
    if len(new_var) == 0:
        raise Exception("Illegal variable length")
    
    if len(vars_list) > 0 and len([item for item in vars_list if item["name"] == new_var]) > 0:
        raise Exception("variable already exists")
    elif len([item for item in list(reserved.keys()) if item == new_var]) > 0:
        raise Exception("inavlid variable name")
    else:
        vars_list.append({ 'name': new_var, 'type': new_var_type })

def check_attribution(var_name, value):
    filtered_vars = [item for item in vars_list if item["name"] == var_name]
    if len(filtered_vars) == 0:
        raise Exception("variable doesn't exists")
    
    var_in_list = filtered_vars[0]
    type_var_in_list = "<class '"+var_in_list["type"]+"'>"
    if str(type(value)) != type_var_in_list:
        raise Exception("invalid type")

def indent_code(code):
    indent = '    '
    return code.replace('\n', '\n' + indent)