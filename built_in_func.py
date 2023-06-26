'''Общеизвестные'''
# print dirmod input и т.д.

'''
lambda -> анонимная функция (та же самая функция только без имени)
'''

# lambda параметры: что функция возвращает

# def add_nums(x, y): 
#     return x+y          #-> обычная функция

# lambda x,y:x+y          #-> lambda функция 

# sum_=lambda x,y:x+y 

# print(sum_(2,4))

# a =lambda a,b,c,:a,b,c

# print(a(1,2,3))

# dict_={1:'a',2:'b',3:'c'}

# dict_keys=lambda x:x.keys()
# print(dict_keys(dict_))

# ls=[1,2,3,4,5,6,7,8]

# ls_=lambda x: x[-1]

# print(ls_(ls))

# num=lambda x:len(x)
# print(num('dfg'))

# func=lambda x:x
# print(func())

'''
map(func,iterable) -> она применяет функцию для каждого элемента итерируемого объекта list_=['1','2','3','4']
# print(map(int,list_))
# for i in map(int,list_):
#     print(i)
# ls1=[map(int,list_)]
# print(ls1)

'''

# list_=['1','2','3','4']
# print(map(int,list_))
# for i in map(int,list_):
#     print(i)
# ls1=[map(int,list_)]
# print(ls1)

# nums=input('Введите 2 числа через пробел: ')
# c=nums.split()
# ls=list(map(int,c))
# a,b=ls
# print('a =',a)
# print('b =',b)
# print(ls)

'''
filter(func,iterable) -> фильтрует элементы итреируемого объекта основвываясб на результат func
'''

# def filter_nums(number:int) -> bool:
#     if number %2==0:
#         return True
#     else:
#         return False
    
# list_=[i for i in range(1,11)]

# result=list(filter(filter_nums,list_))
# print(result)

# list_=['Тима','Макс','Эртай','Эркайим','Алина','Алекс']

# def start(name):
#     vowels='АЕОУИЭЮЯ'
#     return name.upper().startswith(tuple(vowels))

# result=list(filter(start,list_))
# print(result)

'''
reduce(func,iterable) -> нужно импортировать с functools. возвращает один результат 
заменили -> sum, min, max
'''

'''
сумма всех элементов списка 
'''

# from functools import reduce
# list_=[1,2,3,4,5,6,7]
# result=reduce(lambda x,y:x+y, list_)                #-> reduce раньше так делали, но для заметки прошли эту функцию
# print(result)

# print(sum(list_))                                   #-> sum заменил reduce

'''
enumerate(iterable, [start]) -> нумерует элементы последовательности по дефолту начинает с 0
'''

# list_=['hello','test','john','world','py30','питхаб']
# print(list(enumerate(list_,5)))


'''
zip(iterable) -> принимает в аргументы итерируемые объекты
(последовательности, например списки, строки и.т.п) 
и объединяет в кортежи элементы из последовательностей 
переданных в качестве аргументов.
'''

# taxi = [1, 2, 3 ] 
# friends = ['jane', 'joe', 'john', 'joyce'] 
# trip=dict(zip(taxi,friends))
# print(trip)

# dict_={1:2,3:4,5:6}

# result=list(map(str,dict_.values()))
# new_dict=dict(zip) недописал 

# def chet(x):
#     if x%2==0:
#         return 'Четное'
#     else:
#         return 'Нечетное'
    
# list_=[1,2,3,4]
# list2=list(map(chet,list_))
# print(list2)

