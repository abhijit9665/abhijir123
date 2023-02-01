class Parent:
    def __init__(self):
        self.name = "Parent"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.age = 10

s=Child()
print(s.name)