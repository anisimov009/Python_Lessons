# 6.3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
# и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь
# в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше
# записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из
# скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз
# меньше объема ОЗУ.

# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович

# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи

import json


def get_item(input_list, i):
    """
    Функция возвращает i-тый элемент списка, а если его нет (IndexError), то None.
    Возвращаемое значение очищается от управляющих символов.
    :param input_list: список
    :param i: индекс нужного элемента
    :return: input_list[i] или None
    """
    # Можно сделать через if
    if i < len(input_list):
        val = input_list[i].strip()
    else:
        val = None

    # Можно сделать через try
    try:
        val = input_list[i].strip()
    except IndexError:
        val = None

    return val


def get_list(file_name):
    """
    Функция возвращает список строк из файла.
    :param file_name: str: имя файла.
    :return: list: список строк.
    """
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.readlines()


# Написать код, загружающий данные из обоих файлов
users = get_list('users.csv')
hobby = get_list('hobby.csv')

len_users = len(users)
if len_users >= len(hobby):

    # .. и формирующий из них словарь: ключи — ФИО, значения — данные о хобби
    out_dict = {users[i].strip(): get_item(hobby, i) for i in range(len_users)}
    print('dict: ', type(out_dict), out_dict)

    # Сохранить словарь в файл.
    file_name = 'users_hobby.txt'
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(out_dict, f)

    # Проверить сохранённые данные.
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
        print('data: ', type(data), data)

else:

    # Если количество пользователей меньше количества хобби, выходим из скрипта с кодом «1».
    exit(1)
