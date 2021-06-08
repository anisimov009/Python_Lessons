# 6.1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
# web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
# Например:
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]

out_list = []
with open('nginx_logs.txt') as f:
    for line in f:
        elements_line = line.split(' ')
        if len(elements_line) > 5:
            out_list.append((elements_line[0],
                             elements_line[5].replace('"', ''),
                             elements_line[6]))

# Выводим первые 7 значений из списка
print(*out_list[:7], sep='\n')
