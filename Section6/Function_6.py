def pure_chai(cups):
    
    return cups*10;

total_chai = 0;

def impure_chai(cups):

    global total_chai

    total_chai+=cups

def fibonaci(n):
    if n==0 or n==1:
        return 1
    return fibonaci(n-1) + fibonaci(n-2)

x = int(input("Enter the nth term you need from fibonacii: "))

print(fibonaci(x))

chai_types = ["light","kadak","ginger","kadak"]

strong_chai = list(filter(lambda chai: chai!="kadak",chai_types))

print(strong_chai)