#----->swapping of variables
#eg:1
'''
a=7
b=5
temp=a #temp=7
a=b #a=5
b=temp  #b=7
print(a,b)

a=7
b=5
a,b=b,a
print(a,b)
#Eg:2
a=a+b  #7+5=12
b=a-b   #12-5=7
a=a-b   #12-7=5
print(a,b)
'''
#id()--->used to find the memory address of the variable
#a=7
#b=8
#print(id(a))
#print(id(b))
#----> keywords are reserved words which provides special meaning to
# compiler or interpretor
#import keyword
#print(keyword.kwlist)
#print(type(keyword.kwlist))
#To check if the string is keyword or not
#print(keyword.iskeyword("sid"))#false
#if = 8
#print(if) #error coz if is a keyword
'''
#!--->literals
#literal is the constant value assigned to a variable
#A variable is considers to be constant when it is defines
# in caps
#a=78 #a is variable
# A=78 # A is constant
'''
# hash()---> it creates a hash value formconstant datatypes and
# provides error for non constant datdtypes
#n1=89+7j
#print(hash(n1))
#f1=(7,8,9)
#print(hash(f1)) #error---> list is non-constant or mutable datdtype
#a=9
#b=9
#print(id(a))
#print(id(b))
'''
#!---> operators
# operators are symbols which is used to perfeorm various operions
# between 2 or more operands
# Arithmatic
# Assegment
# Logical
# Relational or comparison
# Bitwise
# Identity
# Membership
'''
# --->Arithmatic -->+,-,*,/,%,//,**
#Eg:1
#a=8
#b=6
#c=9
#print(a+b+c)
#input()---->used to get the runtime input
# eval()--->used to get the runtime values of all datatype
#n1=eval(input("enter the value:"))
#print(type(n1))
#a=4
#b=2
#print(a/b) # is used to get the quotient value
#print(a%b) # is used to get the remainder value
# // --> floor division
# a=78786
#b=19
#print(a//b) # the output will be inn integer &the output
#based on floor value
# ** ---> used for power of a number
# print(2**6) #--->64 
'''
# Assignment --> +=,-=,/=,*=,//=,**=,&=,|=
a=8
a+=2
print(a)
a=30
a-=5
print(a)
'''
#-->comparison-->==,>,<,!=,<=,>=
#a=8
#b=7
#print(a>b)
#a=9
#b=5
#print(a==b)
'''
# --->Bitwise operator--->&,|,^,~,<<,>>
a=7
b=4
print(a&b)
print(a|b)
print(a^b)
# ~ ---> tillday
a=9
print(~a)
# <<,>> shift
print(5>>1)
#16>4
'''
# Locial -->used to compare the expressions
# and, or, not
#a=6
#print(a>3 and a<10)
#print(a>7 or a<30)
#print(not(a>8 and a<10))
'''
# -->Identity operation
# it is used to compare the memory location are stored
#is,is not
#a=8
#b=8
#print(a is b)
#print(a==b)
#a=[1,2,3]
#b=[1,2,3]
#print(a is not b)
'''
# Membership operator
# in, not in
#l1=[7,8,9,0,6,5]
#num=55
#print(num not in l1)
#num=678
#print(8 in num) #error
"""
# conditional statement
# if, elif, else
# --> if condition
#Eg:1
a=6
if a:
    print("hello")
#Eg:2
a=7
if a>3:
    print("hey")
else:
     print("no")
#Eg:3
if 7>8:
    print("hello")
print("no")
#eg:4
a=0
a=None
a=False
a=""
if a:
    print("yes")
else:
    print("no")
"""
#a number is even or odd
a=4
if a:
    print("even")
else:
    print("odd")

n=int(input("enter the number: "))
if n%2==0:
    print(n,"is even")
else:
    print(n,"is odd")











