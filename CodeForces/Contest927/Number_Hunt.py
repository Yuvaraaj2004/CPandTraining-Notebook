import math


def is_prime(num):
    """Check if a number is prime using a list of small primes."""
    if num <= 1:
        return False
    prime = 2
    while prime*prime <= num:
        if num % prime == 0:
            return False
        prime += 1
    return True


for t in range(int(input())):
    n = int(input())
    l = []
    while len(l) < 2:
        if is_prime(n):
            l.append(n)
        n += 1
    print(l[0]*l[1], l)
