print("enter '0' for exit")
while True:
    x = int(input("enter a number:"))
    y = ""
    if x == 0:
        print("please donate if you like:)")
        break
    if x < 0:
        print("please enter positive number")
    else:
        for a in range(1, x+1):
            if x % a == 0:
                if a == x:
                    y += str(a)
                else:
                    y += str(a) + ","
        print("factors of", str(x), "are:")
        print(y)
