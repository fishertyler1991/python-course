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
    spRun = True
    stepToOne = 0

    def isEven(num):
        return num % 2 == 0

    try:
        while spRun:
            inNum = input("Enter your fated num: ")
            if not inNum.isdecimal():
                print("please enter a number")
            else:
                inNum = int(inNum)
                while inNum is not 1:
                    print(inNum)
                    stepToOne += 1
                    if isEven(inNum):
                        inNum = inNum // 2
                    else:
                        inNum = (3 * inNum) + 1
                pass
            print("Reached One after " + str(stepToOne) + " steps.")
            pass
    except KeyboardInterrupt:
        spRun = False
    pass

subProjectNames = ["Try + ascii ani", "spike ascii", "PP1"]
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
    
#1. run the same code with slight changes over and over
#
#2. function is called
#
#3. def
#
#4. function defines the code, a call executes the defined code
#
#5. one global scope, infinite local scopes
#
#6. eliminated from memory
#
#7. a value returned by a function, yes
#
#8. None
#
#9. by not setting it as a local variable
#
#10. NoneType
#
#11. imports the named python file if it exists (not typeing that lol)
# (i'd assume its a function that returns all pets named eric)
#
#12. from spam imort bacon or import bacon and used as bacon.spam()
#
#13. try-except statements
#
#14. the attempt to do code goes in try, if any failure occurs
#   goes in except
#
#15. the code that generates the random number only happens once, therefore
#   every check is against that single initial roll
#PP1 collatz