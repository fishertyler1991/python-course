from enum import Enum
import random, re, sys, copy

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

def _rangeToString(r: range) -> str:
    return ''.join(map(str, r))

def _alphaRangeToString(start: str, end: str | None = None, step: int = 1) -> str:
    if len(start) != 1 or (end and len(end) != 1):
        raise ValueError("start and end must be single characters")
    
    if end is None:
        base = 'a' if start.islower() else 'A'
        return ''.join(chr(i) for i in range(ord(base), ord(start) + 1))
    
    start_ord = ord(start)
    end_ord = ord(end)
    adj = 1 if step > 0 else -1
    return ''.join(chr(i) for i in range(start_ord, end_ord + adj, step))

def is_valid_month_day(text: str) -> bool:
    return bool(re.match(r"^(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC) \d{1,2}$", 
        text.strip(), re.IGNORECASE))

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
