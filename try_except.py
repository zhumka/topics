'''========== обработка исключений  ========='''

'''
Ошибки -> проблемы с синтаксисом
1. SyntaxError: забыли двоеточие, скобку
2. IndentationError: неправильный отступ 
3. TabError: неправильная табуляция 
'''

# Исключение: (код написан правильноб но он неправильно работает не так, как ожидалось)
# 1. ArithmeticError ZeroDivisionError
# 2. ValueError
# 3. NameError
# 4. TypeError
# 5. KeyError
# 6. IndexError
# 7. AttributeError
# 8. ImportError 
# 9. BaseException (прородитель)

ZeroDivisionError # при делении на 0
# 8 / 0
# 4 // 0
# 3 % 0

ValueError # Вызывается при распаковки, переводе одного типа данных в другой 
# int('hello')

NameError # когда обращаемся к несуществующей переменной 
# print(b)

TypeError # когда передаем в функциюб метод меньше или больше аргументов, чем требуется 
# for i in 123456789: 
#     print(i)
# [].append()
# [].append(1, 2, 3)
# '5' + 5

KeyError # при обращению к несуществуещему ключу 
# dict_ = {'a' : 1}
# dict_['b']
# dict_.pop('b')

IndexError # при обрашении к несуществующему индексу 
# list_=['a','b','c']
# list_[4]
# list_.pop(3)

AttributeError # когда обрпщпемся к несуществующему методу или аттрибуту объекта
# a=1234
# a.upper()
# b=[1,2,3]
# b.discard()

ImportError #ошибка при импортировании несуществующей бибилиотеки или функции из бибилиотеки
# from math import pi2

'''Конструкция обработки исключений  try except'''
#чтобы код не прекращал свою работу в случае выявлении ошибки 


# try:

    # тело try
    # код, который может вызвать ошибку
# except:

    # тело except 
    #код, который сработает если в try возникае ошибка
# else:

    #код который отработает если в блоке try не возникло ошибки 
# finally:

    #код который отработает в любом случае 

try:
    num=int(input('введите число: '))
    num2=int(input('Введите число: '))
    sum=num/num2
except ValueError:
    print('Вы ввели не число')
except ZeroDivisionError:
    print('На ноль делить нельзя')
else:
    print(f'{num} / {num2} = {sum}')
finally:
    print('ERROR')

# try:
#     while True:
#          print('f')
# except KeyboardInterrupt:
#     print('ctrl + c')


# try:
#     dict_={key: key**2 for key in range(11) if key%a==0}
#     print(dict_)
# except NameError:
#     print('Переменная а не объявлена')

# try:
#         num=int(input('Введите первое число: '))
#         num2=int(input('Введите второе число: '))
#         sum=num+num2
#         res=(f'{num} + {num2} = {sum}')
# except ValueError:
#     print('Вы ввели не число!')

'''============================== raise ================================='''
#искуственно вызывает ошибку 
