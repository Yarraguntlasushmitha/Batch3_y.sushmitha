# Eg:3
# Take values of length and breadth of a
# from user and check if it is square or not.
#n1=int(input("enter the length "))
#n2=int(input("enter the breadth "))
#if n1==n2:
   # print("its a square")
#else:
     #print("its not a square")
'''
#eg:4
# python program to check whether the
# given integer is a multiple of both 5 and 7
n=int(input("enter the number:"))
if n%5==0 and n%7==0:
    print("yes")
else:
    print("no")
'''
# Eg:5
# writr a program to accept the cost price of a bike and display the
# road tax to be paid according to the following criteria:
#cost price (in Rs)         Tax
# > 100000                   15 % + discount 6%
# > 50000 and <= 100000      10%
# <= 50000                   5%
#price=int(input("enter the price: "))
#amount=0
#if price>=100000:
    #discount=price*(6/100)
    #value=price-discount
    #tax=value*(15/100)
    #total=value+tax
#else:
    #tax=price*(5/100)
    #total=price+tax
#print("The on road cost of bike is: ",total)
"""
#if elif
# Eg:1
a=7
b=2
c=9
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
     print("b is greater")
elif c>a and c>b:
     print("c is greater")

# A school has following rules for grading system:
# a. Below 25 -F
# b. 25 to 45 -E
# c. 45 to 50 -D
# d. 50 to 60 -C
# e. 60 to 80 -B
# f. Above 80 -A
# Ask user to enter mark and print the corresponding grade.

n= int(input("enter the mark"))
if n<=25:
    print("F")
elif n>=25 and n<=45:
    print("E")
elif n>=45 and n<=50: 
    print("D")
elif n>=50 and n<=60:
    print("C")
elif n>=60 and n<=80:
    print("B")
elif n>=80:
    print("A")
"""
# ---> short hand if else
# Eg:1
#a=9
#b=60
#if a>b:
    #print("A")
#else:
    #print("B")   
# ----> using short hand if else
# Rules
# 1) statement inside the if condition have to be present at first
# 2) elif cannot be used in short hand if else
# 3) always it have to end with else

#print("A") if a>b else print("B")
# code to check the given char is vowel or consonent
#char=input("enter the char: ")
#if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
    #print("is a vowel")
#else:
    #print("its consonent")

# or
#str1="aeiouAEIOU"
#if char in str1:
    #print("vowel")
#else:
    #print("consonent")
# short hand if else
#char=input("enter the char: ")
#str1="aeiouAEIOU"
#print("vowel") if char in str1 else print("consonent")

# -->elif ladder using short hand if else
# Eg:1
# Find greater among 3 variables using short hand if else
#a=8
#b=5
#c=9
#print("A is greater") if a>b and a>c else print("B is greater") if b>a and b>c else print("C is greater")
'''
# ------>Looping
# Looping can be implimented using
# for loop
# while loop

# -----> for loop
#for loop is used for iteartion, if we know the number of times the loop have to run
# it is used to iterate the iterables eg(string,list,tuple,etc...) 
# todo ----> syntax for loop
# for syntax in c
#for(i=0;i<10;i++){
#print("hello");
#}

# for syntax in python
# for userdefined_variable in range(start, end, step): default step value is 1
#      statement
#      statement
#      statement

'''
# Eg:1
#To print the value from 1 to 10 using for loop
#for i in range(0,10): #(n,n-1)
    #print(i)
    #print("hello")

# Eg:2
#for val in range(23,50,2):
   # print(val)
   
# Eg:3
# To decrement the value
#for val in range(10,0,-3):
    #print(val)

# Eg:4
#print the ooutput of 7th multiplication table from 21 to 43
#for i in range(3,10-3):
    #print(i*7)

#for i in range(1,10+1,):
    # print('7','x',i,'=',i*7) ----->method:1
    # method:2
     #ans="7 x {} ={}"
     #print(ans.format(i,i*7))

    #---> method:3
    #print(f"7 x {i}={i*7}")
"""    
# Eg:5
# Break --> used to terminate the loop
for val in range(1,10):
    if val==6:
        break
    print(val)
# eg:6
for val in range(1,10):
    print(val)
    if val==6:
        break  

# eg:7
for val in range(1,10):
    if val==6:
        print(val)
        break
        
# ---> continue
# Eg:1
#for val in range(1,10):
    #if val==6:
       # continue
    #print(val)

#-->practise problems
# print the even number b/w 20 to 40
for i in range(20,41):
    if i%2==0:  or (odd if i%2!=0:)
       print(i)

# for loop practise
# write a program to display sum of odd numbers and even
# numbers that fall b/w 12 and 37(including both number)
"""
# ---> while loop
# while loop is used when we do not know the number of times the loop have to run
# to iterate the non iterable elements while loop is used

# --->syntax
# initialisation

# while condition:
#    statement
#    incre or decre

# Eg:1
# To iterate number from 1 to 10
#i=0
#while i<11:
   # print(i)
    #i=i+1   #or  i+=1

# Eg:2
#10,1
i=11
while i>0:
    print(i)
    i-=1























