from Lab03_mehmetemreuncu_Q1 import *
from Lab03_mehmetemreuncu_Q2 import *
while True:
    s = input("give me a string:")
    if s == "":
        print("bye!")
        break


    def capitalize_neat_reversible(string):
        x = 0
        sentence = ""
        for y in range(x, len(string)):
            if string[y] == " ":
                if is_neat_reversible(string[x:y]):
                    sentence += uppercase_word_at(string[x:y], 0) + " "
                else:
                    sentence += string[x:y] + " "
                x = y + 1
            if y == len(string)-1:
                if is_neat_reversible(string[x:y + 1]):
                    sentence += uppercase_word_at(string[x:y + 1], 0) + " "
                else:
                    sentence += string[x:y + 1] + " "
        return sentence


    print(capitalize_neat_reversible(s))
