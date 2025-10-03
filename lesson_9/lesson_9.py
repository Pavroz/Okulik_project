# summer = True
#
# if summer is True:
#     print('The weather is fine')
# else:
#     print('The weather is not fine')
#
#
# summer = True
#
# if summer:
#     print('The weather is fine')
# else:
#     print('The weather is not fine')
#
#
# a = 'sdsada'
#
# if a:
#     print('...')
#
#
# numbers = [1, 45, 23, 67, 32, 89]
# print(max(numbers)) # Выводит максимальное число
# # max_num = 0
# # for x in numbers:
# #     if x > max_num:
# #         max_num = x
# # print(max_num)
# print(min(numbers))
# print(sum(numbers))
#
# a = 1 / 3
# print(round(a, 3)) # Округление числа до 3 символов после запятой
#
# print(abs(1)) # Модуль числа
#
# print(sorted(numbers)) # Сортировка
# print(sorted(numbers, reverse=True)) # Сортировка в обратном порядке
# print()
#
# numbers.sort() # Изменение сортировки с сохранением
# print(numbers)
# numbers.sort(reverse=True) # Изменение сортировки с сохранением
# print(numbers)
# print()
# print()

# Map - применение операции к каждому элементу

# my_list = [1, 2, 3, 4, 5]
#
# new_list = []
# for x in my_list:
#     new_list.append(x * 2)
# print(new_list)


my_list = [1, 2, 3, 4, 5]

def mult_by_2(x):
    return x * 2

new_list = map(mult_by_2, my_list) # для каждого элемента my_list применяем функцию mult_by_2
print(list(new_list))
# В вызове функции ничего не передается, т.к. питон сам понимает, что нужно подставлять каждое число из my_list

# Лямбда функции нужны для обозначения простых функций, чтобы не писать их в несколько строк
# Аналог функции выше в виде лямбды
my_list = [1, 2, 3, 4, 5]
new_list = map(lambda x: x * 2, my_list)
print(list(new_list))
print()

my_list = [1, 2, 3, 4, 5]

def mult_by_2(x):
    if x > 10:
        return x * 5
    else:
        return x * 2

# Тернарные операторы или тернарные выражения
new_list = map(lambda x: x * 5 if x > 10 else x * 2, my_list)
print(list(new_list))


my_list = [1, 2, 3, 4, 5]
# Тернарный оператор
b = 1 if len(my_list) > 4 else 5
print(b)
print()

# name, surname = input('Your name and surname: '). split()
# print(f'name is {name} and surname is {surname}')

# code, number = map(int, input('code and number'). split())
# print(f'name is {code} and surname is {number}')


# Filter

my_list2 = [1, 2, 3, 4, 5, 6, 7, 8]
new_list2 = []
for x in my_list2:
    if x % 2 == 0:
        new_list2.append(x)
    else:
        print(f'oops, this is: {x}')
print(f'Первый вариант: {new_list2}')

# Снизу пример кода через Filter

my_list2 = [1, 2, 3, 4, 5, 6, 7, 8]
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
# Для каждого элемента списка применяется функция и если True, то он пойдет в список new_list2, а если False, то нет
new_list2 = filter(is_even, my_list2)
print(f'Второй вариант: {list(new_list2)}')

# Снизу улучшенный вариант кода сверху

my_list2 = [1, 2, 3, 4, 5, 6, 7, 8]
def is_even(x):
    return x % 2 == 0
new_list2 = filter(is_even, my_list2)
print(f'Третий вариант: {list(new_list2)}')

# Еще более улучшенный вариант кода сверху

my_list2 = [1, 2, 3, 4, 5, 6, 7, 8]
new_list2 = filter(lambda x: x % 2 == 0, my_list2)
print(f'Четвертый вариант: {list(new_list2)}')



# Datetime

import datetime

# Вывод даты и времени
time_now = datetime.datetime.now()
print(time_now) # Время и дата
print(time_now.hour) # Сколько часов
print(time_now.year) # Какой год
print(time_now.isoweekday()) # День недели
print(time_now.timestamp()) # Сколько секунд прошло с создания линукса

easy_date = datetime.datetime(1970, 1, 7)
print(easy_date)
print(easy_date.timestamp())
print()

my_time = '2023/06/05 12 hours, 30 mins, 10 secs'
python_date = datetime.datetime.strptime(my_time, '%Y/%m/%d %H hours, %M mins, %S secs')
print(python_date)
print(python_date.month)

human_date = python_date.strftime('Year: %y, month: %B, day: %d')
print(human_date)




new_list = map(lambda x: x * 2, my_list)
print(list(new_list))