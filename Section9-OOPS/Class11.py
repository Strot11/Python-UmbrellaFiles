# Property Decorator Getter and Setter
class TeaLeaf:
    def __init__(self,age):
        self._age = age

    @property
    def age(self):
        return self._age + 2

    @age.setter
    def age(self,age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age

leaf = TeaLeaf(5)
print(leaf.age)
leaf.age = 1
print(leaf.age)
