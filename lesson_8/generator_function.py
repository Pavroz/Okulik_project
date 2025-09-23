# Генераторы функции
from idlelib.colorizer import prog_group_name_to_tag

# my_list = [1, 2, 5, 7, 4, 9]
#
# for x in my_list:
#     print(x)
# print()
#
#
# n = 2
# progression = []
# num = 1
#
# while len(progression) < 100:
#     progression.append(num)
#     num += n
# print(progression)
# print()


def progression(limit=100):
    n = 2
    num = 1
    count = 1
    while count < limit:
        yield num
        num += n
        count += 1
# print(list(progression(10)))
# print()
#
# for number in progression(10):
#     print(number)

count = 1
for number in progression(1000001):
    if count == 1000000:
        print(number)
        break
    count += 1