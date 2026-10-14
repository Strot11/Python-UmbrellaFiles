essential_spices = {"cardamon","ginger","cinnamon"}
optional_spices = {"cloves","ginger","black_pepper"}

all_spices = essential_spices | optional_spices

common_spices = essential_spices & optional_spices

only_in_essential = essential_spices - optional_spices

print(f"All Spices : {all_spices}")
print(f"Common Spices : {common_spices}")
print(f"Only in essential Spices : {only_in_essential}")

# Membership Test 

print(f"Is cloves in essential_spices : {'cloves' in essential_spices}") 
print(f"Is cloves in optional_spices : {'cloves' in optional_spices}") 

# FrozzenSet  see on web

