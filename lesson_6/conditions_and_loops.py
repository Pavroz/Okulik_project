# Условия

# user_input = input('Enter a number: ')
# if user_input.isnumeric():
#     user_input = int(user_input)
#     if user_input == 1:
#         print('one')
#     elif user_input == 2:
#         print('two')
#     elif user_input == 3:
#         print('three')
#     else:
#         print('many')
# else:
#     print('no number')


# Циклы

names = ['John', 'Tim', 'James', 'Bob', 'Jim', 'Bill']
for name in names:
    print(name)
print()

names = ['John', 'Tim', 'James', 'Bob', 'Jim', 'Bill']
for name in names:
    name = name.replace('o', 'OOO')
    if name.startswith('J'):
        print('Mr. ', end='')
    print(name)
print()

names = {'John', 'Tim', 'James', 'Bob', 'Jim', 'Bill'}
for name in names:
    print(name)
print()

persons = {'Jhon': 132, 'Tom': 167, 'James': 234}
print(persons.keys())
print(persons.values())
for person in persons.values():
    print(person)
print()

persons = {'Jhon': 132, 'Tom': 167, 'James': 234}
for person in persons:
    print(f'{person}: {persons[person]}')
print()

persons = {'Jhon': 132, 'Tom': 167, 'James': 234}
print(persons.items())
for name, height in persons.items():
    print(f'{name}: {height}')
print()

text = 'Sed vitae justo malesuada, commodo libero eu, bibendum mauris.'
words = text.split()
fin_words = []
for word in words:
    if 'o' in word:
        print(word)
    else:
        fin_words.append(word)
print(' '.join(fin_words))