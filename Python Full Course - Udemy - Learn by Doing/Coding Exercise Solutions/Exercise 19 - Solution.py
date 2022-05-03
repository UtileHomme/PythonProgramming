"""
Take a look at the code in the problem description where we test if a number is prime.
Refactor the code and put it into the function below to turn the prime_generator() function into a generator.

Implement your generator so that others can get a prime number generator like this:

g = prime_generator(100)    # g can generate prime numbers under 100
next(g) # get next prime like this

Reminder: you don't need to change the function name nor the argument
"""

class PrimeGenerator:
    def __init__(self, stop):
        self.stop = stop
        self.start = 2

    def __next__(self):
        for n in range(self.start, self.stop):
            for x in range (2,n):
                if n % x == 0:
                    break
            else:
                self.start = n + 1

                return n

        raise StopIteration()


