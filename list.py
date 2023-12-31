'''Тип данных списки'''
# изменемый,упорядоченный,индексируемый тип данных.
# [] -> литералы,выражения и константы которые создают объект

# listj = [1,2,3,4,5,[True,'hello'], 'zhuma',{1:'one'},(1,2,3,4)]
# print(listj[5][1])
# print(listj[-1])

# listj[0]='hello' ->добавление элемента

'''==========  Создание списков =========='''

# 1.    list(iterablke)

#       range() -> возвращает последовательность        
#       start -> с какого числа начать (по умолчанию с 0)
#       end -> до какого элемента (не включительно end)
#       step -> шаг (какие элементы пропустить)

'''==================== Методы списка ===================='''
# append(item): добавляет элемент item в конец списка
listj = [1,2,3,4,5,[True,'hello'], 'zhuma',{1:'one'},(1,2,3,4)]
#       listj.append('hello')
#       print(listj)
# list.extend([interable]) -> расширяет список.
# insert(index, item): добавляет элемент item в список по индексу index.
# remove(item): удаляет элемент item. Удаляется только первое вхождение элемента. Если элемент не найден, генерирует исключение ValueError.
# clear(): удаление всех элементов из списка.
# index(item): возвращает индекс элемента item. Если элемент не найден, генерирует исключение ValueError * pop([index]): удаляет и возвращает элемент по индексу index. Если индекс не передан, то просто удаляет последний элемент.
# count(item): возвращает количество вхождений элемента item в список.
# print(listj.count(1))
# sort([key]): сортирует элементы. По умолчанию сортирует по возрастанию. Но с помощью параметра key мы можем передать функцию сортировки.
# reverse(): расставляет все элементы в списке в обратном порядке.
# pop(): удаляет элементы по индексу при этом после удаления он возвращает удаленный элемент, по умолчаниб удаляет последний элемент.
'''Кроме того, Python предоставляет ряд встроенных функций для работы со списками:'''

# len(list): возвращает длину списка
# sorted(list, [key]): возвращает отсортированный список
# min(list): возвращает наименьший элемент списка
# max(list): возвращает наибольший элемент списка

'''========== Цикл for =========='''

# работает как в С++ но без параметра шага проходится по всему объекту последовательно

'''tuple - кортеж'''

#неизменяемый индексируемый итерируемый тип данных
# литералами кортежа явл -> (,)