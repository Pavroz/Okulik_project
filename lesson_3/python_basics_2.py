# List - Списки

my_list = [1, 3, 6, 7, None, 'text', False, 2.42, 'adsdas', 'last']
print(my_list)
print(len(my_list))
print(my_list[2])
print(my_list[-1])
print()

my_list = []
print(my_list)
my_list.append(42)
my_list.append('text')
print(my_list)
print(len(my_list))
print(my_list.index(42))
poped = my_list.pop(0)
print(my_list)
print(poped)
print('text' in my_list)


# Tuple - Кортежи

my_tuple = (1, 3, 6, 7, 1, None, 'text', False, 2.42)
print(my_tuple[1])
print(len(my_tuple))
print(my_tuple.count(1))
print(my_tuple.index(6))
print()



# Set - Множества
my_set = {1, 3, 6, 7, None, 'text', False, 2.42}
my_set.add(42)
print(my_set)
print(my_set)

list1 = [1, 2 , 5, 6, 2, 1, 8]
list1 = set(list1)
list1 = list(list1)
print(list1)
list1 = list(set([1, 2 , 5, 6, 2, 1, 8]))
print(list1)
print()

# Dict - Словарь

my_dict = {'one': 'value', 'two': 'value2'}
print(my_dict['two'])
print(len(my_dict))
my_dict['one'] = 'value1'
print(my_dict)
my_dict['three'] = 'value3'
print(my_dict)
my_dict['four'] = False
my_dict['five'] = [1, 5, 8]
my_dict['six'] = {1, 6, 9}
my_dict[2] = 'ffwefwe'
my_dict[False] = 'qqq'
my_dict[1.42] = 'www'
my_dict[(1, 2, 5)] = 'ooo'
my_dict[5] = {1: 2}
print(my_dict)