import hashlib

string_input = input("Enter String: ")


result = hashlib.md5(string_input.encode())
print("MD5 Hash object: ",result)

print("Hexadecimal String: ",result.hexdigest())