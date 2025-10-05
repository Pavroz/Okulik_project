


def calc(x, y):
    try:
        return int(x) / int(y)
    except (ZeroDivisionError, ValueError) as err:
        # print(x, y)
        # raise err
        print(err)
        print('Ошибка ввода данных!')
    # except ZeroDivisionError as zde:
    #     print('На ноль делить нельзя!')
    # except ValueError as ve:
    #     print('Нужно ввести числа')

print(calc(input('Number one: '), input('Number two: ')))
print('Hello!')