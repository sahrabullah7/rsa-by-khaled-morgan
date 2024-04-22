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

# Extended Euclidean Algorithm to find the modular inverse 
def extended_gcd(a, b):
                                                           
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b   # the table of the lecture
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

# Generate RSA public and private keys 
def generate_keys(bits):
                                                           
    while True:
        p = generate_large_prime(bits)    # generate the 1st prime no
        q = generate_large_prime(bits)   # generate the 2nd prime no
        if p != q:  # Ensure p and q are different
            break
    n = p * q
    phi = (p - 1) * (q - 1)
    while True:  
        e = random.randrange(2, phi)    # conditions of public key
        if gcd(e, phi) == 1:
            break
    gcd_val, x, y = extended_gcd(e, phi)
    d = x    
    if d<0:
        d+=phi  # d+phi= new d
    return ((e, n), (d, n))  # private key and public key

# Encryption
def encrypt(message, public_key):
                                                        
    e, n = public_key
    encrypted_msg_c= pow(message,e,n) # message power e mod n
    return encrypted_msg_c

# Decryption
def decrypt(encrypted_msg_c, private_key):
                                                            
    d, n = private_key
    decrypted_msg = pow(encrypted_msg_c, d, n)  # encrypted message power d mod n
    return decrypted_msg

# Factorize modulus into its prime factors
def factorize_modulus(n):
                                                             
    for i in range(2, int(math.sqrt(n)) + 1): # range of i of factorizing
        if n % i == 0:
            return i, n // i

# check the brute force function
def check(d, public_key, encrypted_message_c):
    e, n = public_key
    decrypted_message = pow(encrypted_message_c, d, n)  # encrypted message power d mod n
    return decrypted_message

# brute force
def brute_force(public_key, encrypted_message_c):
    d = 2
    while True:
        decrypted_message = check(d, public_key, encrypted_message_c)
        if decrypted_message:    # If decrypted message is not None
            return decrypted_message, d
        d += 1
def main():
    print("RSA Encryption and Decryption\n")
    
    # Generate keys
    bits = int(input("Enter the number of bits for key generation: "))
    
    start_time = time.perf_counter()

    public_key, private_key = generate_keys(bits)
    end_time = time.perf_counter()
    
    print("\nPublic Key (e, n):", public_key)
    print("Private Key (d, n):", private_key)

    # User Input: Define variables for plaintext message
    plaintext = 99 

    # Encryption
    
    encrypted_msg_c = encrypt(plaintext, public_key)
    print("\nEncrypted message c:", encrypted_msg_c)

    # Decryption
    
    decrypted_msg = decrypt(encrypted_msg_c, private_key)
    print("Decrypted message:", decrypted_msg)

    # Factorize modulus
    n = public_key[1]
    p, q = factorize_modulus(n)

    end_time = time.perf_counter()

    print("Factorized Modulus (p, q):", (p, q))
    print("\nProgram Time: {:.6f} ms".format((end_time - start_time) * 1000))

    # Brute force private exponent
    start_time = time.perf_counter()

    encrypted_message_c= encrypt(plaintext, public_key)
    private_exponent = brute_force(public_key, encrypted_message_c)

    end_time = time.perf_counter()
    
    print("\nBrute Force Time: {:.6f} ms".format((end_time - start_time) * 1000))
    print("Private exponent d:", private_exponent)
# Run the program
if __name__ == "__main__":
    main()