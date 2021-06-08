# 6.5. **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было
# задать имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта.

import sys

_, *args = sys.argv
if len(args) == 3:
    name_users = args[0]
    name_hobby = args[1]
    name_output = args[2]

    with open(name_users, 'r', encoding='utf-8') as f_users, \
         open(name_hobby, 'r', encoding='utf-8') as f_hobby, \
         open(name_output, 'w', encoding='utf-8') as f_output:

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
