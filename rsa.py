import random           # generating random number
import math         # math eqautions
import time        # get time

# Check if a number is prime
def is_prime(n):
                                                          
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:   # get all prime numbers
        if n % i == 0:
            return False
        if n % (i + 2) == 0:
            return False
        i += 6 # new i
    return True