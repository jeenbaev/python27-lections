"===================================================================Строки========================================================================="
# строки - неизменяемый тип данных, предназначенный для хранения текста (последлвательность символов)

string1 = 'строка в одинарных кавычках'
string2 = "строка в двойных кавычках"  # bez raznicy kakie kavy4ki
string3 = "Don't" # можно мутить внутри
string4 = 'Study in "Makers Incubator"' # можно внутри мутить
string5 = 'dbsfhkdbks
sdfbsjk'  # так нельзя
string6 = '''ahsufbakfek
bfsjk
bsd
'''   # так можно через три кавычки черех строчки ежже и внутри можно юзать любые кавычки (''; "")
string7 = 'hello' '+'  '+' 'world'     # 'hello world'
string8 = 'hello' * 3   # 'hellohellohello'



"===============================================================Экранизация строк==============================================================="
'\n' # Перенос на новую строку 'enter'
'\t' # Отступ (tab)
'\\' # отображение \
'\'' # отображение символа '
"\"" # отображение символа "
'\r' # перезапись начальную букву # hello\rw = wello
'\v' # на строчку вниз # hello\vhi\vhru?

'hello\nworld'
# hello
#world
'hello\tworld'
# hello     world
'hello\\'
# hello\
'123456789\rhello'
# hello6789
'hello\vworld\vmakers'
# hello
       #world
             #makers


"=================================================================Индексы=============================================================="
# индекс - порядковый номер символа в строке (начиная с 0)
 'h e l l o'
# 0 1 2 3 4
#  -4-3-2-1 


string = 'hello world'
# последний символ найти = print(string[-1])  = "d"
# первый символ найти = print(string[0]) = "h"
#string[5] "пробел"

string56 = 'hello world'
# срез - часть строки оставить
string56[6:9]  # 'wor'
string56[0:5]  # 'hello'
string56[0:6]  # 'hello '
string56[:6]   # 'hello '
string56[7:]   # 'orld'
string56[:]    # 'hello world'
string56[0:11:2] # 'hlowrd' срезает через одну
string56[::2] # 'hlowrd' срезает каждую вторую
string56[::-1]


"==========================================================Форматирование строк=========================================================="
title = 'Пирог'
price = 35
string = f'Название: {title}, цена: {price}'
print(string)  # Название : пирог, цена: 35
# f - делает дело, читает и печатает всё как надо

format1 = 'Название: %s, цена: %s'
print(format1 % ('Яблоко', 80))
# Название: Яблоко, цена: 80

format2 = 'Название: {}, цена: {}'
print(format2.format('Груша', 60))
# Название: Груша, цена: 60


"=============================================================Методы строк============================================================="
# метод - футкция, которая принадлежит определенному типу данных, обращаемся к ней через точку

print(dir(str)) # dir - методы которые доступны для типов данных

dir(str) # посмотреть все доступные методы для данного типа данных

print('hello'.upper())  # 'HELLO'  # делает все с большой буквы
      'HELLO'.lower()   # 'hello'  # делает с мелкой буквы

'hello WORLD'.swapcase() # 'HELLO world' # меняет буквы наоборот
'HeLLo'.swapcase() # 'hEllO' # меняет буквы наоборот

'hello world'.title()   # 'Hello World' # пишет буквы слов с заглавной

'hello world'.capitalize()  # 'Hello world' # пишет первую букву с заглавной

'hello'.center(11) # ставит по середине этих (11) # '---hello---'

'hello'.count('l') # 2
'hello'.count('ll') # 1
'Hello'.count('hello') # 0 # потому что с маленькой буквы видишь да ха-ха
'hello'.count('') # 6 

'hello world'.split() # ['hello', 'world']
'hello world'.split('o') # ['hell', 'w', 'rld']

' '.join(['hello', 'world']) # 'hello world'
'%'.join(['hello', 'world']) # 'hello%world'

'hello world'.find('w') # 6
'hello world'.find('wor') # 6
'hello world'.find('o') # 4
'hello world'.rfind(o) # 7 #right_find potomu-4to 














