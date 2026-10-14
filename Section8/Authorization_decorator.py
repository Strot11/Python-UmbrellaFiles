from functools import wraps
# If you remove @wraps(func) then the identity of your function is completely overwritten and lost.
def require_admin(func):
    @wraps(func)  # to preserve the metadata
    def wrapper(user_role):
        if user_role != "admin":
            print("Access Denied: Admins Only")
            return None
        else:
            return func(user_role)
        
    return wrapper

@require_admin
def access_tea_inventory(role):
    print("Access Granted to tea inventory")

access_tea_inventory("admin")
access_tea_inventory("user")
        