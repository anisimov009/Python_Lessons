# Реализовать вывод информации о промежутке времени в зависимости от его
# продолжительности duration в секундах:
# a. до минуты: <s> сек;
# b. до часа: <m> мин <s> сек;
# c. до суток: <h> час <m> мин <s> сек;
# d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = SECONDS_PER_MINUTE * 60
SECONDS_IN_DAY = SECONDS_PER_HOUR * 24
SECONDS_PER_MONTH = SECONDS_IN_DAY * 30
SECONDS_IN_YEAR = SECONDS_PER_MONTH * 12

duration = int(input("Input duration: "))

years = duration // SECONDS_IN_YEAR
remains = duration % SECONDS_IN_YEAR

months = remains // SECONDS_PER_MONTH
remains = remains % SECONDS_PER_MONTH

days = remains // SECONDS_IN_DAY
remains = remains % SECONDS_IN_DAY

hours = remains // SECONDS_PER_HOUR
remains = remains % SECONDS_PER_HOUR

minutes = remains // SECONDS_PER_MINUTE
seconds = remains % SECONDS_PER_MINUTE

if years > 0:
    print(years, 'г', months, 'мес', days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')

elif months > 0:
    print(months, 'мес', days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')

elif days > 0:
    print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')

elif hours > 0:
    print(hours, 'час', minutes, 'мин', seconds, 'сек')

elif minutes > 0:
    print(minutes, 'мин', seconds, 'сек')

else:
    print(seconds, 'сек')
