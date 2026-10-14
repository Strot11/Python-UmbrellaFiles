# for loop range enumerate zip

for token in range(1,11):
    print(f"Serving Chai to Token #{token}")

for batch in range(1,5):
    print(f"Preparing Chai for Batch #{batch}")

orders = ["strot","aman","rishiraj","nayan","puran"]

for name in orders:
    print(f"Order for #{name}")

menu = ["Green","Lemon","Spiced","Mint"]

for m in menu:
    print(f"Menu item is {m}")

for idx,item in enumerate(menu, start=1):  # creates a tuple [(1,item1),(2,item2)..]
    print(f"{idx} : {item} chai")

names = ["Strot","Rishiraj","Animesh","Nayan"]
bills = [50,70,60,10]

for name, amount in zip(names,bills):
    print(f"{name} paid {amount} rupees")