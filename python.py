# print("Hello\bWorld!")
# print("\"Hello\"")
# print("'Hello'")
# print("Hello\rWorld!")

# --------------------------- 9/3/2026 ---------------------------
# name="ALfiya"
# roll=12
# cgpa=9.1
# stream="Computer Science"
# print("name:",name)
# print("roll:",roll)
# print("cgpa:",cgpa)
# print("stream:",stream)
# # this method fromat belong to string class the roll is invoke and inject the value in place holder
# print("Format method {}".format(roll))
# # print using f string
# print(f"f string method {roll}")

# ---------------------------10/3/2026---------------------------

# print(True>True)
# print(10> True)
# print(1+True)

# print(10<20<30)  to make  readabily better we use logical operator
# print(10<20 and False<30)
# a=1001
# b=0000
# print(~a)

# ----------------------------11/3/2026----------------------------------


# And
# X=>T op=>Y
# Y=>F op=>X

# Or 
# X=>F op=>X
# Y=>T op=>Y

# print(10 and 20)
# print(20 and 10)
# print(0 and 20)
# print(20 and 0)
# print(' ' and 0)
# print('A' and ' T')
# print( 0 and 'A')

# print(10 or 30)
# print(0 or 20)
# print(20 or 0)
# print(" " or 40)


# type casting
# num=10
# print(type(num))
# num=float(num)
# print(type(num))

# a=10.3
# b=34.0
# num=int(a*b)
# print(type(num))

# print(True+10)

# X=10
# Y=True
# print(X+Y)=> 11

# upper case notations are use for definig constants
# PI=3.14

# name=int('error')
# print(name)


# -----------------------------16/3/26------------------
# number1=float("12")
# number2=float("34")
# print(number1/number2)

# print(~12)
# print(~(-13))

# binary rep
# print((12&13))

# --------------------------17/3/26--------------------------
# how to convert binary to decimal 
# res=int("1101",2)
# print(res)

# # how to convert dec to binnary 
# resb=bin(12)
# print(resb)

# print(bin(45^60))
# print(bin(45))
# print(bin(60))

# print(10>>2)



# --------------------- 18/3/26 -----------------------
# functions vv.imp 
# def greeting():
#     a="hello"
#     # return a
#     print(a)
# # print(greting())
# greeting()


# ----------------------23/3/26---------------------
# need_transport=bool(input("Need"))
# print(int(need_transport))


# ----------------------30-3-26---------------------------
# ***imp interview Q
# def func(num):        the calling fun call this execution fun and execute the remaining statements 
#     statements        
# num=int(input())      due to default nature of execution of interpreter this will get execute 1st
# func(num)             2nd execution line  this is calling fun


# ----------------------31-3-26-------------------------------

# m=range(20)
# print(m)
# =>range(0,20)

# for num  in m:
    # print(num)

# -------------------1-4-26----------------------------------
# .lower() mathod

# status=input("do u have membership?(yes/no): ").lower().strip()
# if status=="yes":
#     print("you can access")
# else:
#     print("you can not access")

# -------------------1-4-26----------------------------------
# .upper() mathod

# status=input("do u have membership?(yes/no): ").upper().strip()
# if status=="YES":
#     print("you can access")
# else:
#     print("you can not access")

# -------------------2-4-26----------------------------------
# Augmented assignment operator


# sum of first n natural numbers
# def sum_recursive(n):
#     if n == 0:          # base case — stop here!
#         return 0
#     return n + sum_recursive(n - 1)  # recursive call

# sum_recursive(3) calls:
# 3 + sum_recursive(2)
# 3 + 2 + sum_recursive(1)
# 3 + 2 + 1 + sum_recursive(0) → 0/


# ----------------------
# def sum_builtin(n):
#     return sum(range(1, n + 1))

# range(1, n+1) generates: 1, 2, 3, ..., n
# sum() adds them all up
# Python does it internally — very fast in practice

# from functools import reduce
# import operator
# ----------------------
# def sum_reduce(n):
#     return reduce(operator.add, range(1, n + 1))

# reduce applies add repeatedly:
# add(add(add(1, 2), 3), 4) → 10


# ----------------------------7/4/26-------------------------------------
# fibonacci  n simultanious assignment operator
# a,b=0,1
# print(f"{a}\n{b}")
# N=4
# if N<=0:
#     print("enter +ve no")
# elif N==1:
#     print("0")
# else:

#     for i in range(2,N):
#         a,b=b,a+b
#         print(b)


# --------------------------8/4/26---------------------------------------

# break statement => it is useed in looping statements if use it some where else it will show syntax error 
# -----------------***imp IV
# num=10
# if num>40:
#     print("statement1")
#     break
# print("hello")


# continue 

# for i in range(10):
#     if i%2==0:
#         continue
#     print(i)


# pass

# if True:
#     pass
# print("false")


# -------------9/4/26--------------------

# List  =>Hetrogenies, duplicate, mutable n order is preserved 
# mylist=[1,1.4,'Alfiya',True]
# mylist.append("Kodnest")    #method
# print(len(mylist))          #function



# # Tuple =>*immutable
# mylist=(1,1.4,'Alfiya',True)
# print(mylist)   



# -------------------------------10/4/26----------------------------------
# reverse a num
# num=244
# res=0
# while num>0:
#     rem=num%10
#     num=num//10
#     res=(res*10)+(rem)
# print(res)

# product of all even num
# num=4
# i=1
# res=0
# print(res)
# while i<=num:
#     print(res)
#     if i%2==0:
#         res+=i
#         print(res)
#     # else:
#     #     continue
#     i+=1
#     print(res)
# print(res)

#------------------------------13/4/26------------------------------

# does the py fun support multiple return val=> yes  only in py

# def fun_name(a,b):
#     sum=a+b
#     diff=a-b
#     return sum,diff

# s,d=fun_name(2,3)
# print(f"Sum:{s}\nDiff:{d}")

# # it will return the res in the form of tuple if the res is stored in  single var

# @ time of calling the fun the diff data type r passed hence its called dynamic  
# res=fun_name(2.3,3.8)
# print(res)


# Types of arg
# 1) positional arg
# def cal(a,b):
#     print(a+b)
# cal(32,53)

# 2) keyword arg
# def wish(name,msg):
#     print("hello",name,msg)

# wish(msg="Gm",name="Alfiya")

# wish("Alfiya",msg="Gm" )

#**this will through error as the KWA is 1st so it hope for var for next val
# wish(msg="Gm","Alfiya")  



# ----------------------------16/4/26-----------------------------
#3) Default parameter 
# def default(name="Alfiya",usn=12):
#     print(f"Hiii {name} {usn}")

# default()

# default("A",3)  
# default(usn=2,name="AAT")
# it give more preriority to the positional or the keyword n it overide 


# String in py
# indexing n slicing 
# used for file handling 



# my_str="Alfiya"

# print(my_str[1:4])
# print(my_str[::]) => [0:0:1]
# print(my_str[::-1])=> reverse from [n:0:-1]


# --------------------------------17/4/26---------------------------------
my_str='Pizza'
# no error 
# print(my_str[16:])   

# => string index out of range
# print(my_str[33])   

# Concatenation 
# print('a'+'b')
# print('a'*4)

# inbuild Functions

# print(len(my_str))

# membership operator => IN, NOT IN 

# print('izz' in my_str)
