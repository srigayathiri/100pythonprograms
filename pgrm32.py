# program to display fibonacci series using recursion

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))


nterms = int(input("Enter the number of terms : "))

if nterms <= 0:
    print("Enter the positive integer")
else:
    print("Fibonacci sequence")
    for i in range(nterms):
        print(fibonacci(i))