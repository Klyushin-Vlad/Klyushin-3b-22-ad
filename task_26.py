def find_lcf(a, b):
    if a < b:
        for i in range(2, a + 1):
            if a % i == 0 and b % i == 0:
                return i
    else:
        for i in range(2, b + 1):
            if a % i == 0 and b % i == 0:
                return i
