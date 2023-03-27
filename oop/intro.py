class Person:
    arms = 2
    legs = 2

    def walk():
        print("я хожу")

    def walk(self):
        #self - сыылка на обьект, у которого мы вызываем данный метод
        print(self)
        print("я хожу")

person1 = Person()
#print(type(person1)) # __main__ # class - Person
# print(dir(person1))
# print(person1.arms)  # 2





# Аттрибуты класса и аттрибуты обьекта класса

class A:
    var1 = 'Переменная класса'

    def __init__(self):
        self.var2 = "переменная обьекта"

# print(dir(A)) #'var1']

obj = A()
print(dir(obj))


