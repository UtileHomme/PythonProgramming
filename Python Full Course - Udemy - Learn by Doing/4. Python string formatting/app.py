age = 34
age_as_str = str(age)

# This formats the variable as part of the string
print(f"You are {age}")

name = "Jatin"

final_greeting = "How are you, {}?"
final_greeting1 = "How are you, {name}?"

# for real time injection into code
jatins_greeting = final_greeting.format(name)
jatins_greeting1 = final_greeting.format("Jatin1")

jose_greeting = final_greeting1.format(name="Jose")
print(jose_greeting)



