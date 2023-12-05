# Scripto

Ana Júlia Gonçalves Alvarenga - 2020001751
Fernanda Pereira de Sene - 2020026330

## 1. Expressões Regulares

digit = {0-9}
letter = {a-zA-Z}
variable = {letter}{char}*

### 1.1. Tipos de Dados

int = ("-")?{digit}+
float = ("-")?{digit}+{dot}{digit}+
char = "{letter}|{digit}"
bool = "true"|"false"
string = char+
num = int | float

### 1.2. Comandos

attributionSign = "="
inputCommand = "input"
outputCommand = "print"
if = "if"
else = "else"
while = "while"

### 1.2. Operadores Relacionais

equal = "=="
greaterThan = ">"
greaterEqualThan = ">="
lessThan = "<"
lessEqualThan = "<="
different = "!="

### 1.3. Operadores Lógicos

and = "&&"
or = "||"
not = "!"

### 1.4. Operadores Aritméticos

sum = "+"
sub = "-"
mult = "*"
div = "/"
mod = "%"

### 1.5. Símbolos Especiais

begin = "{"
end = "}"
leftParentheses = "("
rightParentheses = ")"
dot = "."

### 1.6. Palavras Reservadas

type = "int"|"float"|"char"|"bool"|"string"|"num"
booleanValues = "true"|"false"
commandWords = "input"|"print"|"if"|"else"|"while"

## 2. Operações da linguagem

codeBlock = begin{operations}+end

main = main codeBlock

operation = declaration | attribution | arithmetic | relational | logical | input | output | conditional | repetition

declaration = type variable

attribution = variable attributionSign type

arithmetic = num(sum | sub | mult | div | mod)num

relational = num(equal | greaterThan | greaterEqualThan | lessThan | lessEqualThan | different)num

logical = not?(bool){(and | or)not?(bool)}*

input = inputCommand leftParentheses (char | int | float | bool | string) rightParentheses

output = outputCommand leftParentheses (char | int | float | bool | string)rightParentheses

conditional = if leftParentheses logical rightParentheses begin {operation}+ end {else begin {operation}* end}?

repetition = while leftParentheses logical rightParentheses begin {operation}* end

## 3. Tokens

| Definição | Token |
| ----------- | ----------- |
| variable | VARIABLE |
| int | INT |
| float | FLOAT |
| num | NUM |
| char | CHAR |
| bool | BOOL |
| string | STRING |
| type | TYPE |
| codeBlock | CODE_BLOCK |
| main | MAIN |
| operation | OPERATION |
| declaration | DECLARATION |
| attribution | ATTRIBUTION |
| arithmetic | ARITHMETIC |
| relational | RELATIONAL |
| logical | LOGICAL |
| input | INPUT |
| output | PRINT |
| conditional | CONDITIONAL |
| repetition | REPETITION |

## 4. Autômatos

<center>
    <img
        src="/assets/images/variable.png"
        alt="variable"
    >
</center>
<center>
    Figura 1 - TOKEN VARIABLE
</center>
<br/>
<br/>
<center>
    <img
        src="/assets/images/int.png"
        alt="int"
    >
</center>
<center>
    Figura 2 - TOKEN INT
</center>
<br/>
<br/>
<center>
    <img
        src="/assets/images/int-thomson.png"
        alt="int"
    >
</center>
<center>
    Figura 3 - TOKEN INT Thompson
</center>
<br/>
<br/>
<center>
    <img
        src="/assets/images/float.png"
        alt="float"
    >
</center>
<center>
    Figura 4 - TOKEN FLOAT
</center>
<br/>
<br/>
<center>
    <img
        src="/assets/images/float-thompson.png"
        alt="float"
    >
</center>
<center>
    Figura 5 - TOKEN FLOAT Thompson
</center>
<br/>
<br/>
<center>
    <img
        src="/assets/images/num.png"
        alt="num"
    >
</center>
<center>
    Figura 6 - TOKEN NUM
</center>
<br/>
<br/>
<center>
    <img
        src="/assets/images/char.png"
        alt="char"
    >
</center>
<center>
    Figura 7 - TOKEN CHAR
</center>
<br/>
<br/>
<center>
    <img
        src="/assets/images/string.png"
        alt="string"
    >
</center>
<center>
    Figura 8 - TOKEN STRING
</center>
<br/>
<br/>
<center>
    <img
        src="/assets/images/type.png"
        alt="type"
    >
</center>
<center>
    Figura 9 - TOKEN TYPE
</center>
<br/>
<br/>
<center>
    <img
        src="/assets/images/codeBlock.png"
        alt="codeBlock"
    >
</center>
<center>
    Figura 10 - TOKEN CODE_BLOCK
</center>
<br/>
<br/>
<center>
    <img
        src="/assets/images/operation.png"
        alt="operation"
    >
</center>
<center>
    Figura 11 - TOKEN OPERATION
</center>
<br/>
<br/>
<center>
    <img
        src="/assets/images/declaration.png"
        alt="declaration"
    >
</center>
<center>
    Figura 12 - TOKEN DECLARATION
</center>
<br/>
<br/>
<center>
    <img
        src="/assets/images/attribution.png"
        alt="attribution"
    >
</center>
<center>
    Figura 13 - TOKEN ATTRIBUTION
</center>
<br/>
<br/>
<center>
    <img
        src="/assets/images/arithmetic.png"
        alt="arithmetic"
    >
</center>
<center>
    Figura 14 - TOKEN ARITHMETIC
</center>
<br/>
<br/>
<center>
    <img
        src="/assets/images/relational.png"
        alt="relational"
    >
</center>
<center>
    Figura 15 - TOKEN RELATIONAL
</center>
<br/>
<br/>
<center>
    <img
        src="/assets/images/logical.png"
        alt="logical"
    >
</center>
<center>
    Figura 16 - TOKEN LOGICAL
</center>
<br/>
<br/>
<center>
    <img
        src="/assets/images/logical-thompson.png"
        alt="logical"
    >
</center>
<center>
    Figura 17 - TOKEN LOGICAL Thompson
</center>
<br/>
<br/>
<center>
    <img
        src="/assets/images/input.png"
        alt="input"
    >
</center>
<center>
    Figura 18 - TOKEN INPUT
</center>
<br/>
<br/>
<center>
    <img
        src="/assets/images/output.png"
        alt="output"
    >
</center>
<center>
    Figura 19 - TOKEN PRINT
</center>
<br/>
<br/>
<center>
    <img
        src="/assets/images/conditional.png"
        alt="conditional"
    >
</center>
<center>
    Figura 20 - TOKEN CONDITIONAL
</center>
<br/>
<br/>
<center>
    <img
        src="/assets/images/repetition.png"
        alt="repetition"
    >
</center>
<center>
    Figura 21 - TOKEN REPETITION
</center>