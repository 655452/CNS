# def xor_127(name):


#     print("for and")
#     for c in name:
#         print(chr(ord(c)&127),end=" ")

#     # or 
#     print("\nfor or")
#     for c in name:
#         print(chr(ord(c)|127),end=" ")
#         # xor
    
#     print("\nfor xor")
#     for c in name:
#         print(chr(ord(c)^127),end=" ")



# xor_127("Asit")

#  practical rsa
import random 
import math

def generate_p_and_q():

    # calculate from 1 to 100 prime numbers
    numbs=[i for i in range(2,101)]

    for n in range(2,101):
        for i in range(2,math.ceil(n/2)+1):
            if(n%i==0):
                numbs.remove(n)
                break
            else:
                continue
    
    # select any two prime nu randomly
    p=random.choice(numbs)
    numbs.remove(p)
    q=random.choice(numbs)
    numbs.remove(q)

    return p,q;

p,q=generate_p_and_q()

print(f"the p = {p} and q  = {q} are ")

# calculate n=p*q
n=p*q
# phi
phi=(p-1)*(q-1)

# calculating e gcd of (e,phi)==1 1<e<phi
def generate_e(phi):

    possible_value=[]
    for i in range(2,phi):
        if math.gcd(i,phi)==1:
            e=i
            possible_value.append(e)

    return random.choice(possible_value)

e=generate_e(phi)

print(f"the  e = {e}")

def generate_d(e,phi):
    d_list=[]

    for i in range(2,phi): # edmod(phi)==1
        if((i*e)%phi==1):
            d=i;
            d_list.append(d)
            break

    return d

d=generate_d(e,phi)
print(f" value of d= {d}")

msg=int(input("Enter the message"))

print(f" msg = {msg}")

def encrypt(msg,e,n): # msg^emod n
    c=pow(msg,e,n)
    return c
encrypt_message=encrypt(msg,e,n)
print(f" encrpted message = {encrypt_message}")

def decrypt(msg,d,n):  #msg^dmod n]
    p=pow(msg,d,n)
    return p

decrypted_message=encrypt(encrypt_message,e,n)
print(f" decrypted message = {decrypted_message}")

# rsa for characters
import random 
import math

def generate_p_and_q():
    # calculate from 1 to 100 prime numbers
    numbs = [i for i in range(2, 101)]

    for n in range(2, 101):
        for i in range(2, math.ceil(n / 2) + 1):
            if (n % i == 0):
                numbs.remove(n)
                break
            else:
                continue

    # select any two prime numbers randomly
    p = random.choice(numbs)
    numbs.remove(p)
    q = random.choice(numbs)
    numbs.remove(q)

    return p, q

def generate_e(phi):
    possible_values = [i for i in range(2, phi) if math.gcd(i, phi) == 1]
    return random.choice(possible_values)

def generate_d(e, phi):
    d_list = [i for i in range(2, phi) if (i * e) % phi == 1]
    return d_list[0]

def encrypt(msg, e, n):
    # Convert each character to its ASCII value and encrypt
    encrypted_msg = [pow(ord(char), e, n) for char in msg]
    return encrypted_msg

def decrypt(encrypted_msg, d, n):
    # Decrypt each value and convert back to characters
    decrypted_msg = ''.join([chr(pow(char, d, n)) for char in encrypted_msg])
    return decrypted_msg

p, q = generate_p_and_q()
print(f"The p = {p} and q = {q}")

# Calculate n = p * q
n = p * q
# Phi
phi = (p - 1) * (q - 1)

# Calculate e (gcd of (e, phi) == 1, 1 < e < phi)
e = generate_e(phi)
print(f"The e = {e}")

# Calculate d
d = generate_d(e, phi)
print(f"The value of d = {d}")

# Take input message as a string
msg = input("Enter the message: ")

# Encrypt and Decrypt
encrypted_message = encrypt(msg, e, n)
print(f"Encrypted message: {encrypted_message}")

decrypted_message = decrypt(encrypted_message, d, n)
print(f"Decrypted message: {decrypted_message}")
# ######################################################################################
# fiestal block cipher structure
import binascii
import random

# random bits key generation
def  rand_key(p):
    
    key1=""
    p=int(p)

    for i in range(p):
        temp=random.randint(0,1)
        temp=str(temp)
        key1=key1+temp
    return key1

# function to implement bit exor

def exor(a,b):
    temp=""
  

    for i in range(n):
        if(a[i]==b[i]):
            temp+="0"
        else:
            temp+="1"
    return temp

def BinaryToDecimal(binary):

    string=int(binary,2)

    return string

PT="Hello"
print(f" plain Text {PT}")

# convert plaintext to ascii
PT_Ascii=[ord(x) for x in PT]

# convert Ascii to 8 bit binary format

PT_Bin=[format(y,'08b')for y in PT_Ascii]
PT_Bin="".join(PT_Bin)

n=int(len(PT_Bin)//2)
L1=PT_Bin[0:n]

R1=PT_Bin[n::]
m=len(R1)

# generate key for first round

K1=rand_key(m)

# gerate key for second round

K2=rand_key(m)

# first round of festal cipher
f1=exor(R1,K1)
R2=exor(f1,L1)
L2=R1
# second round of festalcipher
f2=exor(R2,K2)
R3=exor(f2,L2)
L3=R2



# Ciper text
bin_data=L3+R3
str_data=" "

for i in range(0,len(bin_data),7):

    temp_data=bin_data[i:i+7]

    decimal_data=BinaryToDecimal(temp_data)

    str_data=str_data+chr(decimal_data)

print(f"Cipher text {str_data}  binaary data {bin_data}")

# Decryption
L4 = L3
R4 = R3
  
f3 = exor(L4,K2)
L5 = exor(R4,f3)
R5 = L4
  
f4 = exor(L5,K1)
L6 = exor(R5,f4)
R6 = L5
PT1 = L6+R6
  
 
PT1 = int(PT1, 2)
RPT = binascii.unhexlify( '%x'% PT1)
print("Retrieved Plain Text is: ", RPT)

# # fiestal block cipher structure
# import binascii
# import random

# # random bits key generation
# def rand_key(p):
#     key1 = ""
#     p = int(p)

#     for i in range(p):
#         temp = random.randint(0, 1)
#         temp = str(temp)
#         key1 = key1 + temp
#     return key1

# # function to implement bit exor
# def exor(a, b):
#     temp = ""
#     for i in range(n):
#         if a[i] == b[i]:
#             temp += "0"
#         else:
#             temp += "1"
#     return temp

# def BinaryToDecimal(binary):
#     string = int(binary, 2)
#     return string

# PT = "Hello"
# print(f"Plain Text {PT}")

# # convert plaintext to ascii
# PT_Ascii = [ord(x) for x in PT]

# # convert Ascii to 8 bit binary format
# PT_Bin = [format(y, '08b') for y in PT_Ascii]
# PT_Bin = "".join(PT_Bin)

# n = int(len(PT_Bin) // 2)
# L1 = PT_Bin[0:n]
# R1 = PT_Bin[n::]
# m = len(R1)

# # generate key for first round
# K1 = rand_key(m)

# # generate key for second round
# K2 = rand_key(m)

# # generate key for third round
# K3 = rand_key(m)

# # first round of festal cipher
# f1 = exor(R1, K1)
# R2 = exor(f1, L1)
# L2 = R1

# # second round of festal cipher
# f2 = exor(R2, K2)
# R3 = exor(f2, L2)
# L3 = R2

# # third round of festal cipher
# f3 = exor(R3, K3)
# R4 = exor(f3, L3)
# L4 = R3

# # Cipher text
# bin_data = L4 + R4
# str_data = " "

# for i in range(0, len(bin_data), 7):
#     temp_data = bin_data[i:i+7]
#     decimal_data = BinaryToDecimal(temp_data)
#     str_data = str_data + chr(decimal_data)

# print(f"Cipher text {str_data}  binary data {bin_data}")

# # Decryption
# L5 = L4
# R5 = R4
  
# f4 = exor(L5, K3)
# L6 = exor(R5, f4)
# R6 = L5
  
# f5 = exor(L6, K2)
# L7 = exor(R6, f5)
# R7 = L6

# f6 = exor(L7, K1)
# L8 = exor(R7, f6)
# R8 = L7
# PT1 = L8 + R8

# PT1 = int(PT1, 2)
# RPT = binascii.unhexlify('%x' % PT1)
# print("Retrieved Plain Text is:", RPT)


# difffie hellman
 # Diffie-Hellman Code

def prime_checker(p):
    # Checks if the number entered is a Prime Number or not
    if p < 1:
        return -1
    elif p > 1:
        if p == 2:
            return 1
        for i in range(2, p):
            if p % i == 0:
                return -1
        return 1

def primitive_check(g, p, L):
    # Checks if the entered number is a Primitive Root or not
    for i in range(1, p):
        L.append(pow(g, i) % p)
    for i in range(1, p):
        if L.count(i) > 1:
            L.clear()
            return -1
    return 1

def encrypt(message, key):
    return ''.join([chr(ord(c) + key) for c in message])

def decrypt(encrypted_message, key):
    return ''.join([chr(ord(c) - key) for c in encrypted_message])

l = []

while 1:
    P = int(input("Enter P: "))
    if prime_checker(P) == -1:
        print("Number is not prime. Please enter again!")
        continue
    break

while 1:
    G = int(input(f"Enter the primitive root of {P}: "))
    if primitive_check(G, P, l) == -1:
        print(f"Number is not a primitive root of {P}. Please try again!")
        continue
    break

# Private Keys
x1, x2 = int(input("Enter the private key of Alice: ")), int(
    input("Enter the private key of Bob: "))

while 1:
    if x1 >= P or x2 >= P:
        print(f"Private keys of both users should be less than {P}!")
        continue
    break

# Calculate Public Keys
y1, y2 = pow(G, x1) % P, pow(G, x2) % P

# Generate Secret Keys
k1, k2 = pow(y2, x1) % P, pow(y1, x2) % P

print(f"\nSecret Key for Alice is {k1}\nSecret Key for Bob is {k2}\n")

if k1 == k2:
    print("Keys have been exchanged successfully.\n")

#     while True:
#         # Alice sends a message to Bob
#         message_from_alice = input("Alice, enter the message to be transmitted to Bob: ")
#         encrypted_message_from_alice = encrypt(message_from_alice, k1)
#         print(f"Encrypted Message from Alice to Bob: {encrypted_message_from_alice}")

#         # Bob receives and decrypts the message from Alice
#         decrypted_message_from_alice = decrypt(encrypted_message_from_alice, k2)
#         print(f"Decrypted Message from Alice to Bob: {decrypted_message_from_alice}\n")

#         # Bob sends a message to Alice
#         message_from_bob = input("Bob, enter the message to be transmitted to Alice: ")
#         encrypted_message_from_bob = encrypt(message_from_bob, k2)
#         print(f"Encrypted Message from Bob to Alice: {encrypted_message_from_bob}")

#         # Alice receives and decrypts the message from Bob
#         decrypted_message_from_bob = decrypt(encrypted_message_from_bob, k1)
#         print(f"Decrypted Message from Bob to Alice: {decrypted_message_from_bob}\n")

# else:
#     print("Keys have not been exchanged successfully.")


def prime_checker(p):
    # Checks if the number entered is a Prime Number or not
    if p < 1:
        return -1
    elif p > 1:
        if p == 2:
            return 1
        for i in range(2, p):
            if p % i == 0:
                return -1
        return 1

def primitive_check(g, p, L):
    # Checks if the entered number is a Primitive Root or not
    for i in range(1, p):
        L.append(pow(g, i) % p)
    for i in range(1, p):
        if L.count(i) > 1:
            L.clear()
            return -1
    return 1

def encrypt(message, key):
    return ''.join([chr(ord(c) + key) for c in message])

def decrypt(encrypted_message, key):
    return ''.join([chr(ord(c) - key) for c in encrypted_message])

l = []

while 1:
    P = int(input("Enter P: "))
    if prime_checker(P) == -1:
        print("Number is not prime. Please enter again!")
        continue
    break

while 1:
    G = int(input(f"Enter the primitive root of {P}: "))
    if primitive_check(G, P, l) == -1:
        print(f"Number is not a primitive root of {P}. Please try again!")
        continue
    break

# Private Keys
x1, x2 = int(input("Enter the private key of Alice: ")), int(
    input("Enter the private key of Bob: "))

while 1:
    if x1 >= P or x2 >= P:
        print(f"Private keys of both users should be less than {P}!")
        continue
    break

# Adversary intercepts key exchange
y1_mitm, y2_mitm = pow(G, x1) % P, pow(G, x2) % P

# Mallory generates secret keys
k1_mitm, k2_mitm = pow(y2_mitm, x1) % P, pow(y1_mitm, x2) % P

# Calculate Public Keys for Alice and Bob
y1, y2 = pow(G, x1) % P, pow(G, x2) % P

# Generate Secret Keys for Alice and Bob
k1, k2 = pow(y2, x1) % P, pow(y1, x2) % P

print(f"\nSecret Key for Alice is {k1}\nSecret Key for Bob is {k2}\n")

if k1 == k2:
    print("Keys have been exchanged successfully.\n")

    while True:
        # Alice sends a message to Bob
        message_from_alice = input("Alice, enter the message to be transmitted to Bob: ")
        encrypted_message_from_alice = encrypt(message_from_alice, k1_mitm)
        print(f"Encrypted Message from Alice to Bob: {encrypted_message_from_alice}")

        # Mallory (MITM) intercepts the encrypted message
        intercepted_message = encrypted_message_from_alice

        # Bob receives and decrypts the intercepted message from Alice
        decrypted_message_from_alice = decrypt(intercepted_message, k2)
        print(f"Decrypted Message from Alice to Bob (Intercepted by Mallory): {decrypted_message_from_alice}\n")

        # Bob sends a message to Alice
        message_from_bob = input("Bob, enter the message to be transmitted to Alice: ")
        encrypted_message_from_bob = encrypt(message_from_bob, k2_mitm)
        print(f"Encrypted Message from Bob to Alice: {encrypted_message_from_bob}")

        # Mallory (MITM) intercepts the encrypted message
        intercepted_message = encrypted_message_from_bob

        # Alice receives and decrypts the intercepted message from Bob
        decrypted_message_from_bob = decrypt(intercepted_message, k1)
        print(f"Decrypted Message from Bob to Alice (Intercepted by Mallory): {decrypted_message_from_bob}\n")

else:
    print("Keys have not been exchanged successfully.")
