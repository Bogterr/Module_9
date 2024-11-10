# Лекция ленивые вычисления

list_1 = [1, 5, 9, 29, 4]
list_2 = [5, 2, 9, 1, 2]

# прогон от и до
ran = range(10, 30)
# заворачивает попарно элементы списков в кортежи
zp = zip(list_1, list_2)
# прогон по списку преобразование элементов списка в str
mp = map(str, list_1)

print(ran, zp, mp)

print()
print(list(ran))
print(list(zp))
print(list(mp))
print()

# ДЗ Генераторные сборки
print('ДЗ: "Генераторные сборки"')

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
print(list(first_result))

second_result = ((len(first[x]) == len(second[x])) for x in range(len(first)))
print(list(second_result))