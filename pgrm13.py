# program to find largest among three numbers

number_1 = int(input("Enter the number 1 : "))
number_2 = int(input("Enter the number 2 : "))
number_3 = int(input("Enter the number 3 : "))

if number_1 > number_2 and number_1 > number_3:
    print(f"{number_1} is the largest number")
elif number_2 > number_3:
    print(f"{number_2} is the largest number")
else:
    print(f"{number_3} is the largest number")