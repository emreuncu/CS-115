def district_density(f1, f2):
    file3 = open("ankara_density.txt", "w")
    file4 = open("istanbul_density.txt", "w")
    for line1 in f1:
        if line1[0] == "A":
            line1 = line1[:-1]
            part1 = line1.find("\t")
            dist = line1[part1 + 1:len(line1)]
            file3.write(dist + ",")
            for line in f2:
                line = line[:-1]
                line = line.replace(",", "")
                part = line.find("\t")
                pop = int(line[0:part])
                area = int(line[part + 1:len(line)])
                density = str(round((pop / area), 1))
                file3.write(density + "\n")
                break
        else:
            line1 = line1[:-1]
            part1 = line1.find("\t")
            dist = line1[part1 + 1:len(line1)]
            file4.write(dist + ",")
            for line in f2:
                line = line[:-1]
                line = line.replace(",", "")
                part = line.find("\t")
                pop = int(line[0:part])
                area = int(line[part + 1:len(line)])
                density = str(round((pop / area), 1))
                file4.write(density + "\n")
                break


def find_districts(c, d):
    if c == "Ankara":
        print("Districts in Ankara with population density below " + str(d) + ":")

        for i in open("ankara_density.txt", "r"):
            i = i[:-1]
            part = i.find(",")
            dens = float(i[part + 1:len(i)])
            if dens <= d:
                print(i[0:part])
    else:
        print("Districts in Istanbul with population density below " + str(d) + ":")
        for i in open("istanbul_density.txt", "r"):
            i = i[:-1]
            part = i.find(",")
            dens = float(i[part + 1:len(i)])
            if dens <= d:
                print(i[0:part])
