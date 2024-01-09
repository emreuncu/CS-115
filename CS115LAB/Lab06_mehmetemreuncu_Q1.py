list_2d = [['This', 'is', 'lab', 'Script'],
           ['We', 'should', 'finish', 'it'],
           ['we', 'solve', 'some', 'questions']]


def form_equal_length(lst, integer):
    sent = ""
    for i in range(len(lst[0])):
        for n in range(len(lst)):
            if len(lst[n][i]) == integer:
                if sent == "":
                    sent += lst[n][i].replace(lst[n][i][0], lst[n][i][0].upper())
                else:
                    sent += " " + lst[n][i].lower()
    return sent


print("Sentence:", form_equal_length(list_2d, 6))
