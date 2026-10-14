# Set Comprehensions

favourites_chai= [
    "Masala Chai",
    "Green Tea",
    "Masala Chai",
    "Lemon Tea",
    "Green Tea",
    "Elaichi Chai"
]

unique_chai1 = {chai for chai in favourites_chai}

unique_chai2 = {chai for chai in favourites_chai if len(chai)>9}

print(unique_chai1)

print(unique_chai2)

recipes = {
    "Masala Chai" : ["Ginger","Cardamom","Clove"],
    "Elaichi Chai" : ["Cardamom","milk"],
    "Spicy Chai" : ["Ginger","Black Pepper","Clove"]
}

unique_chai3 = {spice for ingridients in recipes.values() for spice in ingridients}

print(unique_chai3)