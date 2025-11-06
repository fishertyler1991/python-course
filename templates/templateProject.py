from enum import Enum
from random import random


subProjectNames = ["sp1", "sp2", "sp3"]
inputString = "Enter sub project: \n"
subProjectNum = len(subProjectNames)
for i in range(subProjectNum):
    inputString += str(i) + ": " + subProjectNames[i] + "\n"
inputString += "??: "
subProjectRunMode = input(inputString)

