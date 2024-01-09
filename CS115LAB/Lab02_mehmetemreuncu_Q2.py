x = "a"

while x != "":
    y = ""
    x = input("give a string:")
    if x == "":
        print("ok")
        break
    for i in range(0, len(x), 2):
        y += x[i]
    for m in range(1, len(x), 2):
        y += x[m]
    print(y)
