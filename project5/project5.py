from enum import Enum
from random import random

def getNumFromIn(i):
    if i.isdigit():
        return int(i)
    else:
        return False

def _SP1():
    tiw = tiw = input("Enter Width: ")
    while not getNumFromIn(tiw):
        tiw = input("Enter Width: ")
    tih = tih = input("Enter Height: ")
    while not getNumFromIn(tih):
        tih = input("Enter Height: ")

    tiw = int(tiw) - 2
    tih = int(tih) - 0
    for i in range(tih):
        print('O', end = '')
        if i == 0 or i == tih - 1:
            print('O' * tiw, end = '')
        else:
            print(' ' * tiw, end='')
        print('O')
    pass

def _SP2():
    pass

def _SP3():
    pass

subProjectNames = ["make a box", "sp2", "sp3"]
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
