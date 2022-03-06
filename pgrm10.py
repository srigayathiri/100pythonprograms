# program to check a number is positive, negative or zero

number = int(input("Enter a number: "))


if number < 0:
    print(f"{number} is negative number")
elif number > 0:
    print(f"{number} is positive number")
else:
    print(f"{number} is zero")
    