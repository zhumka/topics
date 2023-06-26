db=[]
count=0
def user_create(category,pod_category,title,description,level,price):
    global count
    count+=1
    create={'id':count,
            'Категория':category,
            'Подкатегория':pod_category,
            'Заголовок курса':title,
            'Описание курса':description,
            'Уровень':level,
            'Цена в сомах':price}
    db.append(create)
    return 'Регистрация прошла успешно!'
def main():
    print('Welcome')
    while True:
            action=int(input('1 - регистрация, 2- найти курсы по id, 3- показать все курсы в списке, 4- изменить данные по id, 5-удалить курс по id 6 - выход: '))
            if action==6:
                break
            elif action==1:
                add1=int(input('Выберите категорию -> 1. Веб-разработка  2. Разработка мобильных приложений 3. Разработка игр (по умолчанию Разработка игр): '))
                if add1==1:
                    category1='Веб-разработка'
                elif add1==2:
                    category1='Разработка мобильных приложений'
                else:
                    category1='Разработка игр'
                add2=int(input('ВЫберите подкатегорию -> 1. Python, 2. JavaScript, 3. Java (по умолчанию Java): '))
                if add2==1:
                    pod_category1='Python' 
                elif add2==2:
                    pod_category1='JavaScript'
                else:
                    pod_category1='Java'
                title1=input('Напишите заголовок курса (не более 60 символов): ')
                if len(title1)>60:
                    print('Введите не более 60 символов')
                    title1=input('Напишите заголовок курса (не более 60 символов): ')
                description1=input('Напишите описание к курсу не менее 10 слов: ')
                add3=int(input('Выберите уровень -> 1. начальный, 2. средний, 3. профессиональный: (по умолчанию начальный)'))
                if add3==2:
                    level1='средний'
                elif add3==3:
                    level1='профессиональный'
                else:
                    level1='начальный'
                price1=input('Сумма курса в сомах: ')
                user_create(category1,pod_category1,title1,description1,level1,price1)
            elif action==2:
                user_id=int(input('Введите id курса: '))

                print(get_user(db,user_id))
            elif action==3:
                print(db)
            elif action==4:
                user_id=int(input('Введите id курса: '))
                choose=int(input('Что хотите ихменить? -> 1. Категория 2. Подкатегория 3. Заголовок курса 4. Описание курса 5.Уровень 6. Цена в сомах : '))
                if choose==1:
                    k='Категория'
                elif choose==2:
                    k='Подкатегория'
                elif choose==3:
                    k='Заголовок курса'
                elif choose==4:
                    k='Описание курса'
                elif choose==5:
                    k='Уровень'
                elif choose==6:
                    k='Цена в сомах'
                new_data=input('Введите новое значение: ')
                print(update_user(db, user_id,k,new_data))
            elif action==5:
                id_courses=int(input('Введите айди курса: '))
                delete_user(db,id_courses)
            else:
                print('Не корректный ввод!')


def get_user(data_base,user_id):
    for db in data_base:
        if db['id']==user_id:
            return db
    return None


def update_user(dict_list, dict_id, key, new_value):
    global db
    for item in dict_list:
        if item["id"] == dict_id:
            if key in item:
                item[key] = new_value
                print(f"Ключ '{key}' в словаре с ID {dict_id} успешно обновлен.")
            else:
                print(f"Ключ '{key}' не найден в словаре с ID {dict_id}.")
                print(f"Словарь с ID {dict_id} не найден.")

def delete_user(dict_list,dict_id):
    for i, item in enumerate(dict_list):
        if item["id"] == dict_id:
            del dict_list[i]
            print(f"Курс с ID {dict_id} успешно удален.")
        else:
            print(f"Курс с ID {dict_id} не найден.")
main()