'''
Polymorphism:
Poly == Many
Morph == Forms

Types of Polymorphism:
1. Compile Time Polymorphism (Static Polymorphism)
    Function Overloading 
    operator Overloading
2. Runtime Polymorphism (Dynamic Polymorphism)
    Method Overriding
'''
# def add(a, b):
#     return a + b
# def add(a, b, c):
#     return a + b + c
# def add(a, b, c, d):
#     return a + b + c + d

# print(add(10,20))
# print(add(10,20,30))
# print(add(10,20,30,40))

'''
Python does not support function overloading directly 
we can achieve this variable-length arguments(using *)'''
# def add(*values):
#     return (values,type(values))
# print(add(10,20))
# print(add(10,20,30))
# print(add(10,20,30,40))
'''Operator overloading'''
# class A:
#     def __init__(self, a):
#         self.a = a
#     def __add__(self, other):
#         return self.a + other.a

#     def __sub__(self, other):
#         return self.a - other.a
# a = A(10)
# b = A(20)   
# print(a + b) 
# print(a-b)
'''Example'''
# class B:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def __add__(self, other):
#         return (self.a + other.a, self.b + other.b)
#     def __sub__(self, other):
#         return (self.a - other.a, self.b - other.b)
# a = B(10,20)
# b = B(30,40)
# print(a + b)#(40, 60)
# print(a - b)#(-20, -20)
'''Method Overriding: Same method name in parent and child class'''
# class Parent:
#     def display(self):
#         print("Parent class display method")
# class child:
#     def display(self):
#         print("Child class display method")

# c = child()
# c.display()
# Parent.display(c)
'''Duck Typing'''
class Dog:
    def Sounds(self):
        print("Bark")
class Cat:
    def Sounds(self):
        print("Meow")
def make_sound(animal):
    animal.Sounds()
make_sound(Dog())
make_sound(Cat())
