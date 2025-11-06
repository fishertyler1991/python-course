from enum import Enum
import random


subProjectNames = ["Guess number", "RPS", "sp3"]
inputString = "Enter sub project: \n"
subProjectNum = len(subProjectNames)
for i in range(subProjectNum):
    inputString += str(i+1) + ": " + subProjectNames[i] + "\n"
inputString += "??: "
subProjectRunMode = int(input(inputString)) - 1



if subProjectRunMode == 0:
    #Guess some dumb number lol
    dumbNum = random.randint(1, 20)
    guessNum = -1
    chances = 0
    maxC = 7
    win = True
    while dumbNum != guessNum:
        print("Guess that number bicycle (1 - 20).")
        guessNum = input("??: ")

        if type(guessNum) != int:
            if guessNum == "exit":
                win = False
                break
            print("Only Int's plx.")
            continue
        else:
            guessNum = int(guessNum)

        if guessNum != dumbNum:
            if guessNum < dumbNum:
                print("too low dawg.")
            else:
                print("too high baby")

            chances += 1
            if chances >= maxC:
                win = False
                break
        pass
    if not win:
        print("you lose. the number was: " + str(dumbNum))
    else:
        print("you win. Turns: " + str(chances))

    pass

elif subProjectRunMode == 1:
    #Rock paper sics baby
    result = 0
    class RPS_OPS(Enum):
        ROCK = 0
        PAPER = 1
        SICS = 2

    def checkPoints(cp):
        if cp[0] >= 2:
            return 1
        elif cp[1] >= 2:
            return 2
        else:
            return 0

    player_choice = None
    ai_choice = None
    points = [0, 0]

    def checkMatch():
        pc = player_choice
        ac = ai_choice

        print("You: " + RPS_OPS(pc).name + " AI: " + RPS_OPS(ac).name)
        if pc == ac:
            print("Result: Tie")
            return 0
        elif (pc == 0 and ac == 2) or (pc == 1 and ac == 0) or \
            (pc == 2 and ac == 1):

            print("You win.")
            return 1

        else:
            print("You lose")
            return 2

    while checkPoints(points) == 0:
        print("Current Score\nYou: " + str(points[0]) + \
            "\nAI: " + str(points[1]))
        ai_choice = random.randint(0, 2)
        player_choice = int(input( \
            "Rock 0, Paper 1, Siccors 2\n??: "))

        res = checkMatch()
        if res == 1:
            points[0] += 1
        elif res == 2:
            points[1] += 1

    finRes = checkPoints(points)
    if finRes == 1:
        print("YOU WIN YAY!")
    else:
        print("OH NOOOO")
    pass

