# import recipes.flavors

# print(recipes.flavors.elaichi_chai())

from recipes.flavors import ginger_chai as function1

print(function1());

from utils.discount import chai_discount

print(chai_discount(10,20,0.2))

from .recipes.flavors import ginger_chai
