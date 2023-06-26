'''Области видимости и простанства имен'''

# def func():
#     a=0
#     print('Функция питон')
# print(a)

'''Пространства имен'''

# 1. builtins -> все что встроенно в стандартную библиотеку питона


# print
# lens
# sum
# min
# max


# 2. Global -> все переменные внутри файла которые мы создали 

# 3. Enlosed -> (не локальное, замкнутое) находится между двумя пространствами
#    возникает только тогда когда внутри функций объявляется вложенная фукнция  





# def counter():
#     num = 0 -> Enclosed переменная

#     def incrementer():
#         num =num + 1
#         return num

#     return incrementer 


# def outer_func():
#     outer = 88
#     print(outer)
#     def inner_func():
#         inner = 99
#         print(inner)
    
# outer_func()



# 4. Local -> (локальные)


'''Порядок поиска переменной'''

# Local -> Enclosed -> Global -> Builtins 

# global -> ссылки и указатели в питоне 

# x=10
# def func():
#     global x
#     x=20
#     print(x)

# func()
# print(x)

# nonlocal -> изменить переменную Enclosed

