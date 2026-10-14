# Simple Suggestion Program

a = input("Hey there! Enter your Favourite Meal ? ").lower()

if a == 'samosa' or a == 'biryani':
    print("You are a true Indian")
elif(a == 'pizza'):
    print("You are a true Italian")
elif(a == 'sushi'):
    print("You are a true Japanese")
else:
    print("You are a true Global Citizen")

size = input("Hey Whats your Cup Size ?").lower()

switch = {
   "small" : "Your amount is 10 Rupees",
   "medium" : "Your amount is 20 Rupees",
   "large" : "Your amount is 30 Rupees"
}

if(size in switch):
    print(f"Buddy {switch[size]}")
else:
    print("Unknown Cup Size")