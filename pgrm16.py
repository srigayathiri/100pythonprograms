# program to find a factorial of a number

number = int(input("Enter a number : "))


def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num-1)


factorial = fact(number)
print(f"{number} factorial is {factorial}")
