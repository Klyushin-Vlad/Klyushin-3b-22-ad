import random

mass = []
for i in range(0, 10):
    mass.append(random.randint(1, 101))
print(max(mass), min(mass))