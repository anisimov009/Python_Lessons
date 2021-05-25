# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из двух случайных слов,
# взятых из трёх списков:
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
#
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
#
# Сможете ли вы сделать аргументы именованными?

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n=4, rep_words=True):
    """
    Функция возвращает n шуток, сформированных из списков nouns, adverbs, adjectives

    :param n:int - количество шуток
    :param rep_words:boolean - использовать ли повторы слов в шутках (по умолчанию True)
    :return:list - список из n шуток
    """
    if rep_words:
        selection_method = random.choices
    else:
        selection_method = random.sample

    out_list = list(zip(selection_method(nouns, k=n),
                        selection_method(adverbs, k=n),
                        selection_method(adjectives, k=n)))
    return out_list


print(help(get_jokes))
print()
print('С повторами:  ', get_jokes(n=4))
print('Без повторов: ', get_jokes(rep_words=False))
