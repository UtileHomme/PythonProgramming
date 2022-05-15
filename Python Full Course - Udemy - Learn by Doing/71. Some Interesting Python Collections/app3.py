# Ordered dict usage
# They retain the order of the keys in which they were added to the dictionary. It doesn't sort automatically

from collections import OrderedDict

o = OrderedDict()
o['Rolf'] = 6
o['Jose'] = 12
o['Jen'] = 3

print(o)

o.move_to_end('Rolf')

print(o)
o.move_to_end('Jen', last=False)

print(o)

# Removes the last item from the end
o.popitem()

print(o)

