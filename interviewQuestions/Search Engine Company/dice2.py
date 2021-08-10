from random import randint

def dice():
    return randint(1, 5)

def roll_7():
    while True:
        roll_1 = dice()
        roll_2 = dice()

        roll = ((roll_1 - 1)*5) + (roll_2 )
        if roll > 21:
            continue
    return roll %7 + 1

dice()
dice()
print(roll_7())