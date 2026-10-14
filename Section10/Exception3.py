# Multiple Exception Handling

def process_order(item,quantity):
    try:
        price = {"masala": 100, "ginger": 80}[item]
        cost = price * quantity
        print(f"Total cost for {quantity} {item} chai: {cost}")
    except KeyError:
        print("Error: Item not found")
    except TypeError:
        print("Error: Invalid input types")

process_order("ginger",2)
process_order("unknown",2)
process_order("masala","two")