# program to make a simple calculator

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b


print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:
    choice = int(input("Enter your choice (1/2/3/4) : "))
    a = int(input("Enter the first number : "))
    b = int(input("Enter the second number : "))
    if choice in (1,2,3,4):
        if choice == 1:
            print(f"Addition of {a} and {b} is {add(a,b)}")
        elif choice == 2:
            print(f"Subtraction of {a} and {b} is {sub(a,b)}")
        elif choice == 3:
            print(f"Multiplication of {a} and {b} is {mul(a,b)}")
        else:
            print(f"Division of {a} and {b} is {div(a,b)}")
    else:
        print("Invalid input")
    end = input("Do you want to make other calculations (Yes/No)").upper()
    if end == "NO":
        break
