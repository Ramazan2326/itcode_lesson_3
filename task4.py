list_of = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i, element in enumerate(list_of):
    if (i + 1) % 3 == 0:
        print(i, element)
