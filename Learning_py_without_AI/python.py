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


# -------------------------27-3-26----------------------

# num1=int(input('num1: '))
# num2=int(input('num2: '))

# if num1>num2:
#     print("num1 is greater number")
# elif num1<num2:
#     print("num2 is greater than num1")
# else:
#     print("num1 is equal to num2")


# if num1>=1 and num1<=100:
#     print("True")
# else:
#     print("False")

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
# my_str='Pizza'
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
# used to check the char is present in other str or not
# print('izz' in my_str)



# ---------------------------22/4/26----------------------

# functions
# print(len('alfiya at'))
# len function include the num of cha r including the space 


# print("Hi">"Bye")
# print("hi">"Bye")
# print("Hi">"bye")


# it depends on ascii val A=65 a=97
# print("A">"a")  
# print("a">"A")
# print("a">"a")


# unicode 
# all the char for all lang r hv some code 

# s = "अल्फिया"
# for ch in s:
#     print(ch, hex(ord(ch)))

# ASCII
# only certain char r hv some standard val 



# ---------------------------------23/4/26----------------------

# s1='alfiya'
# print(s1.find('g'))
# if not found it will return -1

# print(s1.index('g'))
# this will return error

# s1='Tamboli'
# print(id(s1))
# shadow problem 
# s2='Tamboli'
# print(id(s2))



# -------------------------24/4/26--------------
# *** imp IV
# str_t=(6)
# tuple_t=(3,)
# print(type(str_t))   => int 
# print(type(tuple_t))  => tuple



# -------------------------27/4/26-------------------
# replace will just replace value n create new str but does not modify the orignal str

# orignal="py is difficult"
# string=orignal.replace("difficult","easy")
# print(orignal)
# print(string)

# # location of var 
# print(id(orignal))
# print(id(string))

# rfind()  from right
# print(orignal.rfind('f'))

# print(orignal.split("-"))

# tup=("A","B","c")

# tup=str([1,2,3])
# print("".join(tup))

# print(type(tup))
# print(".".join(tup))
# print(tup)

# str1="python"
# str2="12345"
# str3=str1.join(str2)
# str3="-".join(str2)
# print(str3)
# in str it access each char wrt to index
# =>1-2-3-4-5



# ---------------------------------28/4/26---------------------

# tup=("a","l","2")
# print("-".join(tup))



# -------------------------
# eval is readablebuffer  
# numb=eval(input("operation"))    #valid expression 
# print(numb)
# 3+5=>8

# generator  :  

# l=[2,4,5]

# print(l)
# print(l+l)
# print(l*3)
# print(4 in l)
# print(l[:7])


# mutable methods of list class
# add at end
# l.append(8)
# print(l)
# # copy
# c=l.copy()
# print(c)
# # clear
# l.clear()
# print(l)
# # insert specific sequence index
# l.insert(1,c)
# # extend
# l.extend(((4, 5),7))
# l.extend({4, 5})

# # VIMP IMP  ***** 
# l.extend("abcd")
# print(l)
# # [[2, 4, 5, 8], (4, 5), 7, 4, 5, 'a', 'b', 'c', 'd']
# # iteratives 
# # iterables An iterable is any object you can loop over (iterate through)
# # doing same task again n again 
# # concat
# l=l+[104,9,4,8]
# print(l)

# l.pop()
# print(l)
# # [[2, 4, 5, 8], (4, 5), 7, 4, 5, 'a', 'b', 'c', 'd', 104]


# # remove first occurance only 
# l.remove(4)
# print(l)


# # its case sensitive 
# l.extend(['Kodnest','kodnest'])
# l.remove('kodnest')
# print(l)



# ------------------------------------7/5/26-----------------------

# l=[2,4,5]

# ____pop by index____
# print(l)
# l.pop()  # Remove last element 
# print(l)

# _____ordering the elements in the list_____
#1. sort() method => it will sort the list in ascending order by default

# l1=["cherry","banana","apple"] 
# => ['apple', 'banana', 'cherry']

# l1=[20,40,'Python',10,True]  
# => error as we can not compare '<' int with str 

# l1.sort()  
# print(l1)

#2 reverse() method => it will reverse the list

# l2=[20,40,'Python',10,True]

# method
# l2.reverse()
# print(l2)

# function
# reversed(l2)
# print(l2)

# ____tuple____
# tup=(1,2,3,"kodnest",39)
# print(tup[0])

# tup=("kodnest")
# print(type(tup))

# l=[1]
# print(type(l))


# ------------------------8/5/26-----------------------

# t=10,
# print(type(t))

# a=23
# b=5
# c=65
# d=44

# tuple packing
# t1=(a,b,c,d)
# print(t1)

# tuple unpacking
# a,b,c,d=t1
# print(a)
# print(b)
# print(c)
# print(d)



# Q.wrt prg to take ip  from user as tuple of numbers n print its sum n avg


# tuple1=eval(input("Enter a tuple of numbers: "))
# total_length=len(tuple1)
# print("Tuple of numbers:", tuple1)

# # total_sum=sum(tuple1)
# # print("Sum:", total_sum)

# # or 

# totalSum=0
# for i in tuple1:
#     totalSum+=i
# print("Sum:", totalSum)

# average=totalSum/total_length
# print("Average:", average)


# l=[3,3,6,1,2]
# print(set(l))


# if user input is 3,4,5 then use eval
# number_list=eval((input("Enter a list of numbers: ")))
# l=(list(number_list))
# n=len(l)
# sum_list=sum(l)
# print(sum_list)

# if user input is 3 4 5 then use eval
# number_list=input("Enter a list of numbers: ").split()
# print(number_list)

# n=len(number_list)
# # sum_list=sum(int(num) for num in number_list)    O(n)
# print(sum_list/n)


# numbers=input("Enter the val")
# print(numbers)
# numbers_list=numbers.split()
# print(numbers_list)
# int_list=[]
# for num in numbers_list:
#     int_list.append(int(num))

# print(int_list[::-1])

# --------------------------18/5/26--------------

# set1={10,20,30,40,50}
# print(set1)
# print(type(set1))


# this is a dict
# set2={}
# print(set2)
# print(type(set2))

# ---------------create empty set-------------------
#creating empty set
# set2=set()
# print(set2)
# print(type(set2))

# --------converting from datatype to set -----------
# converting list to set
# lst=[22,45,22,13,29]
# set3=set(lst)
# print(set3)
# =>{13, 29, 45, 22}

# ------------creating------
# : neither random nor perfectly sorted — it's hash-ordered 4 memory
# set4=set(range(1,11))
# print(set4)


# ***diff bw update n add
# ------------add---------
# set operations
# add used to add single element
# # set4.add(True)

# ----------update------
# to add multiple value
# set4={10,20,30,40}
# list4=[50,60,70,10]
# set4.update(list4,range(5))
# print(set4)
# =>{0, 1, 2, 3, 4, 70, 40, 10, 50, 20, 60, 30}


# ----------copy-------
# set5={40,89,True,20.34}
# set6=set5.copy()
# print(set6)
# =>{40, 89, 20.34, True}



# ***diff bw pop , remove,  discard
# ----------pop---------
# set7={40, 30, 50, 30}
# print(set7)
# # remove the random element
# set7.pop()
# print(set7)

# ---------remove---------
# set7={40, 30, 50, 30}
# set7.remove(30)
# print(set7)
# => {40, 50}


# set7.remove(100)
# print(set7)
# KeyError error if element is not present in set

# ---------------discard--------------

# it  will not throw any error if the element is not present
# it ele is not present then it will not perform any type of operation
# set7={40, 30, 50, 30}
# set7.discard(100)
# print(set7)

# ----------------clear----------------

# set7.clear()
# print(set7)

# math operation on set

# 1.Union
# set1={10,20,30,40,50}
# set2={60,70,30,40,50}
# set3=set1.union(set2)
# print(set3)
# 
# # 2.intersection
# set4=set1.intersection(set2)
# print(set4)



# ---------------------25/5/26-------------------------

# set1={10,20,30,40}
# set2={30,40,50,60}

# print(set1.difference(set2))
# print(set1-set2)


