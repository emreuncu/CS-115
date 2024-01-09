import time


class Nation:
    def __init__(self, cName, continent, pop, sa):
        self.__country = cName
        self.__continent = continent
        self.__population = pop
        self.__surface_area = sa
        self.__density = self.calculate_density()

    def getCountry(self):
        return self.__country

    def getContinent(self):
        return self.__continent

    def getPopulation(self):
        return self.__population

    def getSurface_area(self):
        return self.__surface_area

    def getDensity(self):
        return self.__density

    def calculate_density(self):
        return float(self.__population) / float(self.__surface_area)

    def __lt__(self, other):
        return self.__country < other.__country

    def __str__(self):
        s = 'Country: ' + self.__country + '\n'
        s += 'Continent: ' + self.__continent + '\n'
        s += 'Density: ' + str(self.__density) + '\n'

        return s

    def __repr__(self):
        s = 'Country: ' + self.__country + '\n'
        s += 'Continent: ' + self.__continent + '\n'
        s += 'Population: ' + str(self.__population) + '\n'
        s += 'Area: ' + str(self.__surface_area) + '\n'
        s += 'Density: ' + str(self.__density) + '\n'

        return s


def bubbleSort(c_list):
    i = False
    j = 0
    while j < len(c_list) - 1 and not i:
        i = True
        for k in range(len(c_list) - 1 - j):
            if c_list[k].getContinent() > c_list[k + 1].getContinent():
                i = False
                t = c_list[k]
                c_list[k] = c_list[k + 1]
                c_list[k + 1] = t
            elif c_list[k].getContinent() == c_list[k + 1].getContinent() and c_list[k].getCountry() > c_list[
                k + 1].getCountry():
                i = False
                t = c_list[k]
                c_list[k] = c_list[k + 1]
                c_list[k + 1] = i
        j += 1


def searchCountries(c_list, cntry, i, e):
    if i == -1:
        return e
    else:
        if c_list[i].getCountry() == cntry:
            e.append(c_list[i])
    return searchCountries(c_list, cntry, i - 1, e)


def readCountries(c_list, filename):
    file = open(filename, 'r')
    for line in file:
        data = line.split(';')
        c_list.append(Nation(data[0], data[1], data[2], data[3].replace("\n", "")))
    return c_list


lst = []
readCountries(lst, "nations.txt")
lst.sort()
print("Nations Sorted according to their Names:")
print(lst)
for x in searchCountries(lst, input("Enter the name of the country to search:"), len(lst) - 1, []):
    time.sleep(1)
    print(f'{x}')
    if x == "":
        print("Country does not exist!!!")
time.sleep(1)
print("Nations Sorted according to their Continent and Name:")
time.sleep(1)
bubbleSort(lst)
print(lst)
