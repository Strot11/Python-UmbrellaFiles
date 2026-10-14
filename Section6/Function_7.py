def chai_flavor(flavor="Masala"):
    """Return the flavor of chai."""
    return flavor

print(chai_flavor.__doc__)  # called as dunder
print(chai_flavor.__name__)

help(len)

def generate_bill(chai=0,samosa = 0):
    """
    Calculate the total bill for chai and samosa

    :Param chai: Number of chai cups (10 rupee each)
    :Param chai: Number of samosa (15 rupees each)
    : return :(total amount, thank you message)
    """
    total = chai*10 + samosa*15
    return total,"Thank you For Visiting Us"

print(generate_bill(9,8))