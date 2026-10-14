from functools import wraps

def log_activity(func):

    def wrapper(*args,**kwargs):
        print(f"Calling: {func.__name__}")
        result = func(*args,**kwargs)
        print(f"Finished: {func.__name__}")
        return result
    return wrapper

@log_activity
def brew_chai(type,type1,milk):
    print(f"Brewing {type,type1} {milk} chai")

brew_chai("Ginger","Lemon",milk=30) # brew_chai = log_activity(brew_chai) gets executed

#Line 1: Python imports the wraps utility from the functools module.
# Lines 3–12: Python registers the log_activity decorator function in memory. 
# It does not execute the inside code yet.
# Line 14: Python encounters the @log_activity decorator. 
# It pauses to read the function directly below it.Lines 
# 15–16: Python compiles the brew_chai function.
#The Decoration Hook: Because of the @ symbol, Python automatically executes:

# pythonbrew_chai = log_activity(brew_chai)

# Inside log_activity, the func parameter points to your original brew_chai.
# The @wraps(func) decorator copies the original name ("brew_chai") onto the wrapper function.log_activity 
# returns the wrapper function object.Now, the variable name brew_chai points 
# directly to the wrapper function.