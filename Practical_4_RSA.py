import random 

def gcdByEuclideanMethod(a, b):
    return a if b == 0 else gcdByEuclideanMethod(b, a%b)

def encryptMessage(message, e, n):
	cipher = (message ** e) % n
	return cipher

def decryptMessage(cipher, d, n):
	plain = (cipher ** d) % n
	return plain 

if __name__ == '__main__':
	p = int(input("Enter value for p (must be prime) : "))
	q = int(input("Enter value for q (must be prime) : "))
	n = p * q
	phi_n = (p-1) * (q-1)
	e = [i for i in range(3, phi_n, 2) if gcdByEuclideanMethod(phi_n, i) == 1]
	e = e[random.randint(0, len(e))]
	d = [i for i in range(3, phi_n) if (i * e) % phi_n == 1]
	d = d[random.randint(0, len(d)-1)]
	# print(e, d)
	message = int(input("Enter a message : "))
	cipher = encryptMessage(message, e, n)
	decrypted = decryptMessage(cipher, d, n)
	# print("Public key <{}, {}> \nPrivate key <{}, {}>".format(e, n, d, n))
	print("Original message was {:15}\nEncrypted Message is {:15}\nDecrypted message is {:15}".format(message, cipher, decrypted))
