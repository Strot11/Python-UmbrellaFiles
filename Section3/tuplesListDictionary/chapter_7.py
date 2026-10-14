#Tuples are immutable denoted by ()

masala_spices = ("cardamom" , "cloves" , "cinnamons")

# masala_spices = ("cardamom" , False , 10) --> valid

(spice1,spice2,spice3) = masala_spices

print(f"Main masala spicies : {spice1} {spice2} {spice3}")

ginger_ratio, cadramom_ratio = 2,1 # validrepresentation due to tuples 

print(f"Ratio is G:{ginger_ratio} C:{cadramom_ratio}")

ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio

print(f"Ratio is G:{ginger_ratio} C:{cadramom_ratio}")

# membership

print(f"Is Ginger in masala_spices ? : {'ginger' in masala_spices}")

print(f"Is cinnamon in masala_spices ? : {'cinnamons' in masala_spices}") #true

print(f"Is cinnamon in masala_spices ? : {'Cinnamons' in masala_spices}") #false case sensitive

