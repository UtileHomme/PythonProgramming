import pricing_module

net_price = pricing_module.get_net_price(price=100, tax_rate=0.01)

print(net_price)

#1. Import module as a new name

import pricing_module as selling_price

net_price = selling_price.get_net_price(price=100, tax_rate=0.01)

print(net_price)

#2. Importing the functions or variables of the module

from pricing_module import get_net_price, get_tax

net_price = get_net_price(price=100, tax_rate=0.01)

print(net_price)

# 3. Renaming the functions while importing module

from pricing_module import get_net_price as calculate_net_price

net_price = calculate_net_price(
    price=100,
    tax_rate=0.1,
    discount=0.05
)

print(net_price)

# 4. Importing all objects in one go

from pricing_module import *

net_price = calculate_net_price(
    price=100,
    tax_rate=0.1,
    discount=0.05
)

print(net_price)

# Sometimes two modules might have the same function. In that case,
# whichever module is imported later will override the earlier function's definitiion

from pricing_module import *
from product_module import *

tax = get_tax(100)
print(tax)
