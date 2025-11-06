print("Enter Project subsection: ")
print("a: psyop b: bad calc c: cond test")
subProjectRun = input("??: ")
if subProjectRun == 'a':
    #Project 2a: PsyOp Day

    today_is_psyop = True
    say_psyop = None

    if today_is_psyop:
        say_psyop = True
    else:
        say_psyop = False

    #condesnes to say_psyop = today_is_psyop

    if today_is_psyop:
        say_psyop = not say_psyop

    if say_psyop:
        print("Today is psyop")
    else:
        print("Today is not psyop")

    pass

elif subProjectRun == 'b':
    #Project 2b: bad cap calc

    print("Enter TB or GB for the ad dawg: ")
    unit = input("??: ")
    if unit == "TB" or unit == "tb":
        #to lower lol
        disc = 1000000000000 / 1099511627776
    elif unit == "GB" or unit == "gb":
        disc = 1000000000 / 1073741824

    print("Enter ad'd cap dawg: ")
    adcap = input("??: ")
    adcap = float(adcap)

    realcap = str(round(adcap * disc, 2))

    print("Real cap is " + realcap + " " + unit)

    pass

#1. True, False
#
#2. and or not
#
#3. no
#
#4. False, False, True, False, False, True
#
#5. ==, !=, >, <, >=, <=
#
#6. one evulates the other assigns
#
#7. condion evulats to True of False, most used in if blocks and similar
#
#8. spam == 10: if block, spam > 5: if block, else, else block
#
#9. 

elif subProjectRun == 'c':
    spam = int(input("Enter a number: "))
    if spam == 1:
        print("Hello")
    elif spam == 2:
        print("Howdy")
    else:
        print("Greetings!")