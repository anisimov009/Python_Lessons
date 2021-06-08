# 6.4. *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём
# ОЗУ (разумеется, не нужно реально создавать такие большие файлы, это просто задел на
# будущее проекта). Только теперь не нужно создавать словарь с данными. Вместо этого нужно
# сохранить объединенные данные в новый файл (users_hobby.txt). Хобби пишем через
# двоеточие и пробел после ФИО:

# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи

with open('users.csv', 'r', encoding='utf-8') as f_users, \
     open('hobby.csv', 'r', encoding='utf-8') as f_hobby, \
     open('users_hobby.txt', 'w', encoding='utf-8') as f_output:

    line_user = f_users.readline()
    line_hobby = f_hobby.readline()
    while line_user:
        if line_hobby:
            hobby = line_hobby.strip()
        else:
            hobby = 'None'
        f_output.write(': '.join([line_user.strip(), hobby]) + '\n')
        line_user = f_users.readline()
        line_hobby = f_hobby.readline()

    if line_hobby:
        exit(1)
