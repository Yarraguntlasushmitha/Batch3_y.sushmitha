'''
# Assesment
# 1)
d1={'ten':10,'Twenty':20,'thirty':30}
d2={'Thirty':30,'fourty':40,'Fifty':50}
d1.update(d2)
print(d1)

# 2) python program to determine if the given sets are disjoint
# or not without using inbuilt in functions
set1={'python','Java','Data science'}
set2={'ML','AI','R Language','python'}
set3={'Data Analytics','Robotics','Deep Learning'}
c=0
flag=0
for val in range(3):
    c=c+1
    if c==1:
        for val in set1:
            if val in set2 or val in set3:
                flag=1
                break
    if c==2:
        for val in set2:
            if val in set1 or val in set3:
                flag=1
                break
    if c==3:
        for val in set3:
            if val in set2 or set1:
                flag=1
                break
if flag==0:
    print("Disjoint")
else:
    print("joint")

# 3)
l1=["M","na","i","ke"]
l2=["y","me","s","lly"]
# o/p is ['My','name','is','kelly]
l3=[]
for val in range(len(l1)):
    ans=l1[val]+l2[val]
    l3.append(ans)
print(l3)
 # OR
i=0
while i<len(l1):
    l3.append(l1[i]+l2[i])
    i+=1
print(l3)
'''

# Functions
# DEF
# Function is a block of code which is used to perform a specific functionally
# Function can be created using def keyword
# Function has 3 parts
# Function declaration
# Function defanition
# Function call
# Eg:1
def greet(): # function defanition
  print("Greetings User!!")
greet() # function calling
# Eg:2
# function with parameter
def greeting(name):
    print("welcome",name)
for val in range(3):
    username=input("enter the name:")
    greeting(username)













































   











