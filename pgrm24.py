# program to convert decimal number to binary, octal, hexadecimal

decimal_number = int(input("Enter a number : "))

print(f"The decimal number {decimal_number} is equal to :")
print(f"Binary : {bin(decimal_number)}")
print(f"Octal : {oct(decimal_number)}")
print(f"Hexadecimal : {hex(decimal_number)}")