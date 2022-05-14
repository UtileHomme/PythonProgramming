# Deque usage

from collections import deque

# This is like a list
friends = deque(('Rolf', 'Charlie', 'Jen'))

friends.append('Jose')
friends.appendleft('Anthony')


print(friends)

friends.pop()
friends.popleft()

print(friends)