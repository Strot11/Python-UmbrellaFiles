chai_type = "Ginger Chai"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type} please ?")

chai_description ="Aromatic and Bold"
# slicing
print(f"First word: {chai_description[0:8]}")
print(f"First word: {chai_description[0:-1]}")
print(f"First word: {chai_description[0]}")
print(f"First word: {chai_description[0:8:2]}") #every second character
print(f"First word: {chai_description[:8]}")
print(f"First word: {chai_description[12:]}")
print(f"First word: {chai_description[::-1]}") #reverse the string

label_text= "Chai Special" #provided in another language then like japanese french greek etc then we use utf.

encoded_label = label_text.encode("utf-8")
delabeled_text = encoded_label.decode("utf-8")
print(f"Encoded label: {encoded_label}")
print(f"Non Eecoded label: {label_text}")
print(f"Decoded label: {delabeled_text}")
