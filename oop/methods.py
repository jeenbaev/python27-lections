class A:
    def instance_method(self):
        print("метод обьекта")
        print("self", self)

obj = A()
obj.instance_method()
# метод обьекта
# self <__main__.A object at 0x7fc73bf57ac0>
# когда мы вызываем метод у обьекта, то нам не нужно передавать его в self, он передается автоматически

A.instance_method(obj)
# метод обьекта
# self <__main__.A object at 0x7fc73bf57ac0>
# когда мы вызываем метод у класса, то нам нужно передавать обьект


class A:
    @classmethod
    def class_method(cls):
        print("метод класса")
        print("cls", cls)

A.class_method()
obj = A.class_method()

# метод обьекта
# cls <class '__main__.A'>
#  всё равно от куда вы будете вызывать classmethod (от обьекта или класса), первым аргументом будет приходить класс

#  ex
class C:
    counter = 0

    def __init__(self):
        # обьект создается
        # C.counter += 1
        self._inc_counter()
    def __del__(self):
        # обьект удаляется
        # C.counter -= 1
        self._dec_counter()


    @classmethod
    def _inc_counter(cls):
        # cls - class C
        # увеличиваем аттрибут класса counter на один
        cls.counter += 1


    @classmethod
    def _dec_counter(cls):
        cls.counter -= 1

obj1 = C()
obj2 = C()
obj3 = C()
obj4 = C()
print(C.counter) #4 
del obj1
print(C.counter) #3


class Pizza:
    def __init__(self, radius, *ingridients):
        self.r = radius
        self.ingridients = ingridients

    def cook(self):
        print(f"Пицца размером {self.r*2}")
        print(f"Ингридиенты: {self.ingridients}")

pizza1 = Pizza(15, "Сыр", "Колбаса", "Cherry")
pizza1.cook()

pizza2 = Pizza(10, "1 сыр", "2 сыр", "3 сыр", "4 сыр")
pizza2.cook()





    