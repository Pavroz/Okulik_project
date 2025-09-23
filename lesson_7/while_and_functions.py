# Цикл While

# i = 0
# while i < 5:
#     print('Hello')
#     i += 1
# print('The end')


# while True:
#     user_input = input('Enter something: ')
#     if user_input == 'exit':
#         break
#     elif user_input == 'skip':
#         print('Skipped')
#         continue
#     elif len(user_input) > 10:
#         print('Your input is too long')
#     else:
#         print('Input is okay')
# print('Goodbye')

# text = 'Sed vitae justo malesuada, commodo libero end eu, bibendum mauris.'
# words = text.split()
# fin_words = []
# for word in words:
#     if word == 'end':
#         break
#     elif 'o' in word:
#         print(word)
#         continue
#     fin_words.append(word)
# print(' '.join(fin_words))

# numbers = [1, 5, 4, 7, 5]
# main_number = 47
# for number in numbers:
#     print(number + main_number)


a = 1
b = 5
c = 4
d = 7
y = 1
main_number = 47
def calc(num):
    if y == 0:
        return num
    else:
        result = num + main_number
        return result

# print(calc(a))
calc(b)
calc(c)
calc(d)


# def hello():
#     a = 12
#     return a
# print(hello())

def print_words(first, second, third, fourth, fifth):
    print(f'The first word is {first}, second word is {second}, {third}, {fourth}, {fifth}')

print_words(5, 3, 1, 4, 2) # Позиционный аргументы
print_words(fifth=5, third=3, first=1, fourth=4, second=2) # Именованные аргументы

def power(number, degree=2):
    return number ** degree

print(power(2))
print(power(2, 3))
print()

def example(e, f, g, ff='one', gg='two'):
    print(e, f, g, ff, gg)

example(2, 3, 4, gg = 5)
example(2, 3, 4)
print()

def sum_all(*args):
    # print(args)
    # result = 0
    # for x in args:
    #     result += x
    # return result
    # Код выше - аналог встроенной функции sum(args)
    return sum(args)

print(sum_all(1, 2, 3))
print()


def price_list(title, price):
    print(f'Product {title} price is {price}')

price_list('iphone', 2500)
price_list('android', 1500)
print()

def price_list(**kwargs):
    # print(kwargs)
    for title, price in kwargs.items():
        print(f'Product {title} price is {price}')

price_list(iphone=2500, android=1500, laptop=1000)