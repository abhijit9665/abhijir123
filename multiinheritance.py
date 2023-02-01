# class Mother:
#     def __init__(self):
#         self.name = "Mother"

# class Father:
#     def __init__(self):
#         self.name = "Father"

# class Child(Mother, Father):
#     def __init__(self):
#         super().__init__()
#         self.age = 10


# s = Child()
# print(s.name)
# print()
# print(s.age)

# Python Program to depict multiple inheritance
# when method is overridden in both classes

class Class1:
	def m(self):
		print("In Class1")
	
class Class2(Class1):
	def m(self):
		print("In Class2")

class Class3(Class1):
	def m(self):
		print("In Class3")
		
class Class4(Class2, Class3):
	pass
	
obj = Class4()
Class3.m(obj)
Class1.m(obj)
