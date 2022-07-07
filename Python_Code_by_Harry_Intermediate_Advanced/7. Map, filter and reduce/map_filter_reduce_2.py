# Filter function
#  makes a list of elements for which a function returns True

def greater_than_2(n):
    if n > 2:
        return True
    else:
        return False


h1 = [1, 2, 4, 5, 7, 532, 32]

greater_then_2 = filter(greater_than_2, h1)
greater_then_2_list = list(greater_then_2)

print(greater_then_2_list)
