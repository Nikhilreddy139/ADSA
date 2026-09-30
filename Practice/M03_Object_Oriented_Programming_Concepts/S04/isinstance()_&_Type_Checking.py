'''Type Checking: To check the value of particular type()'''
a = 10
b = 10.5
c = "Hello"
d = [1,2,3]
e = (1,2,3)
f = {1,2,3}
g = {"name":"Akhil","age":20}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
'''
isinstance() : To check the value() of particular datatype() or class
it gives True if the value is of that type or class otherwise it gives False
'''
a = 10
b = 10.5
c = "Hello"
d = [1,2,3]
print(isinstance(a, int))
print(isinstance(b, float))
print(isinstance(c, str))
print(isinstance(d, list))

#Duck Typing : same method acts as same behaviour,we can use same behaviour 
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

def process_data(data):
    if isinstance(data, int):
        return data*2
    elif isinstance(data, str):
        return data.upper()
    elif isinstance(data, float):
        return data * 10.5
print(process_data(10))
print(process_data("hello"))

#Interview Question:
class A:
    pass
class B(A):
    pass
obj = B()
print(type(obj)==B)
print(type(obj)==A)
print(isinstance(obj,B))
print(isinstance(obj,A))
