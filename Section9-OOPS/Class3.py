# Attribute Shadowing

class Chai:
    temperature = "Hot"
    strength = "Strong"

cutting = Chai()

print(cutting.temperature)

cutting.temperature= "Mild"
cutting.cup = "small"
print(cutting.cup)
print("After Changing",cutting.temperature)
print("Look in Class",Chai.temperature)

del cutting.temperature
del cutting.cup
# print(cutting.cup)   # this gives error
print(cutting.temperature)