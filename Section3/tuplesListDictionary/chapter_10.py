chai_order = dict(type="Masala Chai", size="Large", sugar=2)

print(f"Chai Order : {chai_order}")

chai_recipe = {}

chai_recipe["water"] = "1 cup"
chai_recipe["liquid"]= "milk"

print(f"Chai Recipe liquid : {chai_recipe['liquid']}")

del chai_recipe["liquid"]

print(f"Chai Order : {chai_recipe}")

# Membership test

print(f"Is Sugar in the order? : {'sugar' in chai_order}")

chai_order = dict(type="Ginger Chai", size="Medium", sugar=1)

print(f"Chai Keys : {chai_order.keys()}")
print(f"Chai Values : {chai_order.values()}")
print(f"Chai Items : {chai_order.items()}")

last_item = chai_order.popitem() # remove last item from the dictionary

print(f"Chai Order after removing last item : {chai_order} and last removed item is : {last_item}")

optional_spices = {"cloves":"ginger","black_pepper":"sliced"}
# optional_spices = {"cloves","black_pepper"}  this also work without keys.

chai_recipe.update(optional_spices) # add new items to the dictionary
print(f"Optional Spices : {optional_spices}")

print(f"Chai Recipe after adding optional spices : {chai_recipe}")

chai_size = chai_order["size"]
# chai_size = chai_order["Customer"] crashes because key does not exist in the dictionary

chai_size = chai_order.get("Customer","Not Found") # does not crash but return default value if key does not exist in the dictionary


print(f"Chai Size : {chai_size}")