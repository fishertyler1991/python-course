from enum import Enum
from random import random
import time, sys

def _SP1():
    indent = 0
    indent_inc = True
    spRun = True
    try:
        while spRun:
            print(' ' * indent, end = '')
            print('*' * 8)
            time.sleep(0.1)

            if indent_inc:
                indent += 1
                if indent >= 20:
                    indent_inc = False
            else:
                indent -= 1
                if indent <= 0:
                    indent_inc = True
    except KeyboardInterrupt:
        spRun = False
    pass

def _SP2():
    spRun = True
    try:
        while spRun:
            for i in range(1, 9):
                print('-' * (i*i))
                time.sleep(0.1)

            for i in range(7, 1, -1):
                print('-' * (i * i))
                time.sleep(0.1)
    except KeyboardInterrupt:
        spRun = False
    pass

def _SP3():
    pass

subProjectNames = ["Try + ascii ani", "spike ascii", "sp3"]
inputString = "Enter sub project (0 or 'exit' to exit): \n"
subProjectNum = len(subProjectNames)
for i in range(subProjectNum):
    inputString += str(i + 1) + ": " + subProjectNames[i] + "\n"
inputString += "??: "
endProgram = False

while not endProgram:
    subProjectRunMode = input(inputString)
    if subProjectRunMode.lower() == "exit":
        endProgram = True
        continue
    if not subProjectRunMode.isdigit():
        print("Only enter a number please.")
        continue
    subProjectRunMode = int(subProjectRunMode)
    if subProjectRunMode == 0:
        endProgram = True
        continue
    elif subProjectRunMode < 0 or subProjectRunMode > subProjectNum:
        print("Please enter a valid sub program.")
        continue
    
    if subProjectRunMode == 1:
        _SP1()
    elif subProjectRunMode == 2:
        _SP2()
    elif subProjectRunMode == 3:
        _SP3()
