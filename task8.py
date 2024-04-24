n = int(input("Введите количество вводимых данных в список: "))
list_of = [int(input('Введите число: ')) for i in range(n)]
fl = False
for i in range(n):
    item = list_of[i]
    list_of.pop(i)
    if item in list_of:
        fl = True
    else:
        fl = False
    list_of.insert(0, item)

if fl:
    print("Ваш список содержал дубликаты")
elif not fl:
    print("Ваш список не содержал дубликатов")
