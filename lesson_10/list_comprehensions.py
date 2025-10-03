



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = []
for x in my_list:
    new_list.append(x * 2)
print(new_list)


new_list = [x * 2 for x in my_list]
print(new_list)
print()

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = []
for x in my_list:
    if x % 2 == 0:
        new_list.append(x)

new_list = map(lambda x: x * 2, my_list)
new_list1 = filter(lambda x: x % 2 == 0, my_list)
new_list2 = [x for x in my_list if x % 2 == 0]
new_list3 = [x if x % 2 == 0 else x + 1 for x in my_list]
# new_list4 = [x if x % 2 == 0 else print(f'{x} is not even') for x in my_list]
print(list(new_list))
print(list(new_list1))
print(new_list2)
print(new_list3)
# print(new_list4)
print()




my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_dict = {}
for x in my_list:
    new_dict[x] = x * 3 # [x] - ключ, x * 3 - значение
print(new_dict)

new_dict = {x: x * 3 for x in my_list}
print(new_dict)


data = [('one', 'two'), ('three', 'four')]

new_dict = {}
for key, value in data:
    new_dict[key] = value
print(new_dict)
print()

new_dict = {key: value for key, value in data}
print(new_dict)

new_dict = dict(data)
print(new_dict)
print()


countries = ['USA', 'Hawaii', 'Cuba']
temps = [23, 33, 35]

country_temps_dict = dict(zip(countries, temps)) # формирование с помощью zip кортежей, а с помощью dict словарей
print(country_temps_dict)
