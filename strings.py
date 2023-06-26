'''Экранированная последовательность'''

# \r -> возварщает картетку в начало строки 
# \v -> вертикальная табуляция

'''  Конкатенация '+' и Дублирование строк '*'  '''

# str1='Samat'
# str2='Super'
# print((str2+str1+' ')*5)

''' Динамические строки '''

# 1. Использовать знак  '%'

# name=input('Enter your name: ')
# result='Hello, %s' %name
# print(result)'''Экранированная последовательность'''

# \r -> возварщает картетку в начало строки 
# \v -> вертикальная табуляция

'''  Конкатенация '+' и Дублирование строк '*'  '''

# str1='Samat'
# str2='Super'
# print((str2+str1+' ')*5)

''' Динамические строки '''

# 1. Использовать знак  '%'

# name=input('Enter your name: ')
# result='Hello, %s' %name
# print(result)

# 2. С использованием метода .format()

# name=input('Enter your name: ')
# age=input('enter your age: ')
# result= 'Hello, my name is {} I am {} years old'.format(name,age)
# print(result)

# 3. Интерполяция строк (f-строки)

# name=input('Enter your name: ')
# age=input('enter your age: ')
# result=f'Hello, my name is {name} and i am {age} years old'
# print(result)

# 2. С использованием метода .format()

# name=input('Enter your name: ')
# age=input('enter your age: ')
# result= 'Hello, my name is {} I am {} years old'.format(name,age)
# print(result)

# 3. Интерполяция строк (f-строки)

# name=input('Enter your name: ')
# age=input('enter your age: ')
# result=f'Hello, my name is {name} and i am {age} years old'
# print(result)

# sr='Hello'
# print(sr   [  ::-1 -> выполнит действие с обратным шагом (-1) от конца строки  ]   )

'''========== Методы строк =========='''

# метод - та же функция, но обращаемся к нему через точку .()

# методы на is возвращают True/False

# str.isalnum() - состоит ли строка только из букв и/или чисел

# str.isalpha - состоит ли строка только из букв
 
# str.isdigit() - содержится ли в строке числа 

# str.islower() - находится ли стоока в нижнем регистре 

# str.isupper() - состоит ли строка из символов верхнего регистра 

# str.isspace() - состоит ли строка из неотображаемых символов

# str.isnumeric() - состоит ли строка из только чисел 

'''========================='''

# name='hello'
# print(str.isalpha(name))

'''========================='''

# str.upper() - переводит в верхний регистр

# str.lower() - переводит в нижний регистр 

# str.title() - каждое слово в строке запишет с заглавной буквы 

# str.capitalize() - только самое первое слово в строке запишется с заглавной

# strip() - убирает пробелы в начале иконце строки [rstrio(),lstrip()]

# str.replace(old,new,count) - заменяет старое значени в строке на новый 

# str.split('разделитель') - делит строку по разделителю и при этом возвращает список. разделитель по умолчанию пробел
