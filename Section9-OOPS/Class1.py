class Chai:
    pass

class ChaiTime:
    pass

print(type(Chai))

ginger_tea = Chai()

print(type(ginger_tea)) # <class '__main__.Chai'> means object(__Main__) of the Chai class

print(type(ginger_tea) is Chai)

print(type(ginger_tea) is ChaiTime)




