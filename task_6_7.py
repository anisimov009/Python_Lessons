# 7. *(вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта:
# передаём ему номер записи и новое значение. При этом файл не должен читаться целиком —
# обязательное требование. Предусмотреть ситуацию, когда пользователь вводит номер записи,
# которой не существует.

import sys


def clear_file(file_name):
    """
    Функция создает или очищает файл.
    :param file_name: string: имя файла
    :return:
    """
    with open(file_name, 'w', encoding='utf-8'):
        pass


# Будем построчно копировать данные из файла во временный файл, при этом изменим нужную строку.
# Потом перенесем измененные данные обратно.

NAME_SRC = 'bakery.csv'
NAME_TMP = 'temp.txt'

# Номер строки и новое значение получаем из аргументов скрипта.
_, *args = sys.argv
if len(args) > 1:
    num = int(args[0])
    val = args[1] + '\n'

    # Подготовим временный файл
    clear_file(NAME_TMP)

    # Копируем данные построчно во временный файл, при этом делаем замену строки.
    is_replace = False
    with open(NAME_SRC, 'r', encoding='utf-8') as f_src, \
         open(NAME_TMP, 'a', encoding='utf-8') as f_tmp:
        i = 0
        for line in f_src:
            i += 1
            if i == num and line != val:
                line = val
                is_replace = True
            f_tmp.write(line)

    # Копируем все обратно.
    if is_replace:
        clear_file(NAME_SRC)
        with open(NAME_SRC, 'a', encoding='utf-8') as f_src, \
             open(NAME_TMP, 'r', encoding='utf-8') as f_tmp:
            for line in f_tmp:
                f_src.write(line)
    else:
        print(f'Не найдена строка с номером {num} в файле {NAME_SRC}')
