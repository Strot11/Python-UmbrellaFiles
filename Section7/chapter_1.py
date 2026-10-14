# List Comprehension

menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Iced Peach Tea",
    "Ginger Chai",
    "Green Tea"
]

iced_tea = [tea for tea in menu if "Iced" in tea]
extra =  [tea for tea in menu if len(tea)==11]

print(iced_tea)
print(extra)

