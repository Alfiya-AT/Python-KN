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

status=input("do u have membership?(yes/no): ").lower().strip()
if status=="yes":
    print("you can access")
else:
    print("you can not access")
