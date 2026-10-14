temperature = 40
seconds = 0
while temperature <= 100:
    print(f"Current Temperature : {temperature}")
    seconds+=1
    temperature += 5

print(f"Water Boiled Bro Taken {seconds} secs")

# Use of Continue and Break

flavours = ["Ginger","Out of Stock","Lemon","Discontinued","Tulsi"]

for flav in flavours:
    if flav == "Out of Stock":   # just skip this iteration
        continue
    elif flav == "Discontinued":  # out of loop
        break
    print(f"Your Flavour is {flav}")

# For Else 

staff= [("Amit",16),("Zara",20),("Raj",24)]

for name,age in staff:
    if age >=18  :
        print(f"{name} is eligible for managing staff") # print the first true condition break
        break    # if not break else block also execute
else :
    print("No one is Eligible to manage the task") # only when no if is executed
