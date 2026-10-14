# Method Resolution Order

class A:
    label = "A: Base Class"

class B(A):
    label = "B: Masala Class"

class C(A):
    label = "C: Herbel Class"

class D(B,C):
    pass

cup = D() 
print(cup.label) # B: Masala Class
print(D.__mro__)