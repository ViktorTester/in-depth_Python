                                        # Тип данных timedelta


# Тип данных timedelta представляет собой временной интервал
# (разница между двумя объектами datetime или date) и
# используется для удобного выполнения различных
# манипуляций над типами datetime или date.

# При создании объекта timedelta можно указать следующие аргументы:
# недели (weeks)
# дни (days)
# часы (hours)
# минуты (minutes)
# секунды (seconds)
# миллисекунды (milliseconds)
# микросекунды (microseconds)

# Мы можем выбрать любые их сочетания для задания временного интервала,
# при этом все аргументы являются необязательными и по умолчанию равны 0.
from datetime import timedelta

delta = timedelta(days=7, hours=20, minutes=7, seconds=17)

print(delta)  # 7 days, 20:07:17
print(type(delta))  # <class 'datetime.timedelta'>

# Аргументы могут быть целыми числами или числами с плавающей запятой,
# а также могут быть как положительными, так и отрицательными.
# Используйте именованные аргументы, вместо позиционных, чтобы избежать ошибок.

# Тип timedelta внутренне хранит только сочетание days, seconds, microseconds,
# а остальные переданные в конструктор аргументы конвертируются в эти единицы:

# milliseconds преобразуется в 1000 microseconds
# minutes преобразуется в 60 seconds
# hours преобразуется в 3600 seconds
# weeks преобразуется в 7 days


# Атрибуты days, seconds и microseconds затем нормализуются так,
# чтобы представление было уникальным:

# 0 <= microseconds < 1000000
# 0 <= seconds < 3600 * 24 (количество секунд в одном дне)
# -999999999 <= days <= 999999999


# В следующем примере показано, как любые аргументы, кроме days, seconds,
# microseconds, объединяются и нормализуются в три результирующих сочетания.
from datetime import timedelta

delta1 = timedelta(days=50, seconds=27, microseconds=10, milliseconds=29000,
                   minutes=5, hours=8, weeks=2)
delta2 = timedelta(weeks=1, hours=23, minutes=61)
delta3 = timedelta(hours=25)
delta4 = timedelta(minutes=300)

print(delta1, delta2, delta3, delta4, sep='\n')
# 64 days, 8:05:56.000010
# 8 days, 0:01:00
# 1 day, 1:00:00
# 5:00:00

# Обратите внимание на то, что если во временном интервале
# (timedelta) значение days равно нулю, то оно не выводится.

# Также временной интервал (timedelta) может быть отрицательным.
from datetime import timedelta

delta1 = timedelta(minutes=-40)
delta2 = timedelta(seconds=-10, weeks=-2)

print(delta1)  # -1 day, 23:20:00
print(delta2)  # -15 days, 23:59:50


                                        # Атрибуты days, seconds, microseconds и метод total_seconds()


# Как уже было сказано, тип timedelta внутренне хранит только сочетание days,
# seconds, microseconds, которые можно получить с помощью одноименных атрибутов.
from datetime import timedelta

delta = timedelta(days=50, seconds=27, microseconds=10, milliseconds=29000,
                  minutes=5, hours=8, weeks=2)

print('Количество дней =', delta.days)  # Количество дней = 64
print('Количество секунд =', delta.seconds)  # Количество секунд = 29156
print('Количество микросекунд =', delta.microseconds)  # Количество микросекунд = 10
print('Общее количество секунд =', delta.total_seconds())  # Общее количество секунд = 5558756.00001
# Метод total_seconds() возвращает общее количество секунд,
# содержащееся во временном интервале timedelta.

# Обратите внимание на то, что у типа timedelta нет атрибутов hours и
# minutes, позволяющих получить количество часов и минут соответственно.
# Достать часы и минуты можно так:
from datetime import timedelta

def hours_minutes(td):
    return td.seconds // 3600, (td.seconds // 60) % 60

delta = timedelta(days=7, seconds=125, minutes=10, hours=8, weeks=2)

hours, minutes = hours_minutes(delta)

print(delta)  # 21 days, 8:12:05
print(hours)  # 8
print(minutes)  # 12


                                        # Сравнение временных интервалов


# Временные интервалы (тип timedelta) можно сравнивать
# (==, !=, <, >, <=, >=), как и любые другие типы данных.
from datetime import timedelta

delta1 = timedelta(weeks=1)
delta2 = timedelta(hours=24*7)
delta3 = timedelta(minutes=24*7*59)

print(delta1 == delta2)  # True
print(delta1 != delta3)  # True
print(delta1 < delta3)  # False

# Операторы сравнения == или != всегда возвращают значение bool,
# независимо от типа сравниваемого объекта.
from datetime import timedelta

delta1 = timedelta(seconds=57)
delta2 = timedelta(hours=25, seconds=2)

print(delta1 != 57)  # True
print(delta2 == '5')  # False

# Для всех других операторов сравнения, таких как <, >, <=, >=,
# когда объект timedelta сравнивается с объектом другого типа,
# возникает ошибка (исключение) TypeError.
from datetime import timedelta

delta1 = timedelta(seconds=57)
delta2 = timedelta(hours=25, seconds=2)

print(delta2 > delta1)     # тут все ок
print(delta2 > 5)  # TypeError: '>' not supported between instances of 'datetime.timedelta' and 'int'


                                        # Сумма и разность временных интервалов


# С помощью операторов + и - мы можем находить сумму и разность
# временных интервалов (тип timedelta).
from datetime import timedelta

delta1 = timedelta(days=5) + timedelta(seconds=3600)  # 5 дней + 1 час
delta2 = timedelta(days=5) - timedelta(seconds=3600)  # 5 дней - 1 час

print(delta1)  # 5 days, 1:00:00
print(delta2)  # 4 days, 23:00:00


                                        # Умножение временного интервала на число


# С помощью оператора * мы можем умножать временной интервал
# (тип timedelta) на целое или вещественное число (типы int и float).
from datetime import timedelta

delta1 = 48 * timedelta(hours=1)
delta2 = timedelta(weeks=1) * (3/7)

print(delta1)  # 2 days, 0:00:00
print(delta2)  # 3 days, 0:00:00

# Будьте осторожны с умножением временного интервала на вещественное
# число (тип float), так как может возникнуть округление.


                                        # Деление временных интервалов на число


# С помощью операторов / и // мы можем делить временной интервал
# (тип timedelta) на целое или вещественное число (типы int и float).
from datetime import timedelta

delta = timedelta(hours=1, minutes=6)
delta1 = delta / 2
delta2 = delta // 5

print(delta1)  # 0:33:00
print(delta2)  # 0:13:12


                                        # Деление временного интервала на временной интервал


# С помощью операторов / и // мы также можем делить один временной интервал
# (тип timedelta) на другой. По сути происходит деление общей длительности
# одного интервала на общую длительность другого интервала.
from datetime import timedelta

delta1 = timedelta(weeks=1) / timedelta(hours=5)       # обычное деление, результат float
delta2 = timedelta(weeks=1) // timedelta(hours=5)      # целочисленное деление, результат int

print(delta1)  # 33.6
print(delta2)  # 33

# Общая длительность временного интервала вычисляется
# с помощью метода total_seconds().

# Мы также можем использовать оператор нахождения остатка от деления %,
# при этом остаток вычисляется как объект timedelta.
from datetime import timedelta

delta1 = timedelta(weeks=1) % timedelta(hours=5)         # 3 часа
delta2 = timedelta(hours=1) % timedelta(minutes=7)       # 4 минуты

print(delta1)  # 3:00:00
print(delta2)  # 0:04:00

# Рассмотрим следующую задачу: рабочая смена длится
# 7 часов 30 минут, сколько полных смен в 3-х сутках?
from datetime import timedelta

all_time = timedelta(days=3)
smena = timedelta(hours=7, minutes=30)

print(all_time // smena)  # 9
print(all_time % smena)  # 4:30:00
# Таким образом, в 3-х сутках помещается 9 полных смен
# и еще останется 4 часа 30 минут.


                                        # Операции над datetime и date


# К объектам типа datetime и date можно прибавлять (вычитать)
# временные интервалы (тип timedelta), тем самым формируя новые объекты.
from datetime import datetime, date, timedelta

my_datetime1 = datetime(2021, 1, 1, 12, 15, 20) + timedelta(weeks=1, hours=25)
my_datetime2 = datetime(2021, 1, 1, 12, 15, 20) - timedelta(weeks=1, hours=25)

my_date1 = date(2021, 1, 1) + timedelta(hours=49)
my_date2 = date(2021, 1, 1) - timedelta(hours=49)

print(my_datetime1, my_datetime2, my_date1, my_date2, sep='\n')
# 2021-01-09 13:15:20
# 2020-12-24 11:15:20
# 2021-01-03
# 2020-12-30

# Обратите внимание на то, что при прибавлении временного интервала
# к дате (тип date) неполные сутки отбрасываются.

# Объект типа timedelta также возникает при вычитании
# двух дат (тип date) или дат-времён (тип datetime).
from datetime import datetime, date, timedelta

delta1 = datetime(2021, 1, 1, 12, 15, 20) - datetime(2020, 5, 1, 10, 5, 10)
delta2 = date(2020, 2, 29) - date(2019, 9, 1)
delta3 = date(2019, 9, 1) - date(2020, 2, 29)

print(delta1)  # 245 days, 2:10:10
print(delta2)  # 181 days, 0:00:00
print(delta3)  # -181 days, 0:00:00


                                        # Примечания


# Примечание 1.
# Мы можем использовать встроенные функции str() и repr() для
# преобразования объектов типа timedelta к строковому типу.
from datetime import timedelta

delta1 = timedelta(weeks=1, hours=23, minutes=61)
delta2 = timedelta(minutes=-300)

print(str(delta1), str(delta2), sep='\n')
print(repr(delta1), repr(delta2), sep='\n')
# 8 days, 0:01:00
# -1 day, 19:00:00
# datetime.timedelta(days=8, seconds=60)
# datetime.timedelta(days=-1, seconds=68400)

# Обратите внимание на то, что при печати значения объекта timedelta
# с помощью функции print() функция str() вызывается автоматически.

# Примечание 2.
# При работе с типом timedelta мы можем использовать встроенную функцию
# abs(). Функция возвращает объект timedelta
# с положительным значением всех атрибутов.
from datetime import timedelta

delta = timedelta(days=-2, minutes=-300)
abs_delta = abs(delta)

print('Исходная:', delta.days, delta.seconds, delta, sep='\n')
print('С модулем:', abs_delta.days, abs_delta.seconds, abs_delta, sep='\n')
# Исходная:
# -3
# 68400
# -3 days, 19:00:00
# С модулем:
# 2
# 18000
# 2 days, 5:00:00

# Примечание 3.
# Тип данных timedelta является неизменяемым.