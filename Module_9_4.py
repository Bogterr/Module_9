# Функциональное разнообразие
import os

def first_task():

    first = 'Мама мыла раму'
    second = 'Рамена мало было'

    the_standart = [False, True, True, False, False, False, False, False, True, False, False, False, False, False]

    x = list(map(lambda x, y: x == y, first, second))
    print(f'Результат: {x}')
    print(f'Эталон:    {the_standart}')

    print(f'Идентичность данных: {x == the_standart}')
    print()

first_task()

###########

def get_advanced_writer(file_name): # принимает файл для записи

    def write_everything(*data_set): # записывает весь data_set в переданный файл для записи
        writer = open(file_name, 'w', encoding='utf-8')
        for element in data_set:
            writer.write(str(element))
            writer.write('\n')
        writer.close()
        print(f'Запись переданных данных в файл: {file_name}, успешна завершена')
        os.startfile(file_name)

        return writer
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
