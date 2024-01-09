from Lab06_mehmetemreuncu_module import *


def read_file(filename):
    file = open(filename, 'r')
    l = []
    for line in file:
        data = line.split(',')
        id = data[0]
        name = data[1]
        department = data[2]
        status = data[3]
        salary = int(data[4].replace('\n', ''))
        t = Personnel(id, name, department, status, salary)
        l.append(t)
    return l


print("All personnel:")
print(read_file('personnel.txt'))
print("""Personnel With Both Managerial 
and Academic Responsibilities:""")

dct = {}
for k in read_file('personnel.txt'):
    if k.get_status() == "B":
        dct[k.get_id()] = k
        print(k)
