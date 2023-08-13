                                        # Тип данных datetime


# Типы данных date и time позволяют работать по отдельности с датами и временами.
# Однако на практике чаще требуется работать одновременно и с датой,
# и со временем. Для таких целей используется тип
# данных datetime из одноименного модуля datetime.

# Чтобы иметь возможность использовать этот тип данных,
# необходимо предварительно его импортировать из модуля datetime:
from datetime import datetime

# При создании новой даты-времени (тип datetime) нужно указать год,
# месяц, день, часы, минуты, секунды и микросекунды. При этом год,
# месяц и день являются обязательными, а часы, минуты,
# секунды и микросекунды необязательными.
from datetime import datetime

my_datetime = datetime(1992, 10, 6, 9, 40, 23, 51204)    # создаем полную дату-время
only_date = datetime(2021, 12, 31)                       # создаем дату-время с нулевой временной информацией

print(my_datetime)  # 1992-10-06 09:40:23.051204
print(only_date)  # 2021-12-31 00:00:00
print(type(my_datetime))  # <class 'datetime.datetime'>

# Конструктор типа datetime сначала принимает год, месяц, день, часы,
# минуты, секунды, а уже потом микросекунды. Мы также можем использовать
# именованные аргументы, нарушая указанный порядок datetime(day=6, month=10,
# year=1992, second=23, minute=40, microsecond=51204, hour=9).

# Так же, как и при работе с типами date и time, пользуясь типом datetime,
# можно получать доступ к отдельным значениям созданной даты-времени:
# годам, месяцам, дням, часам, минутам, секундам и микросекундам.
# Получить доступ к ним можно с помощью атрибутов:

# year — год
# month — месяц
# day — день
# hour — час
# minute — минуты
# second — секунды
# microsecond — микросекунды
from datetime import datetime

my_datetime = datetime(1992, 10, 6, 9, 40, 23, 51204)

print('Год =', my_datetime.year)  # Год = 1992
print('Месяц =', my_datetime.month)  # Месяц = 10
print('День =', my_datetime.day)  # День = 6
print('Часы =', my_datetime.hour)  # Часы = 9
print('Минуты =', my_datetime.minute)  # Минуты = 40
print('Секунды =', my_datetime.second)  # Секунды = 23
print('Микросекунды =', my_datetime.microsecond)  # Микросекунды = 51204


                                        # Методы combine(), date(), time()


# Сформировать новый объект типа datetime можно с помощью двух разных объектов,
# представляющих дату и время (date и time).
# Для этого используется метод combine().
from datetime import date, time, datetime

my_date = date(1992, 10, 6)
my_time = time(10, 45, 17)
my_datetime = datetime.combine(my_date, my_time)

print(my_datetime)  # 1992-10-06 10:45:17

# Если, наоборот, нужно получить из даты-времени (тип datetime) по отдельности
# дату (тип date) и время (тип time), то используются
# методы date() и time() соответственно.
from datetime import datetime

my_datetime = datetime(2022, 10, 7, 14, 15, 45)
my_date = my_datetime.date()                     # получаем только дату (тип date)
my_time = my_datetime.time()                     # получаем только время (тип time)

print(my_datetime, type(my_datetime))  # 2022-10-07 14:15:45 <class 'datetime.datetime'>
print(my_date, type(my_date))  # 2022-10-07 <class 'datetime.date'>
print(my_time, type(my_time))  # 14:15:45 <class 'datetime.time'>


                                        # Методы now(), utcnow(), today()


# Для того, что получить текущее время на момент исполнения программы,
# используются методы now() и utcnow() для локального и UTC времени соответственно.
from datetime import datetime

datetime_now = datetime.now()
datetime_utcnow = datetime.utcnow()

print(datetime_now)           # текущее локальное время (московское) на момент запуска программы
print(datetime_utcnow)        # текущее UTC время на момент запуска программы
# 2021-08-13 08:03:43.224568
# 2021-08-13 05:03:43.224568

# Всемирное координированное время (Coordinated Universal Time, UTC)
# — стандарт, по которому общество регулирует часы и время.
# Московское время соответствует UTC+3.

# Метод today() аналогичен методу now(). Для получения локальной
# даты-времени рекомендуется использовать именно метод now().


                                        # Метод timestamp()


# Метод timestamp() позволяет преобразовать объект типа datetime в
# количество секунд, прошедших с момента начала эпохи.
# Данный метод возвращает значение типа float.

#    Начало эпохи — это полночь 1 января 1970 года (00:00:00 UTC).
from datetime import datetime

my_datetime = datetime(2021, 10, 13, 8, 10, 23)

print(my_datetime.timestamp())  # 1634101823.0


                                        # Метод fromtimestamp()


# Метод fromtimestamp() позволяет преобразовать количество секунд, прошедших
# с момента начала эпохи, в объект типа datetime.
# Данный метод является обратным по отношению к методу timestamp().
from datetime import datetime

my_datetime = datetime.fromtimestamp(1634101823.0)

print(my_datetime)  # 2021-10-13 08:10:23

# Обратите внимание на то, что метод fromtimestamp() по
# умолчанию возвращает объект datetime в вашем часовом поясе.


                                        # Форматирование даты-времени


# По умолчанию объекты типа datetime (как и объекты типа date и time)
# выводятся в специальном формате, который называется ISO 8601.
# Данное представление не всегда удовлетворяет нашим запросам.

# Чтобы преобразовать дату-время в строку нужного формата, следует
# воспользоваться методом strftime(),
# указав ему в качестве аргумента параметры форматирования.
from datetime import datetime

my_datetime = datetime(2021, 8, 10, 18, 20, 34)

print(my_datetime)  # 2021-08-10 18:20:34            # вывод в ISO формате
print(my_datetime.strftime('%d.%m.%y --- %H::%M::%S'))  # 10.08.21 --- 18::20::34
print(my_datetime.strftime('%d/%m/%y'))  # 10/08/21
print(my_datetime.strftime('%A %d, %B %Y'))  # Tuesday 10, August 2021
print(my_datetime.strftime('%H:%M:%S'))  # 18:20:34

# Для форматированного вывода объектов типов date, time, datetime
# используется один и тот же метод strftime().

# Для форматирования даты-времени (datetime) нам с
# вами потребуется уже знакомая таблица.


                                        # Преобразование строки в дату-время


# Как уже было сказано в прошлом уроке, преобразовать данные
# из строки в объект типа datetime можно двумя способами:

# 1) ручным преобразованием
# 2) с помощью метода strptime()

# Ручной подход основан на использовании метода split():
from datetime import datetime

datetime_str = input('Введите дату/время в формате ДД.ММ.ГГГГ ЧЧ:ММ:СС')

date_str, time_str = datetime_str.split(' ')

date_info = [int(i) for i in date_str.split('.')]
time_info = [int(i) for i in time_str.split(':')]

my_datetime = datetime(date_info[2], date_info[1], date_info[0],
                       time_info[0], time_info[1], time_info[2])

print(my_datetime)

# На практике для преобразования строки в объект datetime редко используется
# ручной подход. Вместо него используется метод strptime(),
# который преобразует строку (первый аргумент) в объект
# datetime согласно переданному формату (второй аргумент).

# Приведенный ниже код работает аналогично коду выше:
from datetime import datetime

datetime_str = input('Введите дату/время в формате ДД.ММ.ГГГГ ЧЧ:ММ:СС')

my_datetime = datetime.strptime(datetime_str, '%d.%m.%Y %H:%M:%S')

print(my_datetime)

# Рассмотрим примеры работы данного метода.
from datetime import datetime

datetime0 = datetime.strptime('10.08.2034 13:55:59', '%d.%m.%Y %H:%M:%S')
datetime1 = datetime.strptime('10/08/21', '%d/%m/%y')
datetime2 = datetime.strptime('Tuesday 10, August 2021', '%A %d, %B %Y')
datetime3 = datetime.strptime('18.20.34', '%H.%M.%S')
datetime4 = datetime.strptime('2021/08/10', '%Y/%m/%d')
datetime5 = datetime.strptime('10.08.2021 (Tuesday, August)', '%d.%m.%Y (%A, %B)')
datetime6 = datetime.strptime('Year: 2021, Month: 08, Day: 10, Hour: 18.', 'Year: %Y, Month: %m, Day: %d, Hour: %H.')

print(datetime0, datetime1, datetime2, datetime3, datetime4, datetime5, datetime6, sep='\n')
# 2034-08-10 13:55:59
# 2021-08-10 00:00:00
# 2021-08-10 00:00:00
# 1900-01-01 18:20:34
# 2021-08-10 00:00:00
# 2021-08-10 00:00:00
# 2021-08-10 18:00:00

# Обратите внимание на то, что первый аргумент должен соответствовать формату
# второго аргумента. Если он не соответствует, то возникает исключение ValueError.
from datetime import datetime

my_datetime = datetime.strptime('10/08/2034 13:55:59', '%d.%m.%Y %H:%M:%S')

print(my_datetime)  # ValueError: time data '10/08/2034 13:55:59' does not match format '%d.%m.%Y %H:%M:%S'


                                        # Примечания


# Примечание 1.
# Тип данных datetime наследует весь функционал (атрибуты и методы) от типа date.

# Примечание 2.
# Тип данных datetime является неизменяемым. Мы можем создать множества,
# содержащие объекты данного типа, а также они могут выступать в качестве ключей словаря.

# Примечание 3.
# Мы можем использовать встроенные функции min(), max(),
# sorted() и т.д. при работе с объектами типа datetime.

# Примечание 4.
# Объекты типа datetime можно сравнивать
# (==, !=, <, >, <=, >=), как и большинство других типов данных.

# Примечание 5.
# При создании объекта datetime из строки с помощью метода strptime()
# необязательно, чтобы строка содержала год, месяц и день,
# в отличие от ручного создания объекта datetime.
from datetime import datetime

d = datetime.strptime('9:00', '%H:%M')
print(d)  # 1900-01-01 09:00:00
# Не приведёт к возбуждению исключения.

# Примечание 6.
# Для создания новой даты-времени на основании уже существующей можно
# использовать метод replace(). Он возвращает новый объект
# datetime с переданными измененными значениями атрибутов.
from datetime import datetime

datetime1 = datetime(1992, 10, 6, 10, 12, 45)
datetime2 = datetime1.replace(year=1995, month=12)
datetime3 = datetime1.replace(day=17, hour=14, minute=37)

print(datetime1)  # 1992-10-06 10:12:45
print(datetime2)  # 1995-12-06 10:12:45
print(datetime3)  # 1992-10-17 14:37:45

# Примечание 7.
# Помните про ограничения на year, month, day, hour, minute, second,
# microsecond, которые используете для создания объекта типа datetime.
# В случае использования неверного значения возникнет ошибка (исключение) ValueError.

# Ограничения:
# 1 <= year <= 9999
# 1 <= month <= 12
# 1 <= day <= количество дней в заданом месяце и году
# 0 <= hour < 24
# 0 <= minute < 60
# 0 <= second < 60
# 0 <= microsecond < 1000000

# Примечание 8.
# Для того, чтобы использовать конкретную локализацию (перевод на язык),
# нужно использовать модуль locale.
# риведенный ниже код устанавливает русскую локализацию:
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

my_datetime = datetime(2021, 8, 10, 12, 34, 15)

print(my_datetime.strftime('%A %d, %B %Y, %H:%M:%S'))  # вторник 10, Август 2021, 12:34:15

# Для установки английской локализации используется код:
import locale

locale.setlocale(locale.LC_ALL, 'en_EN.UTF-8')

# Примечание 9. По умолчанию объекты типа datetime выводятся
# в ISO 8601 формате: YYYY-MM-DD HH:MM:SS.ffffff.

# Примечание 10. Для того чтобы получить строковое представление объекта
# datetime в ISO формате, можно воспользоваться методом
# isoformat() или встроенной функцией str().
from datetime import datetime

my_datetime = datetime(1992, 10, 6, 10, 12, 45)

print(my_datetime.isoformat())  # 1992-10-06T10:12:45
print(str(my_datetime))  # 1992-10-06 10:12:45

# Обратите внимание на символ T, который вставляется между датой и временем
# при использовании метода isoformat() для datetime объектов.