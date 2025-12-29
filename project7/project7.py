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
            if _confirm(prompt="Name does not exit, add birthday?", default=False):
                addDate = input("Please enter the date in the format of 3 letter month space day. Ex: SEP 21.\n?? ")
                if is_valid_month_day(addDate):
                    bdays[checkName] = addDate
                    print("Name and date added.")
                    pass
                else:
                    print("Bday entered is not valid.")
                pass
            pass
        pass
    pass

def _SP2():
    strToCheck = input("Enter a string to count.\n?? ")
    count = {}
    for c in strToCheck:
        count.setdefault(c, 0)
        count[c] = count[c] + 1
    print(count)
    pass

def _SP3():

    ALL_POS = []
    for c in _alphaRangeToString('a', 'h'):
        for i in range(1, 9):
            ALL_POS.append(c + str(i))

    STARTING_PIECES = {'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ',
        'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR', 'a7': 'bP', 'b7': 'bP',
        'c7': 'bP', 'd7': 'bP', 'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',
        'a1': 'wR', 'b1': 'wN', 'c1': 'wB', 'd1': 'wQ', 'e1': 'wK', 'f1': 'wB',
        'g1': 'wN', 'h1': 'wR', 'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP',
        'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP'}

    BOARD_TEMPLATE = """
        a    b    c    d    e    f    g    h
    ____ ____ ____ ____ ____ ____ ____ ____
    ||||||    ||||||    ||||||    ||||||    |
    8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
    ||||||____||||||____||||||____||||||____|
    |    ||||||    ||||||    ||||||    ||||||
    7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
    |____||||||____||||||____||||||____||||||
    ||||||    ||||||    ||||||    ||||||    |
    6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
    ||||||____||||||____||||||____||||||____|
    |    ||||||    ||||||    ||||||    ||||||
    5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
    |____||||||____||||||____||||||____||||||
    ||||||    ||||||    ||||||    ||||||    |
    4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
    ||||||____||||||____||||||____||||||____|
    |    ||||||    ||||||    ||||||    ||||||
    3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
    |____||||||____||||||____||||||____||||||
    ||||||    ||||||    ||||||    ||||||    |
    2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
    ||||||____||||||____||||||____||||||____|
    |    ||||||    ||||||    ||||||    ||||||
    1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
    |____||||||____||||||____||||||____||||||
    """
    
    WHITE_SQUARE = '||'
    BLACK_SQUARE = '  '

    def printState(state: dict):
        squares = []
        isSquareWhite = True
        yStr = _rangeToString(range(8, 0, -1))
        xStr = _alphaRangeToString('a', 'h')
        for y in yStr:
            for x in xStr:
                if x + y in state.keys():
                    squares.append(state[x + y])
                else:
                    if isSquareWhite:
                        squares.append(WHITE_SQUARE)
                    else:
                        squares.append(BLACK_SQUARE)
                isSquareWhite = not isSquareWhite
            pass

        print(BOARD_TEMPLATE.format(*squares))
        pass

    def validateState(state: dict):
        if not 'wK' in state.values():
            return "White does not have a King"
        elif not 'bK' in state.values():
            return "Black does not have a King"
        elif sum(1 for val in state.values() if val == "wP") > 8:
            return "White has more then 8 pawns"
        elif sum(1 for val in state.values() if val == "bP") > 8:
            return "Black has more then 8 pawns"
        elif sum(1 for val in state.values() if val == "wN") > 2:
            return "White has more then 2 knights"
        elif sum(1 for val in state.values() if val == "bN") > 2:
            return "Black has more then 2 knights"
        elif sum(1 for val in state.values() if val == "wR") > 2:
            return "White has more then 2 rooks"
        elif sum(1 for val in state.values() if val == "bR") > 2:
            return "Black has more then 2 rooks"
        elif sum(1 for val in state.values() if val == "wB") > 2:
            return "White has more then 2 bishops"
        elif sum(1 for val in state.values() if val == "bB") > 2:
            return "Black has more then 2 bishops"
        elif sum(1 for val in state.values() if val == "wQ") > 1:
            return "White has more then 1 queen"
        elif sum(1 for val in state.values() if val == "bQ") > 1:
            return "Black has more then 1 queen"
        elif sum(1 for val in state.values() if val == "wK") > 1:
            return "White has more then 1 king"
        elif sum(1 for val in state.values() if val == "bK") > 1:
            return "Black has more then 1 king"
        elif sum(1 for val in state.values() if val[0] == "w") > 16:
            return "White has more then 16 peicess"
        elif sum(1 for val in state.values() if val[0] == "b") > 16:
            return "Black has more then 16 peices"
        else:
            for p in state:
                if not p in ALL_POS:
                    return "A peice does not have a proper game board posistion."

            for v in state.values():
                if len(v) != 2:
                    return "An invalid peice is on the board."
                elif not (v[0] == 'w' or v[0] == 'b'):
                    return "A peice is not assigned to black or white."
                elif not (v[1] == 'K' or v[1] == 'Q' or v[1] == 'P' or v[1] == 'N' or v[1] == 'R' or v[1] == 'B'):
                    return "A peice is not a valid chess peice."
            pass
        return "State Valid"

    def printIntro():
        print('Interactive Chessboard')
        print('by Al Sweigart al@inventwithpython.com')
        print()
        print('Pieces:')
        print('  w - White, b - Black')
        print('  P - Pawn, N - Knight, B - Bishop, R - Rook, Q - Queen, K - King')
        print('Commands:')
        print('  move e2 e4 - Moves the piece at e2 to e4')
        print('  remove e2 - Removes the piece at e2')
        print('  set e2 wP - Sets square e2 to a white pawn')
        print('  reset - Resets pieces back to their starting squares')
        print('  clear - Clears the entire board')
        print('  fill wP - Fills entire board with white pawns.')
        print('  validate - Checks if the board is valid.')
        print('  quit - Quits the program')
    
    printIntro()

    gameInProg = True
    gameBoard = copy.copy(STARTING_PIECES)
    while gameInProg:
        printState(gameBoard)
        nextInput = input("> ").split()
        if nextInput[0][0] == "m":
            gameBoard[nextInput[2]] = gameBoard[nextInput[1]]
            del gameBoard[nextInput[1]]
        elif nextInput[0][0] == "r":
            del gameBoard[nextInput[1]]
        elif nextInput[0][0] == "s":
            gameBoard[nextInput[1]] = nextInput[2]
        elif nextInput[0][0] == "r":
            gameBoard = copy.copy(STARTING_PIECES)
        elif nextInput[0][0] == "c":
            gameBoard.clear()
        elif nextInput[0][0] == "f":
            gameBoard.clear()
            for pos in ALL_POS:
                gameBoard[pos] = nextInput[1]
        elif nextInput[0][0] == "v":
            print("Board Validation check: " + validateState(gameBoard))
        elif nextInput[0] == "quit":
            gameInProg = False
        pass
    pass

def _SP4():
    ITEM_POOL = ["Potion of Healing", \
        "Magic Sword", \
        "Ring of Protection", \
        "Wand of Magic Missiles", \
        "Cloak of Invisibility", \
        "Staff of Power", \
        "Bag of Holding", \
        "Potion of Flying", \
        "Scroll of Fireball", \
        "Amulet of Health", \
        "Boots of Speed", \
        "Ring of Invisibility", \
        "Enchanted Armor", \
        "Potion of Greater Healing", \
        "Decanter of Endless Water", \
        "Feather Fall Token", \
        "Pearl of Power", \
        "Gloves of Missile Snaring", \
        "Hat of Disguise", \
        "Immovable Rod", \
        "Driftglobe", \
        "Cloak of Elvenkind", \
        "Eyes of the Eagle", \
        "Sending Stone", \
        "Alchemy Jug"]

    def printInventory(inv: dict):
        print("Inventory")
        totalItems = 0
        for k, v in inv.items():
            print(str(v) + " " + k)
            totalItems += v
        print("Total Items: " + str(totalItems))
        pass

    def lootEnemy(inv: dict):
        newLoot = {}
        for i in range(8):
            newItem = ITEM_POOL[random.randint(0, len(ITEM_POOL) - 1)]
            newAmt = random.randint(1, 25)
            newLoot.setdefault(newItem, 0)
            newLoot[newItem] += newAmt

        for k, v in newLoot.items():
            inv.setdefault(k, 0)
            inv[k] += v
            pass
        pass

    currentInventory = {}
    for i in range(8):
        newItem = ITEM_POOL[random.randint(0, len(ITEM_POOL) - 1)]
        newAmt = random.randint(1, 25)
        currentInventory.setdefault(newItem, 0)
        currentInventory[newItem] += newAmt

    printInventory(currentInventory)

    print("Fighting dragon.")
    lootEnemy(currentInventory)
    printInventory(currentInventory)

    pass

subProjectNames = ["Friend Bday", "String char counter; dir style", "chess with dics", "Inventory"]
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

# Practice questions:
# 1. emptyDict = {,} correct {}
# 
# 2. fooDict = {'foo': 42}
# 
# 3. dicts have a value and a key but no index position, dicts are unbounded while lists are sequentional corect unordered
# 
# 4. get None, correct KeyError error
# 
# 5. no difference
# 
# 6. first looks for value second looks for keys
# 
# 7. spam['color'] = 'black', correct spam.setdefault('color', 'black')
# 
# 8. sys correct pprint.pprint()
# 