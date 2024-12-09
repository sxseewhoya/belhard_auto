list1 = [1, 2, 3, 4, 5]

# Добавление элемента в конец списка

list1.append(10)
print(list1)

# Подставить значение на выбранную позицию

list1.insert(0, 9)
print(list1)

# Удаление из списка элемент по его имени

list1.remove(3)
print(list1)

# Удаление из списка элементы по индексу + возвращает удалённый элемент

print(list1.pop(0))
print(list1)

# Очистить список

# list1.clear()
# print(list1)

# Найти количество повторение определённого элемента в списке

print(list1.count(10))

# Определить индекс элемента в списке

print(list1.index(4))

# Скопировать список

list2 = list1.copy()
print(list2)

# Сортировка списка

list1.sort() # в порядке возрастания
print(list1)

list1.sort(reverse=True)
print(list1)

# Перевернуть список

list1.reverse()
print(list1)
