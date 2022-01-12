age = int(input("Enter your age:"))
can_learn_programming = age > 0 and age < 150
usually_working = age <= 18 or age >= 65

print(f'At {age}, you are usually working: {usually_working}')

print(bool(0))
print(bool(""))

name = ""
surname = "Smith"

greeting = name or f"Mr {surname}"
print(greeting)

print(not bool(35))