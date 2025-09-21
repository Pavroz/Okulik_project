# Распаковка
my_list = [1, 2]
my_tuple = (5, 6, 8)

# Вместо этого:
# a = my_list[0]
# b = my_list[1]
# c = my_tuple[0]
# d = my_tuple[1]
# e = my_tuple[2]
# Это:
a, b = my_list
c, d, e = my_tuple
print(a, b, c, d, e)


# Срез

lll = [1, 5, 8, 2, 1, 5, 3]
print(lll[1:5]) # Выводит "от" включительно, а "до" не включительно
print(lll[:4]) # Выводит с самого начала и до 4 элемента
print(lll[3:]) # Выводит с 3 элемента до конца
print(lll[1::2]) # Шаг среза, начиная с 1 индекса и до конца, с шагом 2
print(lll[::]) # Аналогично print(lll)
print(lll[::-1]) # Вывод всего списка начиная с конца
print()

# Методы строк

text = 'my long long string'
print(text[3])
print(len(text))
print(text.index('l'))
print('long' in text)
print(text.count('long'))
print(text[:7])
print(text.startswith('my'))
print(text.endswith('string'))

txt = 'ThIs tExT wiTh meSsEd uP CaPITalIZatiOn'
print(txt.capitalize()) # Делает первую букву заглавной, а остальные строчными
print(txt.title()) # Делает каждую первую букву заглавной
print(txt.upper()) # Делает все буквы заглавными
print(txt.lower()) # Делает все буквы строчными

text = 'mY lOng loNg STriNG'
string_index = text.lower().index('string')
print(text[:string_index].lower() + text[string_index:].upper())

msg = 'Hello World!'
msg = msg.replace('World', 'universe')
print(msg)

data = '12,3'
data = data.replace(',', '.')
print(data)

txt = ' admin '
# txt = txt.replace(' ', '')
txt = txt.strip() # Убирает все пробела
txt = txt.rstrip() # Убирает пробел справа
txt = txt.lstrip() # Убирает пробел слева
print(txt)
text = '"name"'
text = text.strip('"')
print(text)
print()

# Строка <--> Список
my_string = 'some little text'
my_string1 = 'some, little, text'
list_from_text = my_string.split()
list_from_text1 = my_string1.split(', ')
print(list_from_text)
print(list_from_text1)

languages = ['Python', 'Java', 'Ruby']
print(languages)
# languages = ', '.join(languages)
# print(languages)
print('Студент знает следующие языки: ', ', '.join(languages))


# Форматирование строк
a = 'one'
b = 'two'
print('First word is', a, ', second word is', b)
print('First word is ' + a + ', second word is ' + b)
my_text = 'First word is %s, second word is %s'
print(my_text % (a, b))
# string format
my_text = 'First word is {0}, second word is {1}' # Рекомендуется проставлять индексы, чтобы можно было их менять
print(my_text.format(a, b))
# f string
my_text = f'First word is {a}, second word is {b}'
print(my_text)