# import random
# name=input('введите имя: ')
# sname=input('Введите фамилию: ')
# def get_info(str1:str,str2:str):
#   password=''
#   nums=['0','1','2','3','4','5','6','7','8','9']
#   strings=[]
#   for i in str1:
#     strings.append(i)
#   for i in str2:
#     strings.append(i)
#   print(strings)
#   for i in range(8):
#     if len(password)<7:
#         word=random.choice(nums)
#         password+=word
#     else:
#         word=random.choice(strings)
#         password+=word
#   print(f'Ваш пароль: {password}')
# get_info(name,sname)

'''============================================================================================================================================='''

# def calculator1(num1,num2,act):
#     print(f'{num1} + {num2} =',num1+num2)

# def calculator2(num1,num2,act):
#     print(f'{num1} - {num2} =',num1-num2)

# def calculator3(num1,num2,act):
#     print(f'{num1} * {num2} =',num1*num2)

# def calculator4(num1,num2,act):
#     try:
#          print(f'{num1} / {num2} =',num1/num2)
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')

# num1=int(input('введите первое число:'))
# act=input("Выберите действие '+' - сложение  '-' - вычитание '*' - умножение '/' - деление : ")
# num2=int(input('введите второе число:'))
# if act=='+':
#     calculator1(num1,num2,act)
# elif act=='-':
#     calculator2(num1,num2,act)
# elif act=='*':
#     calculator3(num1,num2,act)
# elif act=='/':
#     calculator4(num1,num2,act)

'''=============================================================================================================================================='''

# def ice_cream(ice,size,topping=None):
#     ice_cream1=f'Вы выбрали морожоное со вкусом {ice} и размером {size}'
#     if topping:
#         ice_cream1+=f'  Вы выбрали топпинг {topping}'
#         return ice_cream1
#     else:
#         return ice_cream1
# ice=input('Напечатайте с каким вкусом мороженое вы хотите: ')
# size=input('Напишите какого размера хотите мороженое: ')
# add=input('Желаете ли топпинг к мороженому да/нет?: ')
# if add=='да':
#     top=input('Какой топпинг хотите?: ')
#     print(ice_cream(ice,size,top))
# else:
#     print(ice_cream(ice,size))
a = {'a': 1, 'b': 2, 'c': 3}
b={}
for k,v in a.items():
    b[v]=k
print(b)


# list_=[i for i in range(1,25) if i%2==0]
# print(list_)