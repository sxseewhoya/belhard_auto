summ = float(input('Введите сумму заказа в ресторане: '))
tax = 4 * summ / 100
tip = 18 * summ / 100
print(f'Налог составил - {round(tax, 2)} рублей, \nЧаевые - {round(tip, 2)} рублей, \nИтог - {round(summ + tax + tip, 2)} рублей')