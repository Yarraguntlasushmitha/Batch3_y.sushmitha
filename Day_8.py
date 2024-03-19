'''
def profile(name,age,place):
    txt="My name is {}.iam {} year old.iam from {}."
    print(txt.format(name,age,place))
profile("sush",20,"ckd")
# Eg:4
# Function with return statement
# Return
# 1) A variable declared inside the function can be accessed using return
# 2) Return does not print anything
# 3) we cannot write any code below return statement
def f1():
    z=8
f1()
print(z) # error ---> cannot use outside the funciton

def f1(a,b):
    c=a*b
    return c
obj=f1(6,8)
def gracemark(object):
    print(object+4)
gracemark(obj)

# 123 it is a panidrome in python code
num = input("Enter a number")
if num == num[::-1]:
    print("its a palindrome")
else:
    print("its not a palindrome")

# problem:1
def palindrome(n):
    string=str(n)
    rev=str(n)[::-1]
    if string==rev:
        print(n,"palindrome")
    else:
        print("not palindrome")
a=int(input("enter the value:"))
palindrome(a)

# Based on the declaration of parameter and args
# Functions are divided into 5 catagories

    # Positional args
    # Keyword args
    # Default args
    # Variable length args
    # Key variable length args

# Positional args
# The position of parameter have to be same as position as arguments
# Eg:1
def profile(name,phone,mark):
    txt="My name is {}. My phone number is {}. I got {} marks."
    print(txt.format(name,phone,mark))
profile(9878675643,"sidhu",98) # unexpected output

# Keyword args
# Eg:1
# To overcome the disadvantage of position args,we use keyword args
# It is the process of initialising the parameter with the args while calling the function

def profile(name,phone,mark):
    txt="My name is {}. My phone number is {}. I got {} marks."
    print(txt.format(name,phone,mark))
profile(phone=9878675643,name="sidhu",mark=98) 

# ---> Exception of keyword args function

def profile(name,phone,mark):
    txt="My name is {}. My phone number is {}. I got {} marks."
    print(txt.format(name,phone,mark))
#profile(name="sidhu",1234567890,mark=98)# error ---> positional arg follow keyword args 
#profile(9878675643,name="sidhu",mark=98)# error --> name has multiple values
profile(name="sidhu",mark=98,phone=1234567890) 

# Default args
   # The method of assigning the argument to the parameter while declaring the function
# Eg:1
def profile(name,phone,place="kadapa"):
    txt="My name is {}. My phone number is {}. I am from {}."
    print(txt.format(name,phone,place))
profile(9878675643,"sidhu") 
# Eg:2

def profile(name,phone,place="kadapa"):
    if place == "kadapa":
       txt="My name is {}. My phone number is {}. I am from {}."
       print(txt.format(name,phone,place))
    else:
        print("you are not eligiable to signup")
profile(9878675643,"sidhu","guntur") 

# Exception

def profile(name,place="kadapa",phone):# error --> coz default args should not for positional param 
    if place == "kadapa":
       txt="My name is {}. My phone number is {}. I am from {}."
       print(txt.format(name,phone,place))
    else:
        print("you are not eligiable to signup")
profile(9878675643,"sidhu")

# Variable length params
# To pass more then 1 arg to a parameter means we use variabie length args
# To convert normal parameter to variable length param,add*to the prefix of param

# Eg:1
name="sid",'name2','name3'
def profile(*name):
    for val in name:
        print("My name is",val)
profile("sid",'name2','name3')

# Eg:2
def profile(age,*name):
    for val in name:
        print("My name is",val,"may age is",age)
profile(28,"sid",'name2','name3')

# Keyword variable length args
# Eg:1
def price(**price_list):
    print(price_list)
price(shirt=1000,iphone=80000)

# n=5
#{1:1,2:4,3:9,4:16,5:25}
n=int(input("enter the number:"))
d1={}
for val in range(1,n+1):
    d1[val]=val**2
print(d1)

def dict1(n):
    d1={}
    for val in range(1,n+1):
        d1[val]=val**2
    print(d1)    
dict1(5)

# ---> object oriented programming
# The paradigms of objects oriented progarmming are

        # Class
        # objects
        # Inheritance
        # Polymorphism
        # Abstraction
        # Encapsulation
        
# class is a blue print of an object
# Eg:1
class c1:
    name1="sai"
    print(name1)
    
# Eg:2
class person:
    name="sus"
c=person() # c as object
# The process of creation of object is called as Instantiation
print(c.name)

# Eg:3
# create of a method
# when the function is created with a class is called as method

Method without parameter

class person:
    def display(person): # It is a method
        print("Hello welcome to classes")
p=person()
p.display()

# Eg:4
# Method with parameter

class person:
    def display(person,name,age):
        print(name,age)
p=person()
p.display("vasi",10)

# Eg:5
class person:
    name="sai" # attribute of static variable
    def display(person):
        print(person.name)
p=person()
p.display()

class person:
    fname="sai"
    lname="Y"
    def first_name(person):
        print(person.fname)
    def full_name(person):
        print(person.fname+" "+person.lname)
p=person()
p.first_name()
p.full_name()
'''
# Eg:6
# constructors --> __init__()
# This is a special method which has the ability to execute iotself without
# calling it manullay theorugh the process of instantiation

class profile:
    def__init__(self):  # constructor method
        print("hey")
p=profile() # execution of constructor through this processs




























