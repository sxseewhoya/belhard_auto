import random

number = str(random.randint(100, 999))
summ = int(number[0]) + int(number[1]) + int(number[2])
print(f'Случайное число - {number}')
print(f'Сумма цифр данного числа - {summ}')