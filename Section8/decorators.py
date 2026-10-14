#def my_decorator(func):
#
#    def wrapper():
#        print("Before Function Runs")
#        func()
#        print("After Function runs")
#
#    return wrapper()   --> runs automatically without calling the function
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before Function Runs")
        func()
        print("After Function runs")

    return wrapper

@my_decorator   # whatever coming after this line going to get wrapped up!!!
def greet():
    print("Hello from decorator class checkers")

greet()  
print(greet.__name__) # wrapper if tool wraps is not used & used then greet