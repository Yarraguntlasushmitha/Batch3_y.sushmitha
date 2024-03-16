'''
Assigment
# 1)
s1= "how are you"
fst=s1[0].upper()
lst=s1[-1].upper()
print(fst+s1[1:len(s1)-1]+lst)

# 2)
n=128
temp=n
f1=0
while n!=0:
    rem=n%10
    check=temp%rem
    if check!=0:
        f1=1
    n=n//10
if f1==0:
    print("yes")
else:
    print("no")

# 3)
l1=[1,2,3,4]
l2=[5,6,7,8]
sum=[]
for i in range(len(l1)):
     sum.append(l1[i]+l2[i])
print(sum)
    [OR]
l1=[1,2,3,4]
l2=[5,6,7,8]
l3=[]
for i in range(len(l1)):
    ans=l1[i]+l2[i]
    l3.append(ans)
print(l3)

# ----> Set
# characteristics of set
    1) set can be created using{}
    2) The elements inside set are not indexe
    3) Does not allow duplicate values
    4) It unordered
    5) Heterogenous ---> acceot only unmutable datatypes
    6) Mutable or changable

# Eg:1
s1={9,9,89,7.76,8+7j,(8,7,5),"truck",'e'}
print(s1)

# Eg:2
s2={5,8,98,[9,0]}
print(s2) --->error

# max(),min(),len()

# Eg
    To add element inside set

s1={8,78,67,'u'}
#add()
#s1.add(43)
#print(s1)

#updata()
s1.update([9,0])
print(s1)

# To delete element inside set
s1={8,78,67,'u'}
#pop()# To delete one element randonly

#remove()
s1.remove(78)
print(s1)

# Discard()
s1.discard(67)
print(s1)

# clear()
l1={}
print(type(l1)) #---> datatype is dict

s1=set() # To create empty set
print(type(s1))

s1={8,78,67,'u'}
s1.clear()
print(s1)

del s1
print(s1)

# --> join the sets
s1={9,0,8}
s2={9.90,"card",'t',56}

#union() --> To combine 2 sets
s3=s1.union(s2)
print(s3)

# --> Intersection() --> To get common elements inside set
s1={4,5,6}
s2={5,6,7,8}
print(s1.intersection(s2))

# Difference()
s1={4,5,6}
s2={5,6,7,8}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))

#isdisjoint(),issubset(),issuperset()
s1={4,5,6}
s2={4,5,6,7,8}
print(s1.issubset(s2))
print(s2.issuperset(s1))
print(s1.isdisjoint(s2))

# promble :1
# n1={1,2,3} -->s1
for val in s1:
    if val in s2:
        str1="its joint set"
print(str1)

# -----> Dictionary
# EG:1
d1={1:100,'a':200,4.5:"hello"}
print(d1)
print(len(d1))

mech_name=["name1","name2","name3"]
mech_age=[23,22,24]
mech_mark=[89,78,60]
mech_email=["name2@gmail.com","name3@gmail.com"]

# char of dictionary
     1) Have to be surrounded by {}
     2) It have to be in the from of key, value pair
     3) It is mutable
     4) It is unindexed
     5) It is ordered
     6) Duplicate keys are not allowed,duplicate values are allowed
     7) key does not allow mutable datatypes,values allow mutable datatype

d1={1:100,2:200,3:300,4:400}
# To access elements in dictionary
print(d1)
#Or
#To access the values,have to use key
print(d1[1]) #o/p--->100

# some common functions
# len(),min(),max()
print(min(d1))
print(max(d1))

# To find min,max based on values
print(min(d1.values()))
print(max(d1.values()))

# Dictionary based functions
# To add element(key and value pair)in dict
d1={1:100,2:200,3:300,4:400}
d1[5]=500
print(d1)

# To replace a value in dictionary
d1={1:100,2:200,3:300,4:400}
d1[2]="mango"
print(d1)

# Delete element from dictionary
d1={1:100,2:200,3:300,4:400}
#popitem() # ---> To delete last key value pair in dict
print(d1.popitem())

d1={1:100,2:200,3:300,4:400}
d1.popitem()
print(d1)

# pop()
d1.pop(2) # 2 is the key in dictionary
print(d1)

# clear(),del
# join 2 disctionary
# update()
d1={1:100,2:200,3:300,4:400}
d2={"a":"apple","b":"boy","g":"game"}
d1.update(d2)
print(d1)

# Get() ---> used to get the value from a key
d1={1:100,2:200,3:300,4:400}
#print(d1[90])
print(d1.get(90))

# To print all the keys
print(d1.keys())
print(type(d1.keys()))

# print all the values
print(d1.values())

# Iterating dictionary
d1={1:100,2:200,3:300,4:400}
for val in d1:
    print(val)
for val in d1.values(): # To iterate values alone
    print(val)

# To get both key and values
for key,val in d1.items():
    print(key,val)

# promble:1
# n=input()
n=int(input("enter num of times : "))
integer=[]
float_value=[]
string=[]
for val in range(n):
    value=eval(input("enter the values: "))
    if type(value)==int:
       integer.append(value)
    elif type(value)==float:
        float_value.append(value)
    elif type(value)==str:
        string.append(value)
    else:
        print("pls provide data in int,float,string")
print(integer)
print(float_value)
print(string)

# problem:2
s3=set()
s1={10,20,30,40,50}
s2={30,40,50,60,70}
for val in s1:
    if val not in s2:
        s3.add(val)
for val in s2:
    if val not in s1:
        s3.add(val)
print(s3)       
'''
# 1) swap elements in string list
# The original list is:['Gfg', 'is', 'best', 'for', 'Geeks']
# List after performing character swaps :['Gfg', 'is', 'best', 'for', 'Geeks']








# ----> problem :3
l1=[1,2,3,4] # key
l2=["a","b","c","d"] # value
d1={}
for val in range(len(l1)):
    d1[l1[val]]=l2[val]
print(d1)











            








