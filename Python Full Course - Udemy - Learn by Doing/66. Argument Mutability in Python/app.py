friends_last_seen = {
    'Rolf' : 31,
    'Jen' : 1,
    'Anne' : 7
}

def see_friend(friends, name):

    # 1686828525248
    print(id(friends))
    friends[name] = 0

# 1686828525248
print(id(friends_last_seen))

# 1762226176
print(id(friends_last_seen['Rolf']))

see_friend(friends_last_seen, 'Rolf')

# 1762225184
print(id(friends_last_seen['Rolf']))

# 1686828525248
print(id(friends_last_seen))

