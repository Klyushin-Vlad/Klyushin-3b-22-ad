class Employer:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def performance(self):
        print("Name:", self.name, "\nAge:", self.age,"\nSalary:", self.salary)


emp = Employer("name1", 3, 4)
emp.performance()