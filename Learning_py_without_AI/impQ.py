# ***imp  what is the diff bw global n non local

# 
# vimp  *********
# colsure is nested function , return another function , 
# inner funtion has the capability to access outer function , can access global var

# print(type([]))
# # =><class 'list'>

# print(type(()))
# => <class 'tuple'>

# a=(3)
# print(type(a))
# <class 'int'>


# a=(2,)
# print(type(a))
# <class 'tuple'>


# print(type({}))
# # <class 'dict'>


# print(type(set()))
# <class 'dict'>

# Python map() function

# s = ['1', '2', '3', '4']
# res = map(int, s)
# print(list(res))

def f(x=[]):
    x.append(1)
    return x
print(f(), f())

