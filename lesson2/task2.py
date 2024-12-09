list1 = list()
print(list1)

list2 = []
print(list2)

numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers)

# Индексация как и у строк

print(numbers[-1], numbers[0])
print(numbers[2:5])
print(numbers[::-1])

# Вложенные списки

new_list = [1, 2, [5, 6, 7]]
print(new_list[2][1])

# Базовые операции со списками

list1 = [1, 2]
list2 = [3, 4, 5, 6]
print(list1 + list2)
print(list2 * 5)
print(len(list2))

list1[0] = 10
print(list1)