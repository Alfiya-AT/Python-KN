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



# ------------------26/5/26----------------------------

# dictionary


# count={}
# sentence=input()
# sentence_list=sentence.split()
# print(sentence)
# for char in sentence_list:
#     count[char]=count.get(char,0)+1
# print(count)

# print(True)


# -------------------------29/5/26------------------

# type of arguments 
# => variable len arg 
# 1)positional

# how u will declare varaible len arg 
# def add(*args):
#     print(args)
#     for arg in args:
#         if type(arg) == int:
#             print(arg,end=" ")

# add(23,43,True,"Hello")


# def fun(a,b,*args):
#     print(args)
#     for val in args:
#         if type(val) == int:
#             print(val)

# fun(10,True,"df",23,34.33,45,'34')




# ----------------------------3/6/26-------------

# 2) keyword arg 



# diff bw args n kwargs 

# -> args op is in form of tuple 
# ->kwargs op is in the form of dictionary


# def fun(**kwargs):
#     print(kwargs)
# fun(nums1=[1,2,2,1],nums2=[2,2],a=23)
#

# combination with parameter
# def fun(a,b,**kwargs):
#     print(a,b)
#     print(kwargs)
#
# # this is normal passing where the val is first assign to the extra para define in the function call  then remaing to the kwargs
# fun(34,54)
# fun(nums1=[1,2,2,1],nums2=[2,2],a=23,b=34)

#combination of args+normal para+kwargs

# def fun(*args,a,b,**kwargs):
#     print(args)
#     print(a,b)
#     print(kwargs)
#
# # if args is at 1st then val r consider as part of args
# fun(2,3,4,True,a=12,b=33,x=345,y='sd')


# =>
# (2, 3, 4, True)
# 12 33
# {'x': 345, 'y': 'sd'}



# py is
# functional prog lang
# script
# oops


# imp feature of py 
# returning multiple values 

# def fun(a,b,c):
#     return a,b,c
# print(fun(3,4,2))

# py can return multiple class , obj , n paramrets 






# list comprehension
# [expression for item in iterables if condition ]



# list1=(10,20,30,40)
# for num in list1:
#     print(num**2)

# list2=[num**2 for num in list1]
# print(list2)

# print([num**2 for num in list1])

# print([[0] for letter in "python"])
# =>[[0], [0], [0], [0], [0], [0]]
# print([letter for letter in "python"])


# list=[item for item in range(1,6)]
# print(list)
# print(type(list))
# =><class 'list'>


# tuple comprehension is not there it will give some result through generator class
# tuple=(item for item in range(1,6))
# print(tuple)

# print(type(tuple))
# =><class 'generator'>

# imp*** diff bw list n tuple comprehension
# data type of tuple comprehension is generator y??


# 
# string_list = [x for x in "a34&!fd37" if x.isalpha() ]
# print(string_list)
# 



# -------------------------4/6/26------------------

# def fun(*args):
#     unique_list=list(set(args))
#     unique_list.sort()
#     return unique_list
# s= "3 4 5 6 6"
# l=s.split()
# list1=[int(x) for x in l ]
# print(l)
# print(fun(*list1))


# iterator in py 

# *** how does loop work internally
# => loops use 2 fun called next and iter function n execute the loop till it reach last element once it reach last ele it will through exception
# list1 = [1,2,3,4]
# # for i in list1:
# #     print(i)



# # this is used to inisalize a
# ele = iter(list1)
# print(next(ele))
# print(next(ele))
# print(next(ele))
# print(next(ele))
# # once it reach the last ele it will through StopIteration  exception
# print(next(ele))


# in set the insertion order is not preserved hence when set is called it can return some thing just randomly
# set1 = {12,32,1}
# ele = iter(set1)
# print(next(ele))
# print(next(ele))


# dict1={1:10,2:20,3:30,4:40,5:50}
# ele=iter(dict1)
# k=next(ele)
# print("key",k)
# print("value",dict1[k])


# r=range(5,10)
# print(r)
# ele=iter(r)
# print(next(ele))


# $$print function is created using variable len args

# range is created using generator but it has its own class called range
# generator are predefined class 

# r=range(2)
# print(type(r))
# <class 'range'>



# -----------------------5/6/26---------------------------

# Generator 
#  this are used to create obj in py


# can we create are own iterator function???
# => No it can be use to iterate over obj but we cannot crete bcz it is predefine function 


# +++++++++++++++++++++++++++++++++++++++++++
# Vimp *****                                + 
                                          # +
# how range is able to generates a value    +
# =>using generators                        +
#                                           +
#  Can we create our own generator ??]      +
#=> Yes       using yield                   +
                                          # + 
# +++++++++++++++++++++++++++++++++++++++++++



# Generator 


# def my_range(n):
#     i=0
#     while i<n:
#         yield i
#         i+=1

# res=my_range(4)
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))



# range function use iterator to iterate the ele in it and the result value are build using the generator


# def my_range(n):
#     i=0
#     while i<n:
#         yield i
#         i+=1
#
# res=my_range(4)
# print(next(res))
# print(next(res))
# print(next(res))
#



# def num():
#     return [1,2,3]
#
# res=num()
# r=iter(res)
# print(next(r))

# in for/loop the memory allocation happens at once while in generator the memory allocation happen one by one

# using yield keyword we can be able to generate a val
# def num():
#     yield 1
#     yield 2
#     yield 1
#     yield 2
# res=num()
#
# # whole command will be in our hand
# for i in res:
#     print(i)

# def days():
#
#     l1=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
#     i=0
#     while True:
#         yield l1[i]
#         i=(i+1)%7
#
# res=days()
# for i in res:
#     print(next(res))


# def month():
#     year = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','sep','Oct','Nov','Dec']
#     i=0
#     quater_list=[]
#     for i in range(0,len(year),3):
#         quater_list.append(list(year[i:i+3]))
#     print(quater_list)
#     while True:
#         yield year[i]
#         i=(i+1)%(len(year))
#         i+=1


# def mon():
#     year ={'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','sep','Oct','Nov','Dec'}
#     i=0
    # quater_list=[]
    # for i in range(0,len(year),3):
    #     quater_list.append(list(year[i:i+3]))

    # print(quater_list)
    # while True:
    #     for month in year:
    #         yield month


        # yield year[i]
        # i=(i+1)%(len(year))
        # i+=1


# result=mon()
# print(next(result))



# types of varaible
# local/global var
# b=25.6
# def fun():
#     a = 10
#     # global b
#     # b=b+1
#     print("This is a local var",a)
#     print("This is a global var", b)
# fun()
# print("This is a global modified b var",b)

# a is local var n b is global
# a can be access in side only the function 
# b can be access from anywhere 





# ---------------------------8/6/26-------------------------------

# local/global var
# this is stored in heap of RAM
# b=25.6

# this block of code is stored in temp in stack of RAM once the function block end the memory get deallocated
# def fun():
#     # this is stored in stack of RAM
#     a = 10
#     # it is actually creating one more obj as b in the code block as b
#     b=1
#     print("This is a local var",a)
#     print("This is a global var inside the code block", b)
#
# fun()
# print("This is a global var b outside the code block ",b)
#

# can we able access the modified  global var outside the code block => no

#  to change the global var we use keyword
# =>global





# b = 25locak 
#
# def fun():
#     global b
#     # to modify the value of the global var  in side a block of code / local
#     # this is stored in stack of RAM
#     a = 10
#     # this is stored in heap of RAM
#     b = 1
#     print("This is a local var", a)
#     print("This is a modified global var inside the code block", b)
#
# fun()
# print("This is a global var b outside the code block but got modify due to global keyword used inside the code block ", b)



# to check how many local n global var r there in code
# =>locals() ,  globals()

# ***imp
#
# a,b,c=23.4,True,"Alfiya"
# def fun():
#     a, b, c = 2,3,1
#     print("locals",locals())
#     print("locals", globals())
#
#
# fun()



# Recursion => fun call it self


# def fun(n):
#     if n>0:
#         print(n) #base condition  this are mandatory
#         # 5 4 3 2 1
#         fun(n-1)
#         # print(n)
# # recursive call
# fun(5)





# -- ---------------------------9/6/26--------------------

# Which has higher time complexity: recursion or looping?
# => 
# Time complexity depends on the algorithm, 
# not on whether it uses recursion or loops. 
# A recursive solution and an iterative solution can have the same time complexity.
#  However, recursion usually has additional stack-space overhead, and poorly designed 
# recursive solutions may become slower due to repeated computations.




# example fibo n fact
# import secrets

# # recursion
# def fibo(first,second,n):
#     if n == 5:
#         return
#     else:
#         temp = first + second
#         print(temp)
#         fibo(second,temp,n+1)

# first=0
# second=1
# print(first)
# print(second)
# fibo(first,second,2)
# 0 1 1 2 3 5




# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))





# if u want to send the data  to another then 
# import is used
# Bring code from another module (file/library) into your current program so you can use it.


# file can as be act as module 
# user defined module


# import fileName as allies

# invoking the function 
# kod.function(arguments)

# all class contains variable n method
# ex list class hv pop ,append... methods 

# by default there are some default variable such as 
# __name_:'__main__'  => constructor 

# this is present in all file internally py use it but modules doesnot hv
# print(__name__)




# using generator

# def fibo(n):
#     first=0
#     second=1
#     i=0
#     while i<n:
#         yield first
#         temp=first+second
#         first=second
#         second=temp
#         i+=1


# res=fibo(10)
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))



# flatten nested list 

# def nestedlist(l,res):
#     # res=[]
#     for item in l:
#         if type(item) is list:
#             nestedlist(item,res)

#         # print(item)
#         if type(item) is int:
#             res.append(item)

#     return res

# l=[1,2,3,[4,5,6,[7,8,9,[10,11,12]]]]
# # l=[1,2,3,[4,5,6]]
# res=[]
# print(nestedlist(l,res))



# import calendar
#
# def year():
#     print(calendar.month(2018,1))
#
# year()

# ---------------------12/6/26--------------------------

# function as object

# print(print)

# print(print.)

# ************higher order function *********

# created an obj and assign refference of it 
# view=print
# view("Hello")

# take = input()
# a=take(" enter a value")

# print(input.__name__)
# print(bin.__doc__)
# print(print.__doc__)
# print(input.__doc__)


# ----------------------------15/12/26--------------------

# HOF ***V.V.imp
# Higher Order Function 

# where we can pass the fun as parameter , varaible n  return type or even use to store the 


# Nested function 


# parent
# def outer():
#     # child
#     def inner():
#         print("This is inner function")
#
#     print("This is outer function n calling inner function")
#
#     inner()
#
# outer()



# Q. design a calculator which perform all the arithmetic operation  + -  /  *  square


# def claculator():
# 
#     def add():
#         print("Addition :", num1+num2)
# 
#     def sub():
#         print("Substraction :",num1-num2)
# 
#     def div():
#         print("Division :",num1/num2)
# 
#     def mul():
#         print("Multiplication: ",num1*num2)
# 
#     def square(num):
#         print("Square: ",num**num)
# 
#     operator = input("enter the operator: ")
#     if operator == "+":
#         num1 = int(input("enter the num1: "))
#         num2 = int(input("enter the num2: "))
#         add()
#     elif operator == "^":
#         num = int(input("enter the num1: "))
#         square(num)
#     elif operator == "-":
#         num1 = int(input("enter the num1: "))
#         num2 = int(input("enter the num2: "))
#         sub()
#     elif operator == "*":
#         num1 = int(input("enter the num1: "))
#         num2 = int(input("enter the num2: "))
#         mul()
#     elif operator == "/":
#         num1 = int(input("enter the num1: "))
#         num2 = int(input("enter the num2: "))
#         div()
# claculator()



# ---------------------------16/6/26---------------------------

# FIRST CLASS FUNCTION
# if function is used is as object or used to store then it is called first class function 


# function as  parameter /argument

# function as a parameter

# function  is can act as a parameter to another function, and also we can pass a function as arg at the time of calling
# def whish_meassage():
#     print("this is a parameter function passed inside the fun as f")
#
#
# # in HOF 'f' is for fucntion is accepting  another function as parameter
# def fun(f):
#     f()

# # function as arg
# fun(whish_meassage)


# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def arithmetic(f,x,y):
#     return f(x,y)

# sum=arithmetic(add,1,2)
# sub=arithmetic(subtract,1,2)
# print(sum)
# print(sub)


# returning funtion inside another fucntion


# def outside():
#     def inside():
#         print("inside function ")
#     return inside
# # outer fun is called n the inner fun is assign to by return 
# f=outside()
# # then the inner fun is called n the print is got executed 
# f()

# def inside():
#     print("inside function ")
# def outside():

#     return inside
# # outer fun is called n the inner fun is assign to by return
# f=outside()
# # then the inner fun is called n the print is got executed
# f()

# ========closure function==========
# colsure is nested function , return another function , 
# inner funtion has the capability to access outer function , can access global var

# vimp  ********* 

# def outer():
#     # wish local to outer fun n global to inner fun
#     wish = "Good morning"
#     def inner():
#         print("*"*17)
#         print(wish)
#         print("*" * 17)
#     return inner
# f=outer()
# f()

# the inner fun is able to access the wish only in case of nested function 
# 

# def outer():
#     # wish local to outer fun n global to inner fun
#     wish = "Good morning"
#     def inner():
#         print("*"*17)
#         print(wish)
#         print("*" * 17)
#     return inner
# f=outer()
# f()



# def outer(wish):
#     # wish local to outer fun n global to inner fun
#     # wish = "Good morning"
#     def inner():
#         print("*"*17)
#         print(wish)

        # we can not modify the global variable in this it will through an error 
#         # wish = wish + wish
#         print("*" * 17)
#     return inner
# f=outer("good")
# f()

# to manipulate the global val in function like a keyword call nonlocal
#

# ***imp  what is the diff bw global n non local

# global
# it can be use inside any function
# nonlocal
# it can be used to manipulate the local var val


# count=0
# def cnt():
#     global count
#     count+=1
#     return count
# print(cnt())
# print(count)

#
# def outer():
#     count=0
#     def cnt():
#         nonlocal count
#         count+=1
#         return count
#     return cnt()
# print(outer())



# ------------------------17-8-26-----------------------------
# # arithmetic operation using seprate function
#
#
# def add(num1,num2):
#     return num1+num2
#
#
#
# def multiply(num1,num2):
#     return num1*num2
#
#
# def calculate(f,num1,num2):
#     return f(num1,num2)
#
#
# num1=int(input("num1: "))
# num2=int(input("num2: "))
# print(calculate(add,num1,num2))

# ---------------------
# 2. text formatter

# def upper(s):
#     return s.upper()
#
# def lower(s):
#     return s.lower()
#
# def case(f,s):
#     return f(s)
#
# print(case(upper,"Kodnest"))


# ------------------------------

# def counting():
    # count=0
    # def counter_block():
    #     # global count
    #     nonlocal count
    #     count=count+1
    #     return count
    # counter = counter_block()
    # print(counter)
# counting()



# ----------------------------


# def outer_bonus(bonus):
#     def inner_Salary(salary):
#         return salary + (salary * (bonus/100))
#     return inner_Salary(10000)

# (print(outer_bonus(10000)))



# --------------------------------18/6/26---------------------

# Decorators 

# decorators in py --> closure function, fun as parameter
# Decorators are flexible way to modify or extend behavior of functions or methods, without changing their actual code.

# def decorator(f):
#     def inner():
#         print("+"*15)
#         f()
#         print("+"*15)
#
#     return inner
# @decorator
# def display():
#     print("Hello Welcome!!!")
#
# display()



#  imp *** Lambda function

# k=lambda x:x**2 
# print(k(3))


# ---------------------19/6/26------------------------

# build in HOF
# lambda

# # l1=[1,2,3,4,5]
# l2=lambda x:x*x 
# print(l2(3))

# print((lambda x:x*x )(7))


# filter

# l1=[1,2,3,4,5,6,7,8,9]
# item=filter(lambda x:x%3==0,l1)
# print(list(item))

# square=lambda x:x*x
# print(square(5))

# even = list(filter(lambda  x: x%2==0 ,l1))
# print(even)


# ----------------25/6/26---------------------

# l1=[1,2,3,4]
# l2=list(map(lambda x:-x,l1))
# print(l2)

# l1=[1,2,3,4,5,6,7,8,9]
# l=lambda x: x if x%2==0 else -x
# l2=list(map(l,l1))
# print(l2)

# l3=list(map(lambda x: x**2,(filter(lambda x:x%2==0,l1))))
# print(l3)



# Error in python

# 1.Synatx Error
# 2.Logical Error
# 3.Runtime Error

# 1.Syntax

# b=input('synatx error)

# 2.Logical Error
# a=int(input("enter a no: "))
# b=int(input("enter another no: "))
# if a>b:
#     print(a)
# else:
#     print(a)


# # 3.Runtime Error

# a=10
# b=0
# print(a/b)