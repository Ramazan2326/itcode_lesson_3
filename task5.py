number = int(input('Введите число: '))
for i in range(11):
    if i == 0:
        continue
    print(f"{number} * {i} = {number*i}")
