# Hiding the Implementation Details 

def get_input():
    print("Getting user Input")

def validate_input():
    print("Validating user Input")

def save_to_db():
    print("saving to database")

def registerUser():
    get_input()
    validate_input()
    save_to_db()
    print("Registration Successful")

registerUser()

#Improving the Readability

def calculate_bill(cups,price):
    return cups*price

my_bill = calculate_bill(9,8)
print(my_bill)
print(f"Order for Table 2 :", calculate_bill(9,8))

# Improving Traceability your logic not be scattered and difficult to understand the flow

def add_vat(price,vat_rate):
    return price * (100 + vat_rate)/100

orders = [100,150,200]

for price in orders:
    final_amount = add_vat(price,10)
    print(f"Original: {price} , Final after vat Calculation : {final_amount}")