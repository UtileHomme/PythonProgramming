cars = ["ok", "ok", "faulty", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production line")
        break
    print(f"This car is {status}")
    print("Shipping new car to customer!")