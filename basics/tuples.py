"=================================================================Кортеж================================================================="
# tuple - неизменяемый, итерируемый, индексуемый и упорядоченный тип данных, предназначенный для хранения элементов в строгом порядке.(в целом не отличаются от списков, просто неизменяемый, поэтому занимает меньше памяти)

# tuple1 = (1, 2, 3, 4)
# tuple2 = (5) # int
# tuple3 = 1, 2, 3, 4 # tuple
# tuple4 = 5, # tuple (5,)
# tuple5 = (1, 'hello', [2, 3, 4])
# tuple5[-1].append(5)  # (1, 'hello', [2, 3, 4, 5])
# tuple6 = tuple('hello')
# print(tuple6) # ('h', 'e', 'l', 'l', 'o')
"===============================================================Методы Tuples==============================================================="

# count - считает кол-во данного элемента в tuple
# tuple1 = (1,2,1,4,1,5,1,6)
# print(tuple1.count(1)) #4
# print(tuple1(count('hello'))) # 0

# index - возвращает индекс данного элемента в tuple
# tuple1 = ('hello', 'world', 105)
# print(tuple.index())