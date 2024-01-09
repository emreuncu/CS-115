while True:
    x = float(input("Enter x:"))

    y = float(input("Enter y:"))

    z = float(input("Enter z:"))
    if x * y * z == 0:
        print("you cannot enter zero!!!")
    else:
        result = (x + y * z) * (x * y + z)/(x * y * z)
        print(f"f({int(x)},{int(y)},{int(z)}) ={result:.2f}")
