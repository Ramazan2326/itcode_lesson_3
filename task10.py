stroke = str(input("Введите строку: "))
list_of = [i for i in stroke]
for i in range(len(list_of) - 1, -1, -1):
    print(list_of[i])