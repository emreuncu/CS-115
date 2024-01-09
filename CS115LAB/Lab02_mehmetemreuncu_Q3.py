import random

while True:
    rolls = 0
    quest = int(input("give us a dice sum:"))
    if quest == 0:
        print("thanks for choosing us")
        break
    elif quest < 2 or quest > 12:
        print("please enter valid sum!!!")
    while 2 <= quest <= 12:
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        while x + y != quest:
            rolls += 1
            x = random.randint(1, 6)
            y = random.randint(1, 6)
        print(rolls, "rolls")
        break
