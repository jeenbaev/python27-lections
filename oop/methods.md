#  class/static/instance methods
> **instance method** - методы, которые первым аргументом принимают обьект от класса (instance, self). используются для работы с обьектом и его аттрибутами

```py
class A:
    def instance_method(self):
        print("метод обьекта")
        print("self", self)

obj = A()
obj.instance_method()
```

> **class methods** -методы, которые первым аргументом принимают класс (cls). используются для работы с классом и его аттрибутами


```py
class A:
    @classmethod
    def class_method(cls):
        print("метод класса")
        print("cls", cls)

A.class_method()
```