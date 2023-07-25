def sum_numbers(n):
    total_sum = sum(range(1, n + 1))
    print("Сумма чисел от 1 до ", n, " : ", total_sum)


try:
    n = int(input("Введите целое число n: "))
    sum_numbers(n)
except ValueError:
    print("Введено не целое число")