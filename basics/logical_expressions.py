"===============================================================Логические выражения==============================================================="
# print (5 == 5) # '=' - знак присвоения  ===== "TRUE"
  # '=' - знак сравнения  

# print (4 ==5)   # "FAlSE"

# print (4 ! = 5) # '!' - не равно    ======== "TRUE"

# print ( 5 > 5 ) # FAlSE
# print ( 5 > 4 ) # TRUE

"==================================Больше или равно=================================="
# print (5 >= 10)  ===FAlse
# print (5>= 5)  =====True

# print ('5' == 5)   ==== FAlse ==потому что там str + int   нельзя
# print ('Hi' =='Hi')   === True
# print ('Hi' == 'hi')  === False

"=====================================================================AND OR NOT====================================================================="

# a = 5
# b = 6
# print (a == 5 and b == 6) === True
# print ( a == 4 and b == 6) === False

# a = 5
# b = 6
# print (a == 4 or b ==3) === False
# print (a == 5 or b == 3) === True # если одно из будет правильно то уже тру будет ежже

# print (not a == 5)  ==== False # 'not' - не, типо "а" не равен 5, поэтому фолс
# print (not a == 3 and not b ==6) ===FAlse # 1 тру, 2 фолс, потому что "and" смотрит на 1 и 2 понял да
# print (not a == 3 or not b ==6)  ===True # потому что "or" или или смотрит

# print (not True) == False
# print (not False) == True

"===================================================================Boolean Type==================================================================="
#                                                         у булевого типа всего 2 значения: True и False
#True == не пустота, а FAlse == пустот

# print(bool(1)) === True
# print(bool(0)) === False # "0" это ничего

# print(bool(-11)) == True

# print (bool('hello')) == True
# print(bool(' ')) == True
# print(bool(""))  ===false

# print (bool([])) === False
# print (bool([[]])) == True

"====================================================================None Type===================================================================="
#  None - неизменяемый тип данных с одним значением None, который используется для обозначения пустоты

# print (bool(None))  === FAlse
# print (bool("None"))  == True == потому что есть строка в ковычках, читает как строку в ковычках ""

"==================================================================Условные операторы=================================================================="
#  Условные операторы - это конструкция, которая используется чтобы при разных входных данных код работал по-разному (в зависимости от условия)

# if условие1:
#     тело1
#     # тело1 будет выполняться только если условие1 верно

# if условие1:
#     тело1
#     # тело1 будет выполняться только есои условие1 верно
# else:
#     # тело2 будет выполниться во всех других случаях

# if условие1:
#     # тело1 будет выполняться только если условие1 верно
# elif условие2:
#     # тело2 будет выполняться только если условие1 не верное и если условие2 верное 
# else:
#     тело3
#     # тело3 будет выполняться во всех других случаях



# В одной конструкции мы можем использовать только один if
# В одной конструкции мы можем использовать неограниченное количество elif или не испоотзовать вообще
# В одной конструкции мы можем использовать только один else или не испоотзовать вообще


# num = int(input("введите число: ")) 
# if num > 0: 
#    print(f'число {num} - положительное')

# elif num ==0:
#    print(f' число {num} -это 0')

# else:
#    print(f'число {num} - отрицательное')

# password = input('Придумайте свой пароль: ')
# upper_let = password[0].upper()

# if len(password) <= 8:
#     print('Ваш пароль меньше 8 символов')

# elif not password.startswith(upper_let):
#     print('Ваш пароль не начинается с большой буквы')

# else:
#     print('Пароль успешно создан')

"=========================================================Тернарные операторы=========================================================================================="
# Тернарные операторы - условие в одну строку

# тело1 if условие else тело2
# num = int(input())

# res = 'Hello' if num == 5 else "Bye"
# print(res)

# num = int(input("Введите число: "))
# if num % 3 == 0:
#     print('Fizz')

# elif num % 5 == 0:
#     print('Buzz')

# elif num % 3 == 0 and num % 5 == 0:
#     print('FizzBuzz')

# else:
#     print(num)



































