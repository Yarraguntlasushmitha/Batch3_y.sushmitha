# ---> while loop
# ---> break using while loop
# Eg:1
# 1) iterate from 20 to 30 and break the loop in 27
'''
i=20
while i<31:
    if i==27:
        break
    print(i)
    i+=1
# 2)    
i=20
while i<31:
    print(i)  
    if i==27:
        break
    i+=1  
# 3)
i=20
while i<31:
    if i==27:
        print(i)
        break
    i+=1
 '''   
# -----> continue
"""
1)
i=20
while i<31:
    if i==27:
        continue
    print(i)
    i+=1
2)
i=20
while i<31:
    i+=1
    if i==27:
        continue
    print(i)
"""   

# while to iterate from 12 to 22
# find the sum of all number
'''
i=12
sum=0
while i<23:
     sum=sum+i
     i+=1
print(sum)
'''
# Eg:6
# find the average of value form 20 to 25
'''
i=20
sum=0
while i<25:
     sum=sum+i
     i+=1
     avg=sum/6
print(avg)

# 2)
i=20
sum=0
count=0
while i<=30:
    sum=sum+i
    count+=1
    i+=1
print(sum/count)
''' 
# ---> Nested for loop
# Eg:1
'''
for i in range(1,3+1):
     for j in range(1,4+1):
         print(i,j)
for row in range(1,3+1):
     for col in range(1,4+1):
         print(row,col)
'''
# Eg:2
# * * * *
# * * * *
# * * * *
# * * * *
'''
for row in range(4):
     for col in range(4):
         print(col,end=" ")
     print()

# EG:3
rows=int(input("enter the rows: "))
cols=int(input("enter the cols: "))
for row in range(rows):
     for col in range(cols):
         print("*",end=" ")
     print()

sum=0
for row in range(4):
     for col in range(4):
         sum=sum+1
         print(sum,end=" ")
     print()

# To print stars in right angled triangle

for row in range(0,6):
     for col in range(0,row+1):
         print("*",end=" ")
     print() 


for row in range(0,6):
     for col in range(row,6):
         print("*",end=" ")
     print() 

for row in range(6,0,-1):
     for col in range(0,row):
         print("*",end=" ")
     print()    

for row in range(6,col):
     for col in range(row,6):
         print("*",end=" ")
     print()    

for row in range(6):
     for col in range(6):
          if col==0 or col==6-1 or row==0 or row==6-1:
              print("*",end=" ")
          else:
               print(" ",end=" ")
     print()    
    
for row in range(0,5):
     for col in range(0,6):
          if ((row==0 and col==3) or (row==1 and (col>=2 and col<=4) or (row==2 and (col>=1 and col<=5)))):
              print("*",end=" ")
          else:
               print(" ",end=" ")
     print()    
'''   
# ----> Datatypes
# primary
# Number ---> int,float complex
# String
# Boolean
# None

# ---- Collection
# List
# Tuple
# Set
# Dictionary

# ---> List
# If the collection of element are sorounded by the square brackets, it is considered to be list
# Eg:1
# lst1=[4,5,6,7,8,99,"hello",7+9j,[8,9,0]]

# ---> Characteristics of list
#        1) list have to be sorrounded by []
#        2) It is mutable (the elements in the list are changable)
#        3) Evey element inside llist is indexed
#        4) The elements inside list will be ordered format
#        5) It can hold duplicate values
#        6) Its heterogenous
# To access the elements in list
# l1=[1,4,1,7,89.7,7[5,"p","i"]
# print(l1)

# --> Indexing
# In the collection datatypes like list, tuple,string,the elements will be alloted
# with predefined unique value called index value

# We have 2 types of Indexing
# positive indexing ----> starts with 0 from left hand side
# Negative Indexing ---> starts with -1 from right hand side
'''
# Positive indexing
print(lst1[0])
print(lst1[4])
print(lst1[20]) # ---->error
# ----> Negative Indexing
lst1=[4,5,6,7,8,99,"hello",7+9j,[8,9,0]]
print(lst1[-1])
print(lst1[-4])

# -----> Slicing
lst1=[4,5,6,7,8,99,"hello",7+9j,[8,9,0]]
#lst1[start_index:end_index:step]
#print(lst1[0:4])
print(lst1[5:8])
print(lst1[:5])
print(lst1[3:])
print([:])
print(lst1[0:7:1]) # ---> lst1[0:7]--> both are same
print(lst1[0:7:2])

# --> Trail=int(input())
l1=[1,4,1,7,89.7,7.5,"p","i"]
print(l1[-4-1])
print(l1[-1:-4])
print(l1[-7:-1:2])
'''
# To insert of add element inside list
# append()
l1=[9,8,0,6]
l1.append("car")
print(l1)







































     








