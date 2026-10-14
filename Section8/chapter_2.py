def serve_chai():
    yield "Cup1 : Masala Chai"
    yield "Cup2 : Elaichi Chai"
    yield "Cup3 : Ginger Chai"

stall = serve_chai()
for cup in stall:
    print(cup)

def get_chai_list():
    return ["Cup1","Cup2","Cup3"]

# Generator Function
def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()
print(chai) # its an generator object holding reference 
# <generator object get_chai_gen at 0x0000024C34D45540>

print(next(chai)) # Cup 1
print(next(chai)) # Cup 2
print(next(chai)) # Cup 3
print(next(chai)) # Gives Error
# Traceback (most recent call last):
#  File "C:\Users\Hp\Projects\Python-Projects\Section8\chapter_2.py", line 26, in <module>
#    print(next(chai)) # Cup
#          ~~~~^^^^^^
#StopIteration
