# Scopes
def serve_chai():
    chai_type="Masala" # local scope
    print(f"Inside function {chai_type}")

chai_type = "lemon"
serve_chai();
print(f"Outside function {chai_type}")

# Nested 

def chai_counter():
    chai_order = "Cloves"
    def print_order():
        chai_order = "Lemon"
        print(f"Your order Inside Sir : {chai_order}")
    print(f"Your order Outside Sir : {chai_order}")
    print_order()

chai_order= "Tulsi"
chai_counter()
print(f"Your order FULL Outside Sir : {chai_order}")

# Scopes Continued

def update_order():
    chai_type = "Elaichi"
    def Kitchen():
        nonlocal chai_type
        chai_type = "Kesar"
    Kitchen()
    # Changed to Kesar from Elaichi
    print(f"After Kitchen update "+ chai_type)

update_order()