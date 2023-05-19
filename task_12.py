class Student:

    def __init__(self, name, surname, course, grades):
        self.name = name
        self.surname = surname
        self.course = course
        self.grades = grades

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)
