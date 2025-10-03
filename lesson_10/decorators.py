


def greet():
    def hello():
        return 'Hello, world!'
    return hello()
print(greet())


def outer():
    def inner():
        return 2 + 5
    return inner
print(outer()())


def func1(give_me_a_func):
    print('before')
    give_me_a_func()
    print('after')

def simple1():
    print('simple1')

def simple2():
    print('simple2')

func1(simple1)
func1(simple2)
print()

def add_text(func):
    def wrapper():
        print('before')
        func()
        print('after')
    return wrapper

@add_text # Обозначение функции декоратора add_text(simple1)()
def simple1():
    print('simple1')

@add_text # Обозначение функции декоратора
def simple2():
    print('simple2')

simple1()
simple2()
print()


def add_logs(func):
    def wrapper():
        print(f'function {func.__name__} started') # Вызывается название функции, которая помещается в add_logs
        func()
    return wrapper

@add_logs
def simple1():
    print('simple1')

@add_logs
def simple2():
    print('simple2')

@add_logs
def print_nothing():
    return 'hello'

simple1()
simple2()
print_nothing()
print()



def add_logs(func):
    def wrapper(*args):
        print(f'function {func.__name__} started') # Вызывается название функции, которая помещается в add_logs
        result = func(*args)
        print(f'function {func.__name__} finished')
        return result
    return wrapper

@add_logs
def calc1(x):
    print(x * 2)

@add_logs
def calc2(x, y):
    print(x * y)

calc1(3)
calc2(3, 7)




# List comprehension


