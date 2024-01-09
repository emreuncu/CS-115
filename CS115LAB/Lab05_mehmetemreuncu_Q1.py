def load_movies(f):
    for i in open(f, "r"):
        if i[0:4] in d:
            d[i[0:4]].append(i[5:].replace("\n", ""))
        else:
            d[i[0:4]] = []
            d[i[0:4]].append(i[5:].replace("\n", ""))
    return d


def get_movies_by_year(diction, year):
    if year in diction.keys():
        return diction[year]
    else:
        print("No movies from", year, "found")


def get_movies_by_keyword(diction, keyword):
    tl = []
    for i in diction:
        for j in diction[i]:
            if keyword in j:
                tl.append((i, j))
    if not tl:
        print("No movies with the keyword '" + keyword + "' found")
    else:
        return tl


def print_list(lst):
    if lst:
        for i in lst:
            print(i)


d = {}
load_movies("movie_data.csv")
while True:
    y = input("Enter year to search:")
    print_list(get_movies_by_year(d, y))
    k = input("Enter keyword to search:")
    print_list(get_movies_by_keyword(d, k))
