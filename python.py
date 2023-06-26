# # a=0
# # while a <=9:
# #     a+=1
# #     print(a)
# # for i in range(10):
# #     a+=1
# #     print(a)

# # a=[1,2,3,4,5,'hello',9,False]
# # sum=0
# # for i in a:
# #     if type(i) not in (int,float):
# #         continue
# #     sum+=i

# # number=input('Введите число: ')
# # x = [int(a) for a in str(number)]
# # print(x)
# # max1=x[0]
# # for i in x:
# #     if i>max1:
# #         max1=i
# # print(f'Наибольщая цифра: {max1}')

# # dict_={'murat':24,'erzhan':21,'karina':24,'altynai':17,'aibek':16}
# # for k,v in dict_.items():
# #     if v>=18:  
# #         print(k,'Вход разрешен')
# #     else:
# #         print(k,'Вход запрещен')

# '''==============================================================================================================================================='''

# # def calculator(num1,num2,act):
# #         if act=='+':
# #             print(f'{num1} + {num2} =',num1+num2)
# #         elif act=='-':
# #             print(f'{num1} - {num2} =',num1-num2)
# #         elif act=='*':
# #             print(f'{num1} * {num2} =',num1*num2)
# #         elif act=='/':
# #             print(f'{num1} / {num2} =',num1/num2)


# # while True:
# #     try:
# #         num1=int(input('введите первое число:'))
# #         num2=int(input('введите второе число:'))
# #         act=input('Выберите действие + , - , * , / : ')
# #         calculator(num1,num2,act)
# #         if num1==0 and num2==0:
# #               break
# #     except ValueError:
# #         print('Вы ввели не число!')
# #         num1=int(input('введите первое число:'))
# #         num2=int(input('введите второе число:'))
# #         act=input('Выберите действие + , - , * , / : ')
# #         calculator(num1,num2,act)
# #         if num1==0 and num2==0:
# #               break
# #     except ZeroDivisionError:
# #         print('На ноль делить нельзя!')
# #         num1=int(input('введите первое число:'))
# #         num2=int(input('введите второе число:'))
# #         act=input('Выберите действие + , - , * , / : ')
# #         calculator(num1,num2,act)
# #         if num1==0 and num2==0:
# #               break
# #     finally:
# #          continue


# '''==============================================================================================================================================='''


# # lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# # max_list=[]
# # min_list=[]
# # max=lists[0]
# # for i in lists:
# #     print(len(i))

# def calculator(num1,num2,act):
#         if act=='+':
#             print(f'{num1} + {num2} =',num1+num2)
#         elif act=='-':
#             print(f'{num1} - {num2} =',num1-num2)
#         elif act=='*':
#             print(f'{num1} * {num2} =',num1*num2)
#         elif act=='/':
#             print(f'{num1} / {num2} =',num1/num2)
#         else:
#              print('Такой операции нет!')


# while True:
#     try:
#         num1=int(input('введите первое число:'))
#         act=input('Выберите действие + , - , * , / : ')
#         num2=int(input('введите второе число:'))
#         calculator(num1,num2,act)
#         if num1==0 and num2==0:
#               break
#     except ValueError:
#         print('Вы ввели не число!')
#         num1=int(input('введите первое число:'))
#         act=input('Выберите действие + , - , * , / : ')
#         num2=int(input('введите второе число:'))
#         calculator(num1,num2,act)
#         if num1==0 and num2==0:
#               break
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')
#         num1=int(input('введите первое число:'))
#         act=input('Выберите действие + , - , * , / : ')
#         num2=int(input('введите второе число:'))
#         calculator(num1,num2,act)
#         if num1==0 and num2==0:
#              break
    
# category,pod_category,title,description,level,price

#    category=input('Выберите категорию -> Веб-разработка, Разработка мобильных приложений, Разработка игр: ')
#     pod_category=input('ВЫберите подкатегорию -> Python, JavaScript, Java: ')
#     title=input('Напишите заголовок курса (не более 60 символов):')
#     description=input('Напишите описание к курсу не минимум 10 слов:')
#     level=input('Выберите уровень -> начальный, средний, профессиональный')
#     price=input('Сумма курса в сомах:')

# db={'id':1,
#             'Категория':'sfdsfds',
#             'Подкатегория':'pod_category',
#             'Заголовок курса':'title',
#             'Описание курса':'description',
#             'Уровень':'level',
#             'Цена в сомах':'price'}

# def read_me(id):
#      for i in db:
#           if i['id']==1(id):
#                print(db[i])
# num=int(input('enter num: '))
# read_me(num)

# from functools import reduce
# list_ = [5, 6, 7, 8] 
# result=reduce(lambda x, y:x*y,list_)
# print(result)
# list_=[1,2,3,4,5,6,7,8]
# result=reduce()
# print(result)
# result=list(map(lambda x:'Fizz' if x%3==0 else 'Buzz',range(1,50)))
# print(result)
from functools import reduce
list_ = ['a', 'n', 'n', 'a']
result=list(map(lambda x: 'YES' if list_[::-1]== list_ else 'NO',list_))
print(result)