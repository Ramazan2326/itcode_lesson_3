stroke = str(input('Введите строку: '))
list_of = [i for i in stroke]
list_of_rev = reversed(list_of)
stroke_of = ''.join(list_of)
comparable_stroke = ''.join(list_of_rev)
print(stroke_of == comparable_stroke)
