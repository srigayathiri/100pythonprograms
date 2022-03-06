#program to swap two variables

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))

print("Swapping without using temp variable")

print(f"Before swapping the value of and a and b is : {a} and {b}")

a,b = b,a

print(f"After swapping the value of and a and b is : {a} and {b}\n")


print("Swapping using temp variable")

print(f"Before swapping the value of and a and b is : {a} and {b}")

temp = a
a = b
b = temp

print(f"After swapping the value of and a and b is : {a} and {b}")

