class InvalidChaiError(Exception): pass

def bill(flavor,cups):
    menu = {"masala": 20,"ginger": 40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("Invalid Chai Flavor not Available")
        if not isinstance(cups,int):
            raise TypeError("Invalid Input Type")
        total = menu[flavor] * cups
        print(f"Total cost for {cups} cups of {flavor} chai: {total}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Thank you for your order!")

bill("masala",3)    
bill("mint",2)
bill("ginger","two")