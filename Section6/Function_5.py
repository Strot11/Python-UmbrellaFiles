def make_chai():
    return "Here is Your Masala Chai"

print(make_chai()) #Here is Your Masala Chai

def make_chai():
    print("Here is Your Masala Chai")

print(make_chai()) # None

def ideal_chaiwala():
    pass

print(ideal_chaiwala) # <function ideal_chaiwala at 0x000001455989BAB0>

# <function ... >: Indicates that the object is a function.
# ideal_chaiwala: The specific name of the function you defined in your code
# .at 0x000001455989BAB0: The hexadecimal memory address where this function object is 
# currently stored in your computer's RAM.

print(ideal_chaiwala())

def sold_cups():
    return 10

print(sold_cups())

def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai over"
    return "Chai is Ready"
    print("This Part is never Executed") # unreachable code (or dead code)

print(chai_status(0))
print(chai_status(1))

def chai_report():
    return 100,20,10  # sold,remaining

sold,remaining,_ = chai_report();
print("Sold:",sold)
print("Remaining:",remaining)
 
