# NAMESPACE

class Chai:
    origin = "India"

print(f"Class: {Chai.origin}")

Chai.is_hot = True

print(f"Class: {Chai.is_hot}")

# Creating object from class chai

masala = Chai()

print(f"Masala : {masala.origin}")
print(f"Masala : {masala.is_hot}")

masala.is_hot = False
print(f"Class: {Chai.is_hot}")
print(f"Masala : {masala.is_hot}")

masala.flavor = "Masla"
print(masala.flavor) # but not exist in class