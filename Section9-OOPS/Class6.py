# Lecture 65 Inheritance and Composition

class BaseChai:
    def __init__(self,type_):
        self.type= type_

    def prepare(self):
        print(f"Preparing {self.type} chai....")

class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom,ginger,cloves.")
        print(self.type)

class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()
        print(type(self.chai))

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai

m1 = MasalaChai("Medium")
m1.add_spices()

shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()



 