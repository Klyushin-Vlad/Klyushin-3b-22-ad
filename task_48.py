a = [5, 7, 11, 13, 15, 20, 25]
sum = 0
count = 0
for i in range(len(a)):
    if a[i] > 10:
        sum += a[i]
        count += 1
print(sum / count)