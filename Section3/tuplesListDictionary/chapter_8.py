# List/Arrays are mutables denoted by []

ingredients= ["water","milk","black tea"]

ingredients.append("ginger") # add new item to the list

print(f"Ingredients : {ingredients}")

ingredients.remove("milk")

print(f"Ingredients : {ingredients}")

spice_options = ["ginger","cardamon","cinnamon"]

chai_ingredients = ["water", "milk", "black tea"] 

chai_ingredients.extend(spice_options) # add new items to the list

print(f"Chai: {chai_ingredients}")

chai_ingredients.insert(1,"sugar") # add new item to the list at index 1

print(f"Chaiwith sugar: {chai_ingredients}")

last_added = chai_ingredients.pop() # remove last item from the list

print(f"Chai after removing last added element : {chai_ingredients} and last added element is : {last_added}")

chai_ingredients.reverse() # not return anything but reverse the list in place

print(f"Chai after Reversing the list : {chai_ingredients}")

chai_ingredients.sort() 

print(f"Chai after Sorting the list : {chai_ingredients}")

sugar_levels = [1,2,3,4,5]

print(f"Maximum sugar level : {max(sugar_levels)}")
print(f"Minimum sugar level : {min(sugar_levels)}")

# Extension Lecture for Operator Overloading

base_liquid = ["water","milk"]

extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor # operator overloading for + operator

print(f"Full Liquid Mix : {full_liquid_mix}")

strong_brew = ["black tea","water"] * 3 # operator overloading for * operator

print(f"Strong Brew : {strong_brew}")

# "Cinnamon" --> list

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA",b"GINGER") # replace CINNA with GINGERMON
print(f"Bytes:  {raw_spice_data}")
# 8:11 