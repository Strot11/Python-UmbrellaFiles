def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

#Masala Chai
# Ginger Chai
# Matcha
# Oolong

def chai_stall():
    try:
        while True:
            order = yield "Waiting for Chai Order"
    except:
        print("Stall Closed, No More Chai")

stall = chai_stall()

print(next(stall))
#Waiting for Chai Order 
#Stall Closed, No More Chai
print(next(stall))
#Waiting for Chai Order
#Waiting for Chai Order
#Stall Closed, No More Chai
stall.close()  # Should be done cleanup generates a generator exit method 

