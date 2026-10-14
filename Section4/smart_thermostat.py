device_status = input("Enter device Status 'Active' to start: ").lower()

if(device_status=='active'):

    temperature = int(input("Enter the Temperture: "))

    if temperature > 35: print("Warning High Temperature")

    else: print("Temperature is Normal")

else: print("Device Offline")

# Cost Deduction Logic 

order_amount = float(input("Enter the order amount: "))

delivery_fees = 0 if order_amount<300 else 300

print(f"Remaining Fees After Delivery Cost Deduction : {order_amount-delivery_fees}")
