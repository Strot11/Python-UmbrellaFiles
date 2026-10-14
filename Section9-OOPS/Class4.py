# Self argumentss

class Chaicup:
    size = 150 #ml
    def describe(self):
        return f"A {self.size}ml cup chai"

cup = Chaicup()
print(cup.describe())

# print(Chaicup.describe())  # always require object to call self this gives error 

print(Chaicup.describe(cup))  # always need an reference so that it distinct from other variable 

cup2 = Chaicup()
cup2.size = 80
print(Chaicup.describe(cup2))

# Without self: Use @staticmethod to write pure, independent utility functions inside a class.