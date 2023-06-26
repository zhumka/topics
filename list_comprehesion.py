#генерация какой то последовательности в одну строку используя цикл for (синтаксический сахар)

# for переменная  in диапазон:
#     тело

"""синтаксис"""

# результат for  элемент in интерируемый объект

# результат for  элемент in интерируемый объект if фильтрация

# list:

# упрощает процесс создания списков

# list_=[] 
# for i in 'hello':
#     list_.append(i)
# print(list_)

# list1=[i for i in 'hello']
# print(list1)

# list1=[i for i in range(1,11) if i%2==0]
# print(list1)

# [элемент if условие else элемент 2 for i in итерируемый объект]

# print(['четное' if i%2==0 else 'нечетное' for i in range(1,11)])

#set: 

# list0=[1,2,23,4,2,5,23,]
# set1={i for i in list0}
# print(set1)

#dict:

# dict0={1:'a',2:'b',3:'c'}
# dict1={v: k for k,v in dict0.items()}
# print(dict0)
# print(dict1)
# print(dict1['a'])

# dict_={i:i**2 for i in range(1,11)}
# print(dict_)

# list_=[1,2,3,4,5,6,7,8,9,0]

# list1=[1,2,3,4,5,6,7,8,9,0]
# list2=[0,9,8,7,6,5,4,3,2,1]
# dict1={list1[i] : list2[i] for i in range (len(list1))}
# print(dict1)

'''========= вложенные comprehension========='''

# dct={i:[j for j in range(i+1)] for i in range(1,6)}
# print(dct)

# list1=[['hello world' for i in range(5)] for i in range(3)]
# print(list1)

employees = {
    'id1': {
        'first name': 'Александр',
        'last name' : 'Иванов',
        'age': 30,
        'job':'программист'
            },
    'id2': {
        'first name': 'Ольга',
        'last name' : 'Петрова',
        'age': 35,
        'job':'ML-engineer'
            }
}

dct={key:{k:float(v) 
          if k=='age' 
          else v for k,v in 
          value.items()} 
          for key,value in 
          employees.items()}
print(dct)