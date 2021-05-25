# 2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу
# с числительными, начинающимися с заглавной буквы. Например:
# >>> >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"


def num_translate_adv(key):
    first_big = key == key.capitalize()
    val = translater_data.get(key.lower())
    if first_big and val != None:
        val = val.capitalize()
    return val


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

key = input('key: ')
print(num_translate_adv(key))
