# Global Variable

chai_type = "plain"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Iranian"
    kitchen()

front_desk()
print(f"Final Global Chai " + chai_type) 

# Handling Arguments 

chai = "Ginger Chai"

def prepare_chai(order):
    print("Preparing Chai "+ order)

prepare_chai(chai)
print(chai)

chai = [1,2,3]

def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)
print(chai)  # Updated to 42

def make_chai(tea,milk,sugar):
    print(tea,milk,sugar)

make_chai("Darjeeling","Yes","Low") #positona args
make_chai(tea="Green",sugar="high",milk="No") #keywords args order doesn't matter

def special_chai(*ingridients,**extras):
    print("Ingridinets ",ingridients)
    print("Extras ",extras)

special_chai("Cinnamon","Cardmom", sweeterner = "Honey",foam = "yes")
# Outputs
# Ingridinets  ('Cinnamon', 'Cardmom')
# Extras  {'sweeterner': 'Honey', 'foam': 'yes'}

def chai_orders(order=[]):  # defaults always store values just as a global variable.
    order.append("Masala")
    print(order)

chai_orders() # ['Masala']
chai_orders() # ['Masala','Masala']

def chai_order(order=None): 
    if order is None:
        # order = []
        order = []
        order.append("Masala")
    print(order)

chai_order() # ['Masala']
chai_order() # ['Masala']