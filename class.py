# class student():
#     def __init__(self):
#         self.name = 'duga'
#         self.age = 40
#         self.marks = 70
        
# s = student()
# print(s.name)
# print(s.age)
# print(s.marks)
 
        
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name}  and {self.age}"
# p1 = Person("John", 36)
# print(p1)

class ab():
    def __init__(self):
        self.a=20
    def abc(self):
        self.b = 30
        
p1=ab()
p1.abc()
p1.d = 40
print(p1.__dict__)
