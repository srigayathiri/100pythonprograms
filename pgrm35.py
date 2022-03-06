# program to convert decimal to binary

def binary(n):
    if n==0:
        return n
    else:
        binary(int(n/2))
        print(n%2,end="")


n = int(input("Enter a number : "))
binary(n)

