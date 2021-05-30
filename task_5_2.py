# 2. *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя
# ключевое слово yield.


def odd_nums(n):
    return (i for i in range(1, n+1, 2))


gen = odd_nums(5)
print(*gen)
