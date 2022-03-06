# program to calculate sum of natural numbers using recursion

def compute_sum(n):
    if n<=1:
        return n
    else:
        return n + compute_sum(n-1)


num = int(input("Enter a number : "))
if num == 0:
    print("Enter a positive number")
else:
    print(f"Sum of {num} natural numbers is : {compute_sum(num)}")
