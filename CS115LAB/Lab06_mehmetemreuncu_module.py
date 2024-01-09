class Personnel:
    def __init__(self, id, name, department, status, salary):
        self.__id = id
        self.__name = name
        self.__department = department
        self.__status = status
        self.__salary = salary

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_department(self):
        return self.__department

    def get_status(self):
        return self.__status

    def get_salary(self):
        return self.__salary

    def increase_salary(self):
        if self.get_status() == "M":
            salary = int(self.get_salary() * 1.12)
            return float(salary)
        if self.get_status() == "A":
            salary = int(self.get_salary() * 1.15)
            return float(salary)
        if self.get_status() == "B":
            salary = int(self.get_salary() * 1.18)
            return float(salary)

    def __repr__(self):
        return f'Id: {self.get_id()}\n' \
               f'Name: {self.get_name()}\n' \
               f'Department: {self.get_department()}\n' \
               f'Status: {self.get_status()}\n' \
               f'Salary: {self.increase_salary()} TL\n'

    def __str__(self):
        return f'Id: {self.get_id()}\nDepartment: {self.get_department()}\nSalary: {self.increase_salary()} TL'
