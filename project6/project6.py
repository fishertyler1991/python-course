from enum import Enum
import random
import time

def _getNumberFromText(i, numberType = int, printExcept = False):
    toReturn = None
    try:
        if numberType == int:
            toReturn = int(i)
        elif numberType == float:
            toReturn = float(i)
    except ValueError:
        if printExcept:
            print("Value is not " + str(numberType) + ".")
        pass
    return toReturn

ballResponses = ["It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."]

def _SP1():
    theQ = input("Ask the ball if you dare.\n??: ")
    print(random.choice(ballResponses))
    if "yes" in input("\nAsk again?\n??: ").lower():
        _SP1()
    pass

def _SP2():
    matWidth = 70
    try:
        cols = [0] * matWidth
        while True:
            for _i in range(matWidth):
                if random.random() < 0.02:
                    cols[i] = random.randint(4, 14)
                if cols[i] <= 0:
                    print(" ", end = '')
                else:
                    print(random.choice([0, 1]), end = '')
                    cols[i] -= 1
            print()
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    pass

def _SP3():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    printVal = ""
    for i in range(len(spam)):
        if i == len(spam) - 2:
            printVal += spam[i] + ", and "
        elif i == len(spam) - 1:
            printVal += spam[i] + "."
        else:
            printVal += spam[i] + ", "
    print(printVal)
    pass

def _SP4():
    coinRes = []
    tossOps = ['H', 'T']
    for i in range(100):
        coinRes.append(random.choice(tossOps))
        pass
    print(coinRes)
    curStreakOp = coinRes[0]
    curStreakCount = 1
    maxStreakOp = coinRes[0]
    maxStreakCount = 1
    maxStreakIndex = 0
    for i in range(1, len(coinRes)):
        if coinRes[i] == curStreakOp:
            curStreakCount += 1
        else:
            curStreakOp = coinRes[i]
            if curStreakCount > maxStreakCount:
                maxStreakCount = curStreakCount
                maxStreakOp = curStreakOp
                maxStreakIndex = i
            curStreakCount = 1
    print("Largest streak is of " + maxStreakOp + " at " + str(maxStreakCount) + " occuring at index " + str(maxStreakIndex) + ".")
    pass

subProjectNames = ["Listed balls", "I'm a Hacker", "BQ: comma code", "BQ: coin streaks"]
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
    elif subProjectRunMode == 4:
        _SP4()

'''
  1.  What is []?
    an empty list
  2.  How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
    spam[2] = "hello"
For the following three questions, assume spam contains the list ['a', 'b', 'c', 'd'].

  3.  What does spam[int(int('3' * 2) // 11)] evaluate to?
    'd'
  4.  What does spam[-1] evaluate to?
    'd'
  5.  What does spam[:2] evaluate to?
    ['a', 'b']
For the following three questions, assume bacon contains the list [3.14, 'cat', 11, 'cat', True].

  6.  What does bacon.index('cat') evaluate to?
    1
  7.  What does bacon.append(99) make the list value in bacon look like?
    adds 99 to the end after True
  8.  What does bacon.remove('cat') make the list value in bacon look like?
    [3.14, 11, 'cat', True]
  9.  What are the operators for list concatenation and list replication?
    extend and copy
10.  What is the difference between the append() and insert() list methods?
    insert takes an extra argument specfiying were to insert the new data
11.  What are two ways to remove values from a list?
    remove or del[index]
12.  Name a few ways that list values are similar to string values.
    both point to an ordered collection of data instead of a single value
13.  What is the difference between lists and tuples?
    tuples are immutable (can't be changed)
14.  How do you write the tuple value that has just the integer value 42 in it?
    (42,)
15.  How can you get the tuple form of a list value? How can you get the list form of a tuple value?
    use list() or tuple()
16.  Variables that “contain” list values don't actually contain lists directly. What do they contain instead?
    pointers to the data
17.  What is the difference between copy.copy() and copy.deepcopy()?
    deepcopy copies list in list values



'''