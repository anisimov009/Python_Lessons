﻿# ЗАДАНИЕ ИЗ 4 УРОКА СДАЮ ВМЕСТЕ С 5

# 4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
# Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.

import utils

print(utils.currency_rates('USD'))
print(utils.currency_rates('EUR'))
print(utils.currency_rates('BBB'))
