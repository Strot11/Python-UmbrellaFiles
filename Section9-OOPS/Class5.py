# Constructors  Lecture 64

class ChaiOrder:

    def __init__(self,type_,size):
        self.type = type_
        self.size = size

    def summary(s):
        return f"{s.size} Cup of {s.type} Chai"  #f-string, which is short for formatted string literal.

order = ChaiOrder("Ginger","Medium")
print(order.summary())

order_2 = ChaiOrder("Clove","Full")
print(order_2.summary())