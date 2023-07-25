mas_a = set('aeiouy')
mas_b = set('bcdfghjklmnpqrstvwxz')
str = input('Введите строку: ')
flag1 = 0
flag2 = 0
for i in range(len(str)):
    if str[i] in mas_a:
        flag1 += 1
    if str[i] in mas_b:
        flag2 += 1
print("В вашей строке ", flag1, " гласных и ", flag2, " согласных")