"======================================================================Словари======================================================================"
#  dict - изменяемый, итерируемый, неупорядоченный, неиндексируемый тип данных, предназначенный для хранения данных в парах (ключ: значение)

# user = {
#     'name':'Bek',
#     'age': 13,
#     'last_name':'Hui'
# }

# print(user['name']) # 'Bek'

# ключи в словаре будут уникальными, поэтому если в словарь добавить значение по уже существующему ключу, то сохранится последнее значение
dict1 = {'a':1, 'b':2, 'a':3, 'c':2}
# {'a':3, 'b':2, 'c':2}
a = 1
b = 2
a = 3
c = 2
# a=3 b=2 c=2


# ключами могут быть только хешируемые типф данных (неизменяемые типы данных)
# print(hash(10)) #10
# print(hash('hello')) #1751897364732039454
# print(hash([1,2,3])) #TypeError: unhashable type: 'list'
# print(hash( (1,2,3) )) #529344067295497451
# print(hash( (1,2,3,[]) )) #TypeError: unhashable type: 'list'

# dict2 = {
#     [1,2,3]:'hello'
# }
# dict2['hello'] #[1,2,3

# dict1 = {'a':1, 'b':2, 'c':3}
# dict1['d] # KeyError: 'd'

"================================================================Создание====================================================================================="
# dict1 = {'a':1, 'b':2, 'c':3}
# dict2 = dict([('a', 1),('b', 2)])   #{'a':1, 'b':2}

# list1 = ['a', 'b', 'c']
# list2 = [1,2,3]
# dict3 = dict(zip(list1, list2)) # {'a':1, 'b':2, 'c':3}
# dict4 = {}
# dict4['name'] = 'Bek'
# dict4['last_name'] = 'Hui'
# print(dict4) #{'name': 'Bek', 'last_name': 'Hui'}
"=================================================================Методы ==============================================================================================="
# get - метод, который принимает в себя ключ. Если такой ключ есть - возвращает его значение. Если такого ключа нет - возвращает None (или default значение)

#  user['id'] # KeyError:'d'

# get - идёт дальше без остановки, если не правильно будет, то он дальше пойдет.
# default - возвращается если ключа нет, если есть ключ, возвврашается его значение

# pop - метод, который принимает ключ, удаляет пару под этим ключем. Возвращает удаленное значание
# pop - удаляет просто

# dict1 = {'a':1,'b':2,'c':3}
# deleted = dict1.pop('a')
# print(dict1) # {'b': 2, 'c': 3}
# print(deleted) # 1


# popitem - метод, который удаляет пару, которая была добавлена последней в словарь

# dict1 = {'a':1,'b':2,'c':3}
# res = dict1.popitem('a')
# print(dict1) # {'a':1,'b':2}
# print(res) # ('c', 3)

#  update - расширяет словарь, вторым словарём
# dict1 = {'a':1}
# dict2 = {'b':2}
# dict1.update(dict2)
# print(dict1) #{'a': 1, 'b': 2}
# print(dict2) # {'b': 2}

"=============================================================keys, values, items============================================================="
# # keys - 
# ключи 
# # values -
# values - значения
# # items -
# пары возвращает 

# dict1={'a':1, 'b':2, 'c':3}

# d1 = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e'}

# d2 = {'a':1,'b':2, 'c':3, 'd':4, 'e':5}

# for i in d1:
#   if i == 1:
#     d2[1] = d1[i]
#   else:
#     d2[i] = d1[i]
# print(d2)



# dict1 = {
#     'a':{'key':1},
#     'b':{'key':2},
#     'c':{'key':3}
# }

# res = dict1(zip(dict1.keys(), dict1.values)) 
# dict1.pop(dict1.values)

# print(res)




