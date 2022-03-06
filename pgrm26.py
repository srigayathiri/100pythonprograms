# program to find gcd or hcf of two numbers

def compute_gcd(a,b):
    if b == 0:
        return a
    else:
        return compute_gcd(b,a%b)


a = int(input("Enter the first value : "))
b = int(input("Enter the second value : "))
print(f"GCD of {a} and {b} is {compute_gcd(a,b)}")


