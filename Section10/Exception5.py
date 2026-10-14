# Creating Custom Exceptions

class OutOfIngridientsError(Exception):
    pass

def make_chai(milk,sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngridientsError("Missing milk or sugar")
    print("Chai is Ready")

make_chai(2,0)