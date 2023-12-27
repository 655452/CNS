# Write a program that combines a string with a values "Hello World " The Program should  and and  Xor  Or Each character  in this string with 127 end display result

input_string = "Hello World"
and_result = ""
or_result = ""
xor_result = ""

for char in input_string:
    # Perform AND operation with 127 on each character
    and_result += chr(ord(char) & 127)
    # Perform OR operation with 127 on each character
    or_result += chr(ord(char) | 127)
    # Perform XOR operation with 127 on each character
    xor_result += chr(ord(char) ^ 127)

print("Original String:", input_string)
print("AND Result:", and_result)
print("OR Result:", or_result)
print("XOR Result:", xor_result)
