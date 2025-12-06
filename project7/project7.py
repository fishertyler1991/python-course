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

def _confirm(prompt: str = "Confirm?", default: bool = True) -> bool:
    choices = " [Y/n]" if default else " [y/N]"
    response = input(prompt + choices + " ").strip()
    
    if not response:
        return default
    
    normalized = response.lower()
    if normalized in {'y', 'yes', 'yeah', 'yep', 'sure', 'ok', 'okay', '1'}:
        return True
    if normalized in {'n', 'no', 'nope', 'nah', '0'}:
        return False
    
    first = normalized[0]
    return first == 'y' if default else first == 'n'

threeLetterMonths = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'nov', 'dec']

def _SP1():
    bdays = {
        'alex': 'Mar 12',
        'sophia': 'Jul 25',
        'marcus': 'Nov 8',
        'emma': 'Feb 14',
        'liam': 'Sep 30',
        'olivia': 'Jan 19',
        'noah': 'Oct 4',
        'ava': 'Jun 22',
        'ethan': 'Dec 17',
        'isabella': 'Aug 9',
        'mason': 'May 31',
        'chloe': 'Apr 6',
        'lucas': 'Nov 27',
        'zoe': 'Mar 3',
        'jacob': 'Oct 15'
        }

    runsp = True
    while runsp:
        checkName = input("Enter name to check bday (exit to quit).\n?? ").lower()
        if checkName == "exit":
            runsp = False
            continue
        elif checkName in bdays:
            print(checkName + "'s bday is " + bdays[checkName] + ".")
        else:
            addName = input("No bday exists for " + checkName + ".\n Would you like to enter one?\n?? ").lower()
            if addName == "yes" or addName == "y":
                pass
            pass
        pass
    pass

def _SP2():
    pass

def _SP3():
    pass

subProjectNames = ["Friend Bday", "sp2", "sp3"]
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

