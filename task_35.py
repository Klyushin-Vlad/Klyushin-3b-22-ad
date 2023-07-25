n = int(input("Введите число: "))
a = 0
b = 1
while n:
    print(a)
    a, b = b, a + b
    n -= 1