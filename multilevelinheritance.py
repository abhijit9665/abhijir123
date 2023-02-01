class GrandParent:
    def __init__(self):
        self.name = "GrandParent"

class Parent(GrandParent):
    def b(self):
        super().__init__()
        self.age = 30

class Child(Parent):
    def ab(self):
        super().__init__()
        self.gender = "male"

s = Child()
print(s.name)