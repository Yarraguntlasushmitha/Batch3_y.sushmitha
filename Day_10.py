'''
#method riding
#ploymorphism in classes using interitance
#eg:1
class bank:
    def ratio(self):
        print("all banks has repo rate")
class sbi(bank):
    def ratio(self):
        print("sbi rate is 9%")
class iob(bank):
    def ratio(self):
        print("iob rate is 7.5%")
i=iob()
i.ratio()
s=sbi()
s.ratio()
#eg:2
class usa:
    def language(self):
        print("english")
    def capital(self):
        print("washington dc")
class india(usa):
    def language(self):
        print("none")
    def capital(self):
        print("new delhi")
i=india()
i.language()
i.capital()

#eg:3
#polymorphism using objects
#c1,c2-->c1=print(c1),print(c2)
#f1,f2
class c1:
    def f1(self):
        super().f1()
        print("class 1")
class c2:
    def f1(self):
        print("class 2")
obj1=c2()
obj1.f1()

class c1:
    def f1(self):
        print("class 1")
class c2:
    def f1(self):
        print("class 2")
obj1=c2()
obj2=c1()
def display(a):
    a.f1()
display(obj1)
display(obj2)

#changing the functionality of builtin functions
a=9
b=6
print(a+b)
print(a.__add__(b))
int()
print(a.__sub__(b))
#eg:4
class shooping:
    def __init__(self, l1):
        self.items=l1
    def __len__(self):
        length=len(self.items)
        return length
s=shooping([1,2,3,4,5])
print(len(s))

#method overloading
#eg:1
class suming:
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
s=suming()
#s.add(3,4)  is error because their are only two numbers
s.add(4,5,1)
#eg:2
class summing:
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print(a)
obj=summing()
obj.add(2)
obj.add(2,4)
obj.add(1,2,3)

#-->abstraction
#the process of hiding the implimentation detailsis abstraction
#eg:1
#class shapes:
#    def sides(self):
#        print('All shapes have sides except circle')

#class triangle:
#    def triangle_sides(self):
#        print("3 sides")
#class square:
#    def square(self):
#        print("4 sides")
#    def sides(self):
#        pass

#s = shapes()
#s.sides()

#tr = triangle()
#tr.triangle_sides()
eg:3
def decor(func):
    def inner():
        str1 = func()

def greet():
    return 'good morning'

print(decor(greet))


# ! Rules to define abstract class 1
1.) Abstract class cannot be instantiated
2.) From abc import ABC, abstractmethod
3.) subclass the normal class with ABC
4.) Convert the normal method inside the abstract class to abstract method
5.) All the child classes have to be subclassed with abstract class
6.) The abstract method should be present in the child classes

#eg:4
#super()-->used to access the parent class method from child class method
from abc import ABC, abstractmethod
class c1(ABC):
    @abstractmethod
    def m1(self):
        print("this is abstract class")
class c2(c1):
    def m2(self):
        super().m1()
        print("iam child 1")
    def m1(self):
        pass
class2=c2()
class2.m2()

#eg:5
from abc import ABC, abstractmethod
class password(ABC):
    @abstractmethod
    def pwd(self):
        pswd = "sidd1994$"
        return pswd
    

class login(password):
    def validate(self, name, password):
        if super().pwd() == password:
            print("welcome", name, '||')
            print("Login Sucessful")
        else:
            print("Please check the password")

    def pwd(self):
        pass

Login = login()
name = input("Enter the name: ")
pwd = input("enter the password: ")
Login.validate(name, pwd)

#encapsulation
#eg:1
class car:
    __name="bmw" #private variable
c1=car()
print(c1.name)
c1.name="audi"
print(c1.name)

#eg:2
#accessing private date outside the class
class c1:
    __phone="766564321"
    def display(self):
        print(self.__phone)
c=c1()
c.display()
#eg:3
#declare private method
class class1:
    def __m1(self):
        print("iam private method")
    def __init__(self):
        self.__m1()
c=class1()
#c._m1()
'''
#nested class
class class1:
    class class2:
        name="sus"
        def display(self):
            print(self.name)
    obj1=class2()
obj=class1()
obj.obj1.display()
class c1:
    name="sus"
obj=c1()
print(isinstance(obj.c1))









