# import random
#
# def xorOperation(str1, str2):
# 	answer = ""
# 	if len(str1) != len(str2):
# 		raise ValueError("Length of both binary numbers is not equal")
# 	else:
# 		for i in range(len(str1)):
# 			if str1[i] != str2[i]:
# 				answer += "1"
# 			else:
# 				answer += "0"
# 	return answer
#
# def encryptionFunction(l, r, k):
# 	f1 = xorOperation(r, k)
#
# 	r2 = xorOperation(f1, l)
# 	l2 = r
# 	return l2, r2
#
# def decimalconversion(str1):
# 	decimal = 0
# 	j = -1
# 	for i in range(len(str1)-1, -1, -1):
# 		j += 1
# 		if(str1[i] == '1'):
# 			decimal += 2**j
#
#
# 	return decimal
#
# if __name__ == '__main__':
# 	#print(decimalconversion("1001"))
# 	characters = [char for char in "Hello"]
# 	print([bin(ord(char))[2:] for char in characters])
# 	binary_chars = "".join(["0"+bin(ord(char))[2:] for char in characters])
# 	k1 = "".join([str(random.randint(0, 1)) for i in range(len(binary_chars)//2)])
# 	k2 = "".join([str(random.randint(0, 1)) for i in range(len(binary_chars)//2)])
#
# 	print(binary_chars, len(binary_chars))
# 	l1, r1 = binary_chars[0:len(binary_chars)//2], binary_chars[len(binary_chars)//2:]
# 	print(l1, r1, len(l1), len(r1))
# 	l2, r2 = encryptionFunction(l1, r1, k1)
# 	l3, r3 = encryptionFunction(l2, r2 , k2)
# 	encrypted_string = "".join((l3, r3))
# 	encrypted_in_plain = "".join([chr(decimalconversion(encrypted_string[i:i+8])) for i in range(0, len(encrypted_string), 8)])
#
#
# 	print("Encrypted string {}".format(encrypted_in_plain))

import random

def DESWorking(binary_input: str):

	left = binary_input[:32]
	right = binary_input[32:]
		# print(left + right)
	k = random.randint(1, 42949672)
	k = format(k, '032b')
	xor = []
	for i in range(32):
		xor.append(int(right[i]) ^ int(k[i]))
	new_xor = []
	for i in range(32):
		new_xor.append(int(xor[i]) ^ int(left[i]))
	right = "".join(str(i) for i in new_xor)
	return right, left


if __name__ == "__main__":
	message = input("Enter a message (it should be 8 character long only) : ")
	binary_of_message = "".join(format(ord(i), '08b') for i in message)
	k = 0
	left = 0
	right = 0
	while k < 16:
		left, right = DESWorking(binary_of_message)
		binary_of_message = left + right
		k += 1
	total = left + right
	print("The cipher text after 16 round is : ", end=" ")
	for i in range(0, len(total), 8):
		print(chr(int(total[i:i+8], 2)), end="")
	print()


	# print(binary_of_message)





