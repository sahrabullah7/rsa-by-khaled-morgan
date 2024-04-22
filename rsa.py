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

#  Generate a large prime number
def generate_large_prime(bits):
                                                          
    while True:
        p = random.randint(2**(bits-1), 2**bits)   # generate the prime no
        if is_prime(p):
            return p

# Calculate the Greatest Common Divisor of two numbers 
def gcd(a, b):
                                                          
    while b != 0:
        a, b = b, a % b          # swap a with the b, swap b with the remainder of a nd b after division
    return a
