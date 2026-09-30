#Single inheritance
class Animal:
    def eat(self):
        print("Animal eats")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
d = Dog()
d.eat()
d.bark()
#Multiple inheritance
class A:
    def show(self):
        print("A")
class B:
    def display(self):
        print("B")
class C(A, B):
    pass
x = C()
x.show()
x.display()
#Multilevel inheritance
class A:
    def show(self):
        print("A")
class B(A):
    pass
class C(B):
    pass
x = C()
x.show()
#Hierarchical inheritance
class A:
    def show(self):
        print("A")
class B(A):
    pass
class C(A):
    pass
B().show()
C().show()
#Hybrid inheritance
class A:
    def show(self):
        print("A")
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass
D().show()

