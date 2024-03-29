# Наследование
> Принцип ООП, где мы можем унаследовать, переопределять и использовать все аттрибуты  и методы родительского класса

```py
class A:
    def method(self):
        print("Методы в классе А")

obj_a = A()
obj_a.method()
#  Метод в классе А


class B(A):
    pass 


obj_b = B()
obj_b.method()
# Метод в классе А
```
> класс А - родительский
> класс В - дочерний

## Переопределение
> когда мы создаем метод или аттрибут с таким же названием, как и в родительских классах

```py
class C(A):
    def method(self):
        print("Метод в классе C")

obj_c = C(A)
obj_c.method()
# Метод в классе C
```


## Виды наследования
* **одиночное** (когда один родитель)
* **множественное** (когда неколько родителей)
* многоуровневые (когда есть дедушка бабушка, у родителя есть родитель)
* иерархическое (когда у каждого есть только один родитель, но к родителя может быть много детей)
* гибридное (совмещение разных видов наследования)

