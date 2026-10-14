# Walrus Operators repersented by :=
value  = 13 # not return anything if we write 2+2 it returns 4

remainder = value % 5

if remainder:
    print(f"Not divisible,remainder is {remainder}")

value = 13

if(remainder := value%5):
    print(f"Not divisible,remainder is {remainder}")

# there is new syntax := that assigns values to variables as a part of larger expression.

# return with assigning in variable

available_sizes = ["Small","Medium","Large"]

if(request_size := input("Enter the size 'Small' / 'Medium' / 'Large' ? ")) in available_sizes:
    print(f"Entered the valid Size Here is your {request_size} size")
else:
    print("Entered Invalid Size")

flavours = ["Masala","Ginger","Mint","Lemon"]

print("Available flavours: ", flavours)
chances = 0

while(flavor := input("Choose your Flavour: ")) not in flavours:  # It alaways available outside
    print(f"Enter the valid flavour not {flavor}")
    chances +=1

print(f"Finally you got it in {chances} tries here is your {flavor}")