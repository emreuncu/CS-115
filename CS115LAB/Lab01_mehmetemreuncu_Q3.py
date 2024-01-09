x = input("Enter first name:")
y = input("Enter second name:")
z = input("Enter third name:")

max_name = '0'

if len(x) > len(max_name):
    max_name = x
if len(y) > len(max_name):
    max_name = y
if len(z) > len(max_name):
    max_name = z

if len(x) == len(y) == len(max_name):
    print(x, "'s name is longest, but there is a tie!")
elif len(x) == len(z) == len(max_name):
    print(x, "'s name is longest, but there is a tie!")
elif len(y) == len(z) == len(max_name):
    print(y, "'s name is longest, but there is a tie!")
else:
    print(max_name, "'s name is longest")
