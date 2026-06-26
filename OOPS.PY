# ***************** 1) Inheritance in Python**********************


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         print("Animal name:", self.name)

# class Dog(Animal):
#     def sound(self):
#         print(self.name, "barks")

# d = Dog("Buddy")
# # Inherited method
# d.info()     
# d.sound()



# ***************** super() MRO(Method Resolution Order )*********************
# Parent Class: Animal
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         print("Animal name:", self.name)

# # Child Class: Dog
# class Dog(Animal):
#     def __init__(self, name, breed):
#         # Calls constructor based on MRO
#         super().__init__(name)  
#         self.breed = breed

#     def details(self):
#         print(self.name, "is a", self.breed)

# d = Dog("Buddy", "Golden Retriever")
# d.info()      # Parent method
# d.details()   # Child method


# ****************************Method Overriding in Inheritance*************

# class Animal:
#     def sound(self):
#         print("Animal sound")

# class Dog(Animal):
#     def sound(self):
#         print("Bark")

# d = Dog()
# d.sound()










# *****************  2) Polymorphism  ***************
# ->Compile-time Polymorphism
# ->Run -time Polymorphism


# ********************1. Compile-time Polymorphism******************

# class Calculator:
#     def multiply(self, a=1, b=1, *args):
#         result = a * b
#         for num in args:
#             result *= num
#         return result

# # Create object
# calc = Calculator()

# # Using default arguments
# print(calc.multiply())            
# print(calc.multiply(4))           

# # Using multiple arguments
# print(calc.multiply(2, 3))       
# print(calc.multiply(2, 3, 4))


#********************** 2. Runtime Polymorphism (Overriding)*************************
# #class Animal:
#     def sound(self):
#         return "Some generic sound"

# class Dog(Animal):
#     def sound(self):
#         return "Bark"

# class Cat(Animal):
#     def sound(self):
#         return "Meow"

# # Polymorphic behavior
# animals = [Dog(), Cat(), Animal()]
# for animal in animals:
#     print(animal.sound())


# ************************** Polymorphism in Built-in Functions***************************

# print(len("Hello"))  # String length
# print(len([1, 2, 3]))  # List length

# print(max(1, 3, 2))  # Maximum of integers
# print(max("a", "z", "m"))  # Maximum in strings



# ****************************Polymorphism in Functions****************

# class Pen:
#     def use(self):
#         return "Writing"

# class Eraser:
#     def use(self):
#         return "Erasing"

# def perform_task(tool):
#     print(tool.use())

# perform_task(Pen())
# perform_task(Eraser())


# *************************Polymorphism in Operators**************

# print(5 + 10)  # Integer addition
# print("Hello " + "World!")  # String concatenation
# print([1, 2] + [3, 4])  # List concatenation







# *************************3. Encapsulation******************

