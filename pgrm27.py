# program to find LCM of two numbers

def compute_lcm(a,b):
    if a>b:
        higher = a
    else:
        higher = b
    value = higher
    while True:
        if higher%a==0 and higher%b==0:
            print(f"LCM of {a} and {b} is {higher}")
            break
        else:
            higher = higher + value


a = int(input("Enter the first value : "))
b = int(input("Enter the second value : "))
compute_lcm(a,b)