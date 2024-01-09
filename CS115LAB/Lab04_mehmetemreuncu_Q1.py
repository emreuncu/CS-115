from Lab04_mehmetemreuncu_module import *
file1 = open("city_districts.txt", "r")
file2 = open("city_values.txt", "r")
district_density(file1, file2)
file1.close()
file2.close()
while True:
    city = input("Enter city to search (“quit” to exit):")
    if city == "quit":
        print("thank you, bye")
        break
    if city != "Ankara" and city != "Istanbul":
        print(city, " not found...")
        break
    density = float(input("Enter maximum density:"))

    print(find_districts(city, density))
