'''Декораторы'''

'''функция высшего порядка -> это функция которая может 
принимать в качестве аргумента другую функцию или возвращать 
функцию как результат'''

# def outer(x):
#     def inner(y):
#         return x+y
#     return inner

# outer_func=outer(9)

# def test_func(func):
#     def inner_func():
#         func
#         #<тело>
#     return inner_func

# def hello(func):
#     #<тело>
#     pass


'''
Декораторы -> функция высшего порядка 
(в качестве аргумента принимает функцию и возвращает функцию) 
которая оборачивает другую функцию для расширения ее функционала при этом не изменяя её код
'''

# как работает @ под капотом

# @ -> синтаксический сахар позволяет нам явно указать какой декоратор применяется для функции

# под капотом вызывает функцию декоратор и рузельтат этой функции сохраняет в переменной с точной таким же названием как и обернутая функция 


# def uppercase_decorator(func):
#     def wrapper():
#         func_=func()
#         upper_str=func_.upper()
#         return upper_str
#     return wrapper

# @uppercase_decorator
# def inp_str():
#     str_=input('Введите текст: ')
#     return str_

# print(inp_str())


# def repeat(num):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(num):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator

# @repeat(num=3)
# def greet(name):
#     print(f"Hello, {name}!")

# greet("Juma")

import time

def countdown(seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Обратный отсчёт начат: осталось {seconds} секунд...")
            time.sleep(seconds)
            print("Обратный отсчёт завершён. Выполняется декорированная функция...")
            func(*args, **kwargs)
        return wrapper
    return decorator

@countdown(seconds=5)
def greet(name):
    print(f"Hello, {name}!")

greet("Juma")
