# class A:
#     def method(self):
#         print("Методы в классе А")

# obj_a = A()
# obj_a.method()
# #  Метод в классе А


# class B(A):
#     pass 


# obj_b = B()
# obj_b.method()
# # Метод в классе А



# class C(A):
#     def method(self):
#         print("Метод в классе C")
 
# obj_c = C(A)
# obj_c.method()
# # Метод в классе C


# class A:
#     def method(self):
#         print("Метод в классе А")
#         return "AAA"
    
# class B(A):
#     def method(self):
#         print("Метод в классе B")
#         return_from_super = super().method()
#         print("super().method() вернул", return_from_super)
#         return "BBB"
    


# obj_a = A()
# res_a = obj_a.method()
# print("A.method вернул", res_a)
    

# obj_b = B()
# res_b = obj_b.method()
# print("B.method вернул", res_b)



# class Range:
#     def create(self, n):
#         """Принимает число и возвращает список чисел от 0 до данного числа веключительно"""
#         return list(range(n+1))
    

# class Range10(Range):
#     def create(self):
#         """Возвращает список чисел от 0 до  включительно"""
#         return super().create(10)


# range_obj = Range()
# res = range_obj.create(5)
# print(res)
# # [0, 1, 2, 3, 4, 5]

# range10_obj = Range10()
# res = range10_obj.create()
# print(res)
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]





class A:
    attr1 = 'a'
    
    def method(self):
        print("Мктод в классе А")



class B:
    attr2 = 'b'

    def method(self):
        print("Мктод в классе B")



class C(A,B):
    pass


 