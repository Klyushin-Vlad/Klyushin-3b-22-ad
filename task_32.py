class Schoolkid:
    def __init__(self, name, class1):
        self.name = name
        self.class1 = class1

    def study(self):
        print("Школьник учится")


schoolkid1 = Schoolkid("Георгий", "7-Б")
schoolkid1.study()