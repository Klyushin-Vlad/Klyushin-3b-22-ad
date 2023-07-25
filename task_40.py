try:
    file = open('text.txt')
    file.close()
    print("Файл существует")
except:
    print("Файл не найден")