import sys
import os
from subprocess import call

file, extension = os.path.splitext(sys.argv[1])

if extension != ".sto":
    raise Exception("Invalid extension (.sto is required)")

path = ""
if "/" in file:
    path = file[:file.rfind("/")+1]
    file = file[file.rfind("/")+1:]
call("python3 " + "src/yacc.py " + f"{path}{file}{extension}", shell=True)

isempty = os.stat(f"./logs/erros_{file}.txt").st_size == 0

if(isempty):
    call("python3 " + f"{file}.py", shell=True)
else:
    print("Syntactic errors found")
    sys.exit(0)