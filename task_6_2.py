# 6.2. *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла
# логов из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать
# даже с файлами, размер которых превышает объем ОЗУ компьютера.


# Создаем словарь: ключом будет ip-адрес, значением - количество вызовов.
number_of_calls = {}

# Читаем файл построчно, чтобы не загружать ОЗУ.
with open('nginx_logs.txt') as f:
    for line in f:
        elements_line = line.split(' ')
        if len(elements_line) > 0:
            remote_addr = elements_line[0]
            stat = number_of_calls.setdefault(remote_addr, 0)
            number_of_calls[remote_addr] += 1

# Сортируем словарь по значениям.
sorted_keys = sorted(number_of_calls, key=number_of_calls.get)

# Получили список, в нем последнее значение - ключ, который нам нужен.
remote_addr = sorted_keys[-1]
print(remote_addr, number_of_calls[remote_addr])
