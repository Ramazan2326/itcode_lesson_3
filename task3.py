"""
В цикле for нужно явно задать стартовое значение итератора равное 1
"""

number = int(input('Введите число, факториал которого нужно найти: '))
factorial = 1
for num in range(1, number + 1):
    factorial *= num
    print(factorial)
print(f"{number}! = {factorial}")
