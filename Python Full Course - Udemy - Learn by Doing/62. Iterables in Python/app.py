# Iterator: used to get the next value
# Iterable: used to go over all the values of the iterator

class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            # Error in case we reach end of generator
            raise StopIteration()

    def __iter__(self):
        return self


my_gen = FirstHundredGenerator()
# print(my_gen.number)
# my_gen.__next__()
print(next(my_gen))
print(next(my_gen))


# print(my_gen.number)

# class FirstFiveIterator:
#     def __init__(self):
#         self.numbers = [1,2,3,4,5]
#         self.i = 0
#
#     def __next__(self):
#         if self.i < len(self.numbers):
#             current = self.numbers[self.i]
#             self.i +=1
#             return current
#         else:
#             raise StopIteration()

# class FirstHundredIterable:
#     def __iter__(self):
#         return FirstHundredGenerator()


# Sum of 1 + 2 + ..... + 99
# print(sum(FirstHundredIterable()))
#
# for i in FirstHundredIterable():
#     print(i)

class AnotherIterable:
    def __init__(self):
        self.cars = ['Fiesta', 'Focus']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]


for car in AnotherIterable():
    print(car)
