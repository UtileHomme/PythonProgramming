from phone import Phone
from keyboard import Keyboard
from item import Item

item1 = Keyboard("jscKeyboard", 1000, 3)

item1.apply_discount()

print(item1.price)

item2 = Item("MyItem", 750, 6)

item2.send_email()

# This shouldn't be allowed
# item2.connect()
