from enum import Enum
from random import random
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')

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
    tiw = tiw = input("Enter Width (2-20): ")
    while not getNumFromIn(tiw):
        tiw = input("Enter Width (2-20): ")
    tih = tih = input("Enter Height (2-20): ")
    while not getNumFromIn(tih):
        tih = input("Enter Height (2-20): ")

    tiw = int(tiw) - 2
    tih = int(tih) - 0
    if tiw < 2:
        print("Width to small.")
        _SP1()
    elif tiw > 20:
        print("Width to big.")
        _SP1()
    elif tih < 2:
        print("Height to small.")
        _SP1()
    elif tih > 20:
        print("Height to big.")
        _SP1()
    else:
        for i in range(tih):
            print('O', end = '')
            if i == 0 or i == tih - 1:
                print('O' * tiw, end = '')
            else:
                print(' ' * tiw, end='')
            print('O')
        pass
    pass

def _SP2():
    logging.debug("Starting subprogram 2.")
    facN = input("Enter number to factorial (0-100): ")
    while _getNumberFromText(facN, numberType = int) == None:
        facN = input("Enter number to factorial (0-100): ")
    facN = int(facN)
    if facN < 0:
        logging.debug("Number to low.")
        _SP2()
    elif facN > 100:
        logging.debug("Number to high.")
        _SP2()
    else:
        facTotal = 1
        for i in range(1, facN + 1):
            facTotal *= i
            logging.debug("i is " + str(i) + ", total is " + str(facTotal))
        logging.debug("Finished subprogram: final Factorial is: " + str(facTotal))
        pass
    pass

def _SP3():
    pass

subProjectNames = ["make a box", "Logging facts", "sp3"]
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


#1.  Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.
# assert int(spam) < 10
# 2.  Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different. (That is, 'hello' and 'hello' are considered the same, as are 'goodbye' and 'GOODbye'.)
# assert type(eggs) == str and type(bacon) == str and eggs.lower() != bacon.lower() 
# 3.  Write an assert statement that always triggers an AssertionError.
# assert False
# 4.  What two lines must your program have to be able to call logging.debug()?
# import logging and logging.basicConfig
# 5.  What two lines must your program have to make logging.debug() send a logging message to a file named programLog.txt?
# the previous two lines but in basicConfig you need to set the filename argument
# 6.  What are the five logging levels?
# debug, info, warning, error, critical
# 7.  What line of code can you add to disable all logging messages in your program?
# logging.disable()
# 8.  Why is using logging messages better than using print() to display the same message?
# better control, log to file, easy to enable/disable messages
# 9.  What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?
# step over skips a function call, step in does the next line and step out finishes the current function
#10.  After you click Continue, when will the debugger stop?
# error or end of program
#11.  What is a breakpoint?
# manuel stop for a debugger
#12.  How do you set a breakpoint on a line of code in Mu?
# click the lkine number