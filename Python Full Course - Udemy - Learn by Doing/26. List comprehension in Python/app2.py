friend = input("Enter your friend's name")
friends = ["Rolf", "Bob", "Jen", "Charlie"]
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
    # title turns the first letter as uppercase
    print(f"{friend.title()} is one of your friends")