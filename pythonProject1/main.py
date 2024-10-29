# This is a sample Python script.

import math

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def check_prime(n):
    if n < 2:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return 0
        return 1


def prime_sieve(n):
    if n <= 2:
        return 0
    ind = [1] * n
    ind[0] = 0
    for i in range(1, len(ind)):
        if i ** 2 > n:
            break
        else:
            for j in range((i + 1) ** 2, n, (i + 1)):
                ind[j] = 0
    return sum(ind) - 1
# Press the green button in the gutter to run the script.


class Person:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.bmi = (weight^2)/height

    def selfloathing(self) -> object:
        print("I hate myself.")


if __name__ == '__main__':
    result = int(input())
    if check_prime(result):
        print("It is a prime!")
        print("Total primes less than it: " + str(prime_sieve(result)))
    else:
        print("It is not a prime...")
        print("Total primes less than it: " + str(prime_sieve(result)))
    k = Person(180,85)
    print(k.bmi)
    k.selfloathing()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
