# program to print fibonacci series

limit = int(input("Enter the limit of fibonacci series : "))


def fibonacci():
    n1 = 0
    n2 = 1
    while True:
        yield n1
        n1, n2 = n2, n1+n2


seq = fibonacci()
for i in range(limit):
    print(next(seq))
