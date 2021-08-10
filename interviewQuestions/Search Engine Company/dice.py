from random import randint

def dice():
    return randint(1, 7)

def roll_5():
    roll = 7
    
    while roll > 5:
        roll = dice()
        print("The dice has rolled",roll)
    print("Final roll",roll)

dice()
print(roll_5())
