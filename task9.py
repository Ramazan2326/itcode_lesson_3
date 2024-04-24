n = int(input("Введите количество вводимых данных в список: "))
list_of = [int(input('Введите число: ')) for i in range(n)]
print(list_of)
for i in range(n):
    len_of_list = len(list_of)
    if i >= len_of_list:
        break
    item = list_of[i]
    list_of.pop(i)
    if item in list_of:
        continue
    else:
        list_of.insert(0, item)
print(list_of)
