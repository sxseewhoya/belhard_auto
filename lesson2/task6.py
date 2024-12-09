a = int(input('Введите три целых числа: '))
b = int(input('Введите три целых числа: '))
c = int(input('Введите три целых числа: '))

if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)