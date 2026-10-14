# Send Generators

def chai_customer():
    print("Welcome ! What chai would you like ?")
    order = yield    # Someone will give me a chai order 
    a = 3
    while a>0:
        print(f"Preparing : {order}")
        order = yield # Wait for order
        a-=1

stall = chai_customer()
next(stall) # Start Generator
# Welcome ! What chai would you like ? Executed upto here waiting for input yield
# Function will wait for yield value for execution
stall.send("Masala")
# Welcome ! What chai would you like ?
# Preparing : Masala
stall.send("Lemon")
stall.send("Ginger")
# stall.send("Clove")  # Error