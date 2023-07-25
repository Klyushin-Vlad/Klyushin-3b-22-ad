n = int(input("Введите количество элементов в списке: "))
list = []
for i in range(n):
    a = int(input())
    list.append(a)
print(list)


min_1 = float('inf')
min_2 = float('inf')
for i in list:
    if i < min_1:
        min_1, min_2 = i, min_1
    elif i < min_2:
        min_2 = i

print(min_1)
print(min_2)