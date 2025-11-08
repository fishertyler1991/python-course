from enum import Enum
from random import random

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