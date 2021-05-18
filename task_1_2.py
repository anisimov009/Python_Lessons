# 2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# * К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.


MAX_NUMBER = 1000
sum_of_numbers = 0

# Создаем список
list_numbers = [i ** 3 for i in range(1, MAX_NUMBER, 2)]
for i in list_numbers:

    # Считаем сумму цифр числа i
    remains = i
    sum_of_digits = 0
    while remains > 0:
        sum_of_digits += remains % 10
        remains //= 10

    # Проверяем, делится ли сумма цифр на 7
    if sum_of_digits % 7 == 0:
        sum_of_numbers += i

print('Сумма чисел =', sum_of_numbers)

# Добавляем по 17 к каждому элементу и еще раз вычисляем сумму.
sum_of_numbers = 0
for i in range(len(list_numbers)):
    list_numbers[i] += 17

    # Считаем сумму цифр числа list_numbers[i]
    remains = list_numbers[i]
    sum_of_digits = 0
    while remains > 0:
        sum_of_digits += remains % 10
        remains //= 10

    # Проверяем, делится ли сумма цифр на 7
    if sum_of_digits % 7 == 0:
        sum_of_numbers += list_numbers[i]

print('Сумма чисел =', sum_of_numbers)

