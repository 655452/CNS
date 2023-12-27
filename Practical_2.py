def AndOperation(s: str):
    return [(ord(i) & 127) for i in s]

def XorOperation(s: str):
    return [(ord(i) ^ 127) for i in s]

def orOperation(s: str):
    return [(ord(i) | 127) for i in s]

if __name__ == "__main__":
    string = "Hello World"
    print("AND : ", AndOperation(string) ," Characters : ", "".join(chr(i) for i in AndOperation(string)))
    print("OR : ", orOperation(string)," Characters : ", "".join(chr(i) for i in orOperation(string)))
    print("XOR : ", XorOperation(string))



