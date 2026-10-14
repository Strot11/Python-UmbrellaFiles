# Dictionary Case

users = [{"id":1, "total": 100, "coupon":"P20"},
         {"id":2, "total": 200, "coupon":"F10"},
         {"id":3, "total": 300, "coupon":"P50"}]

discounts = {
    "P20" : (0.2,0),
    "F10" : (0.5,0),
    "P50" : (0,10)
}

for user in users:
    percent,fixed = discounts.get(user["coupon"], (0,0)) # (0,0) is the default value
    discount = user["total"] * percent + fixed 
    print(f"user {user["id"]} paid {user["total"]} and got discount for the next visit of rupees {discount}")

