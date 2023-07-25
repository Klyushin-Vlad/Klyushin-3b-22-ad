def task_23(mass: list):
    try:
        mass.index(int(input()))
        print("Число найдено в массиве",)
    except:
        print("Число не найдено в массиве")

mass = [1, 2, 3, 4, 7]
task_23(mass)