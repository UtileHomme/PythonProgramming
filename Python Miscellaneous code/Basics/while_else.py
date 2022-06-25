# The while loop is checked and if there is no break statement or return statement, the else will run
# If there is a break or return statement, else statement will not run

# The conventional way

basket = [
    {'fruit': 'apple', 'qty': 20},
    {'fruit': 'banana', 'qty': 30},
    {'fruit': 'orange', 'qty': 10},
]

fruit = input('Enter a fruit :')

index = 0

found_it = False

while index < len(basket):
    item = basket[index]

    if item['fruit'] == fruit:
        found_it = True
        print(f"The basket has {item['qty']} with item {item['fruit']}(s)")
        break

    index += 1

if not found_it:
    qty = int(input(f'Enter the quantity of the {fruit}'))
    basket.append({'fruit': fruit, 'qty': qty})
    print(basket)

# Using while else

basket = [
    {'fruit': 'apple', 'qty': 20},
    {'fruit': 'banana', 'qty': 30},
    {'fruit': 'orange', 'qty': 10},
]

fruit = input('Enter a fruit :')

index = 0

while index < len(basket):
    item = basket[index]

    if item['fruit'] == fruit:
        found_it = True
        print(f"The basket has {item['qty']} with item {item['fruit']}(s)")
        break

    index += 1
else:
    qty = int(input(f'Enter the quantity of the {fruit}'))
    basket.append({'fruit': fruit, 'qty': qty})
    print(basket)
