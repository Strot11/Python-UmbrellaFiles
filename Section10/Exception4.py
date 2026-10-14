# Custom Exceptions

def brew_chai(flavor):
    if flavor not in ["masala","ginger"]:
        raise ValueError("Unsupported Chai Flavor")
    print(f"Brewing {flavor} chai")

brew_chai("mint")