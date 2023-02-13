'===================================================================Comprehensions==================================================================='
# Генератор, с помощью которого можно создавать последовательность используя цикл for

# list1 = []
# for i in range(1,11)
#     list1.append(i)
# # list1 = [1,2,3,4,5,6,7,8,9,10]
#         сократили внизу:
# list1 = [i for i in range(1,11)]
# print(list1)  == [1,2,3,4,5,6,7,8,9,10]

# результат for элемент in последовательность
# результат for элемент in последовательность if фильтр

# comprehension = (i for i in range(1,11))
# print(comprehension)

# <generator object <genexpr> at 0x7fbce27344a0>
#  генератор - итерируемый обьект, который не хранит в себе полностью все элементы последовательности, а генерирует их когда требуется

# print(next(comprehension))   #1
# print(next(comprehension))   #2
# print(next(comprehension))   #3
# print(next(comprehension))   #4

# hi = []
# for i in range(1,11):
#  if i % 2 == 0:
#     hi.append(i)
#     print(hi)

# res = []
# for i in range(1,11):
#     res.append(i*100)
#     print(res)

# res=[]
# res =[i *100 for i in range(1,11)]
# print(res)

# res = ['hello' for i in range(5)]
# print(res)

# [[1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5]]
# res = [[x for x in range(1, i+1)] for i in range(1,6)]
# print(res)

# res = []
# for i in range(1,6):
#     inner_list = []
#     for x in range(1, i+1):
#         inner_list.append(x)
#     res.append(inner_list)
# print(res)

# list1 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# res = [1,2,3,4,5,6,7,8,9,10,11,11,12]

# res = [i for inner_list in list1 for i in inner_list]
# # res = []
# # for inner_list in list1:
# #     for i in inner_list:
# #         res.append(i)
# print(res)


# # [1,2,3,4]
# # ['не четное', 'четное', 'не четное', 'четное']

# res = ['четное' if i%2==0 else 'не четное' for i in range(1,7)]
# print(res)