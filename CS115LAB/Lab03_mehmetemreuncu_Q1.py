"""
 is_neat_reversible(s): takes a string s as a parameter and returns True if the input string s is neat
reversible, False otherwise.
A string is “neat reversible” if, after moving its first character to the end, reversing it results in the original
string. For example, the word “uneven” is “neat reversible” since moving its first letter, “u”, to the end gives
“nevenu”, which when reversed gives “uneven” again. 
"""


def is_neat_reversible(w):
    if w == w[0] + w[len(w):0:-1]:
        return True
    elif w == "":
        return False
    else:
        return False
