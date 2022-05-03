friends = ["Rolf", "Jose", "Randy", "Anna", "Mary"]

# We are trying to convert the original friends values to lower case
# https://www.geeksforgeeks.org/python-map-function/
friends_lower = map(lambda x: x.lower(), friends)

# The above is a simulated version of below code
friends_lower_sim = [friend.lower() for friend in friends]

friends_lower_generator = (friend.lower() for friend in friends)

print(next(friends_lower))


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data["username"], data["password"])


users = [
    {
        'username': 'rolf', "password": '123'
    },
    {
        'username': 'teclado', "password": 'youaretoo'
    }
]

users = [User.from_dict(user) for user in users]
users = map(User.from_dict, users)
