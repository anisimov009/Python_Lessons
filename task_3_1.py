# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию,
# необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.


def num_translate(key_en):
    return translater_data.get(key_en)


translater_data = {'zero': 'ноль',
                   'one': 'один',
                   'two': 'два',
                   'three': 'три',
                   'four': 'четыре',
                   'five': 'пять',
                   'six': 'шесть',
                   'seven': 'семь',
                   'eight': 'восемь',
                   'nine': 'девять',
                   'ten': 'десять',
                   }

key_en = input('key: ')
print(num_translate(key_en))
