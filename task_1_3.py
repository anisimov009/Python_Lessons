# 3. Реализовать склонение слова «процент» для чисел до 20.
# Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента».
# Вывести все склонения для проверки.

for i in range(21):
    if i > 4 or i == 0:
        percent = "процентов"
    elif i > 1:
        percent = "процента"
    else:
        percent = "процент"
    print(i, percent)
