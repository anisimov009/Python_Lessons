# ЗАДАНИЕ ИЗ 4 УРОКА СДАЮ ВМЕСТЕ С 5

# 5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05

import sys
import utils

if __name__ == '__main__':
    _, *args = sys.argv
    if len(args) > 0:
        date, course = utils.currency_rates(args[0])
        print(course, date.strftime("%Y-%m-%d"))
