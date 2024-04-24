top_header = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
text_header = '       '.join(top_header)  # семь пробелов между днями недели
print(text_header.center(50, '_'))
list_of = [i for i in range(1, 32)]  # создаем список из 31 числа
week = list()

for i in range(len(list_of)):
    if list_of[i] % 7 == 0:
        count = 0
        number_of = str(list_of[i])
        for i in number_of:
            count += 1
        if count == 1:
            number_of = '0' + number_of
        week.append(number_of)
        week_sp = '       '.join(week)
        print(week_sp.center(50, '_'))
        week.clear()
    else:
        count = 0
        number_of = str(list_of[i])
        for i in number_of:
            count += 1
        if count == 1:
            number_of = '0' + number_of
        week.append(number_of)
week = '       '.join(week)
print(week)


