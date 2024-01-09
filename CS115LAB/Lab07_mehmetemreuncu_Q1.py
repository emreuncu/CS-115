from Lab07_mehmetemreuncu_module import *


def read_file(file):
    lst = []
    with open(file, "r") as file:
        for line in file:
            data = line.strip("\n").split(";")
            cab_type = data[0]
            kms = int(data[1])
            year = int(data[2])
            if cab_type == "Sedan":
                car = Sedan("Sedan", kms, year)
            else:
                car = Hatchback("Hatchback", kms, year)
            lst.append(car)
    return lst


def find_greater(cab_list, cab):
    cab_count = 0
    for c in cab_list:
        if c.get_year() > cab.get_year() and c.get_type() == cab.get_type():
            cab_count += 1
    return cab_count


num = 1
for i in read_file("cabs.txt"):
    if i.get_type() == "Sedan":
        print("Sedan", num, "will pay", i.calculate_fare(), "TL")
        num += 1
print("")
print("There are", find_greater(read_file("cabs.txt"), Sedan("Sedan", 10, 2015)),
      "Sedan cars newer than 2015")
print("")
total = 0
for i in read_file("cabs.txt"):
    if i.get_type() == "Hatchback" and i.get_year() == 2020:
        total += i.get_kms()
print("All Hatchback cars of year 2020 have travelled", total, "kms")
