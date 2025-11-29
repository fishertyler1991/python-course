from enum import Enum
import random

def _getNumberFromText(i, numberType = int):
    toReturn = None
    try:
        if numberType == int:
            toReturn = int(i)
        elif numberType == float:
            toReturn = float(i)
    except ValueError:
        print("Value is not " + str(numberType) + ".")
        pass
    return toReturn

def _SP1():
    pass

def _SP2():
    pass

def _SP3():
    pass

subProjectNames = ["sp1", "sp2", "sp3"]
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
