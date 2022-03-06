# program to find factorial of a number using recursion

def fact(num):
    if num == 1:
        return num
    else:
        return(num*fact(num-1))


num = int(input("Enter a number : "))
if num ==0:
    print("Enter a positive integer ")
else:
    print(f"Factorial of {num} is {fact(num)}")