import sys

x = int(input("Enter first integer:"))
y = int(input("Enter second integer:"))
z = int(input("Enter third integer:"))

sum_of_evens = 0
max_of_evens = -sys.float_info.max
if x % 2 == 0:
    sum_of_evens += x
    if x > max_of_evens:
        max_of_evens = x
if y % 2 == 0:
    sum_of_evens += y
    if y > max_of_evens:
        max_of_evens = y
if z % 2 == 0:
    sum_of_evens += z
    if z > max_of_evens:
        max_of_evens = z
if sum_of_evens != 0:
    print("the sum of even numbers:", sum_of_evens)
    print("even max is", max_of_evens)
else:
    print("no even number is entered")
