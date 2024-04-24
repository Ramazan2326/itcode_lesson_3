number = int(input("Введите число: "))
number_of = number
count = 0
while number > 0:
    number = number // 10
    count += 1
print(f"Решение через цикл While: В введенном числе {count} цифр(-ы)")

count = 0
number_of = str(number_of)
for i in number_of:
    count += 1

print(f"Решение через цикл For: В введенном числе {count} цифр(-ы)")