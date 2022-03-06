# program to generate a random number

import random

limit = int(input("Enter the range to generate random number : "))

random_no = random.randint(0, limit)

print(f"Random number is : {random_no}")
