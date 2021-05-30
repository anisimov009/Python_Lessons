# ЗАДАНИЕ ИЗ 4 УРОКА СДАЮ ВМЕСТЕ С 5

# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests. В качестве API можно использовать
# http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API
# в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать
# вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
# аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.

# 3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
# которая передаётся в ответе сервера. Дата должна быть в виде объекта date.
# Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?

import requests.utils
from decimal import Decimal
from datetime import datetime


def get_nodes(input_string):
    """
    Функция раскладывает строку с узлами в формате XML в словарь.
    Вложенность узлов не поддерживается.
    Ключи с атрибутами не поддерживаются.
    :param input_string:string - строка вида '<Узел1>Значение1</Узел1><Узел2>Значение2</Узел2>'
    :return: dict (словарь): {Узел1: Значение1, Узел2: Значение2}
    """
    out_dict = {}
    nodes = input_string.split('><')
    for node in nodes:
        # Значение node в виде: 'NumCode>036</NumCode'
        pos_beg = node.find('>')
        pos_end = node.find('</')
        if pos_beg >= 0 and pos_end >=0:
            name = node[:pos_beg]
            value = node[pos_beg+1:pos_end]
            out_dict[name] = value
    return out_dict


def currency_rates(currency_code):
    """
    Функция возвращает курс валюты и дату его актуальности.
    :param currency_code: string - код валюты
    :return: (date, course) - дата курса и курс валюты
    """
    # Проверяем "кэш", чтобы не лазить каждый раз на сайт.
    # В процессе выполнения программы может смениться дата, и тогда cach станет неактуальным.
    # Проверка на актуальность здесь не реализована, но мы о ней знаем.
    global cach
    if cach is not None:
        print('Используем кэш')
        date = cach.get('date')
        courses = cach.get('courses')
    else:
        print('Получаем с сайта')
        response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        encoding = requests.utils.get_encoding_from_headers(response.headers)
        content = response.content.decode(encoding)

        # Разделим текст на блоки
        courses = {}
        splited_content = content.split('<Valute ')
        for val in splited_content[1:]:

            # Разделим блоки на узлы
            nodes = get_nodes(val)
            code = nodes.get('CharCode')
            value = nodes.get('Value')
            nominal = nodes.get('Nominal')
            if code is not None and value is not None and nominal is not None:

                # Используем decimal, а не float, потому что это деньги, и нужна точность.
                # Используем capitalize, чтобы не зависеть от регистра.
                courses[code.capitalize()] = Decimal(value.replace(',', '.')) / int(nominal)

        # Вытаскиваем дату из первой строки списка splited_content
        date = None
        pos = splited_content[0].find('Date=')
        if pos >= 0:
            date_string = splited_content[0][pos+6:pos+16]
            date = datetime.strptime(date_string, '%d.%m.%Y')

        # Инициализация кэш.
        cach = {'date': date, 'courses': courses}

    return date, courses.get(currency_code.capitalize())


# Чтобы не лазить на сайт при каждом вызове функции, объявляем глобальную переменную cach.
cach = None
print(currency_rates('EUR'))
print(currency_rates('usd'))
print(currency_rates('NONE'))
