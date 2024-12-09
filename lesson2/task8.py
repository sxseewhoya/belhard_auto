name = str(input('Введите имя: '))
if len(name) > 3 and len(name) < 50:
    print('Got it!')
else:
    print('Минимальное количество символов - 3, максимальное - 50')