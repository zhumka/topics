# сопособы создания словаря 

# 1. dict_={'a': 'hello'}

# 2. dict_1=dict(a='hello',b=1)

# 3. dict_=dict((['key', 'value' ]))

# ключи должны быть неизменяемым типом данных
#ключи в словаре должныы быть уникальными 
# значения могут быть любого типа данных 

dict_={
    'name':'Aiana',
    'last_name': None,
    'email':True,
    'info':[1,2,3,4]
}
# print(dict_['info'])
# print(dict_)

# dict_['email']='soslippyyy@gmail.com' -> изменяет значения по ключу
# print(dict_)
# dict_['email1']=12 -> добавляет новую пару в словарь 
# print(dict_)

'''=================== Методы словаря =================='''

# dict.values() -> для получения значений в словаре

# for i in dict_.values():
#     print(i)

# example_dictionary.clear() - очищает словарь example_dictionary.

# example_dictionary.copy() - возвращает копию словаря example_dictionary.

# dict_copy=dict_.copy()
# print(dict_copy)

# dict.fromkeys(seq, [value]) - создает словарь с ключами из seq (seq -- это последовательность в виде кортежа, списка, строчного значения, или множества) и значением value (по умолчанию None).

# list_=['name','hello','hi']
# dict_=dict.fromkeys(list_,1)
# print(dict_)

# example_dictionary.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).

# print(dict_.get('name'))

# example_dictionary.items() - возвращает пары (ключ, значение).

# example_dictionary.keys() - возвращает ключи в словаре.

# example_dictionary.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).

# dict.popitem() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.

# dict.setdefault(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ с значением default (по умолчанию None).

# dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).

# dict.values() - возвращает значения в словаре.

# Метод clear() - удаляет все элементы словаря, но не удаляет сам словарь. В итоге остается пустой словарь.
