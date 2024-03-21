# 2) find the uncommon words from 2 strings
'''
s1="Hello how are you"
s2="Hello how is"
s1=s1.split(" ")
s2=s2.split(" ")
for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)
        
# Find the 8th fibanochi number

num=8
n1=-1
n2=1
for val in range(num):
    ans=n1+n2
    n1=n2
    n2=ans
    print(ans)

# Constructors
# Eg:2
# unparametarised constructor

class profile:
    def __init__(self):
        print("hello world")
obj=profile()
obj.__init__()

# * parametarised constructor

class profile:
    def __init__(self,id,name,age):
        print(id,name,age)
obj=profile(23,"reddy",45)

# Eg:4
class c1:
    name="obul"
    place="ckd"
    def m1(self):
        print(self.name,self.place)
object=c1()
object.m1()


class c1:
    email="obul@gmail.com"
    def m1(self):
        name="obul"
        place="ckd"
        print(name,place)
        print(self.email)
object=c1()
object.m1()

# Eg:5
class c1:
    def m1(self):
        name="sush"
        age=18
        return name,age
    def display(self):
        print(self.m1())
object=c1()
object.display()

# Eg:6
# To use the variable inside the constructor in another methods

class class1:
    def __init__(self):
         self.name="sush" # instance variable
         self.email="sus@gmail.com"
    def display(self):
         print(self.name,self.email)
c1=class1()
c1.display()

# --> Inheritance
The process of utilising the methods and attributes of parent class
# thought the object of child class it is called as inheritance
# 5 types of inheritance

     #Single Inheritance
     #Multilevel Inheritance
     #Multiple Inheritance
     #Hybrid Inheritance
     #Heirarichal Inheritance

# Single Inheritance
It has only one parent class and only one child class

# Eg:1
class parent:
    def m1(self):
        print("Iam parent class")
class child(parent):
    def m2(self):
        print("Iam child class")
obj=child()
obj.m1()

# Eg:2
class c1:
    def __init__(self):
        print("Iam constructor from parent class")
class child1(c1):
    pass
obj=child1()

# Eg:3
class parent:
    name="sus"
class child(parent):
    name="name1"
    def display(self):
        print(self.name)
d=child()
d.display()

# Multilevel inheritance
# Eg:1

class voice:
    def sound(self):
        print("All the animals have their own voices")
class dog(voice):
    def dog_voice(self):
        print("bark")
class cat(dog):
    def cat_voice(self):
        print("meow")
class parrot(cat):
    def parrot_voice(self):
        print("speak")
all=parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()

#eg:2
class honda_city:
    def honda_engine_specs(self,cc,hp,torque,fuel_type,num_of_pistion):
        print(cc,hp,torque,fuel_type,num_of_pistion)

    def honda_engine_specs(self,color,weight,hegiht,length,vechical_type):
        print(color,weight,hegiht,length,vechical_type)
class amaze(honda_city):
    def honda_engine_specs(self,cc,hp,torque,fuel_type,num_of_pistion):
        print(cc,hp,torque,fuel_type,num_of_pistion)

    def honda_engine_specs(self,color,weight,hegiht,length,vechical_type):
        print(color,weight,hegiht,length,vechical_type)
    
class civic(amaze):
    def honda_engine_specs(self,cc,hp,torque,fuel_type,num_of_pistion):
        print(cc,hp,torque,fuel_type,num_of_pistion)

    def honda_engine_specs(self,color,weight,hegiht,length,vechical_type):
        print(color,weight,hegiht,length,vechical_type)
class honda(civic):
    pass
honda = honda()
honda.honda_city_engine_specs(1500,230,2929,"petrol",4)
honda.civic_body_specs("while",2000,5.5,8,"hatchback")
#multiple inheritance
#it has multiple parent and 1 child
class while_petrol:
    def function_w(self):
        print("used for airplans")

class organic_petrol:
    def function_o(self):
        print("used for bike,cars")

class premium_petrol:
    def function_p(self):
        print("used for spots cars,bikes")
class petrol(while_petrol,organic_petrol,premium_petrol):
    def defanition(self):
        print("petrol types")
p=petrol()
p.defanition()
p.function_o()
#eg:2

class addition:
    def add(self,a,b):
        print(a+b)
class subtract:
    def sub(self,a,b):
        print(a-b)        
class multiply:
    def mul(self,a,b):
        print(a*b)
class division(addition,subtract,multiply):
    def div(self,a,b):
        print(a/b)
calc=division()
calc.add(3,4)
calc.mul(4,2)

#heirarical inheritance
class catagory:
    def weight(self,weight):
        print(weight)
    def display(self,color,taste):
        print(color,taste)
class tomato(catagory):
    def tomato_specs(self):
        color="black"
        taste="neutral taste"
        self.display(color,taste)
class carrot(catagory):
    def carrot_specs(self):
        color="green"
        taste="sweet"
        self.display(color,taste)
c=carrot()
c.carrot_specs()
c.weight("30gms")

# Hybrid inheritance
# The combination of above 4 inheritance is called Hybrid inheritance
class c1:
    def m1(self):
        print("class1")
class c2(c1):
    def m2(self):
        print("class2")
class c3(c2):
    def m3(self):
        print("class3")
class c4(c2):
    def m4(self):
        print("class4")
class c5(c3):
    def m5(self):
        print("class5")
class c6(c5,c4,c2,c1):
    def m6(self):
        print("class6")
obj=c6()
obj.m3()

# ---> polymorphism

# poly -many,morph ---> form
# A function which has the ability to perform more than 1 functionality
# then it is considered to be as plioymorphism

# ploymorphism in builtin functions
    # len() ---> which is used to find the length of list,tuple,dict etc
    # index()
      max()
      min()
      count()
      pop()
      and more...

# ploymorphism in operators
 # +
print(8+8)
print("k"+'1')
print([1,2,3]+[5,6])

 # *
print(6*7)
l1={1,2,3,4,5,6}
print(*11)

def f1(*args):
    l1=[1,2,3,4]
    print(l1*10)
'''

# ploymorphism in classes
# we can achieve polymorphism in 2 ways
1) method overloading -->it is not possible in python
2) method overriding



















