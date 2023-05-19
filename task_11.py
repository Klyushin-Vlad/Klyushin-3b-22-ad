class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def info(self):
        print("Breed:", self.breed, "\nName:", self.name, "\nAge:", self.age)
