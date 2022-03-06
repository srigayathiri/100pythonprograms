# program to find sum of natural number

limit = int(input("Enter the limit : "))

sum_natural = limit * (limit+1)//2
print("Sum of natural numbers using formula : ",sum_natural)

sum2 = 0
for i in range(1,limit+1):
    sum2 = sum2 + i
print("Sum of natural numbers using loop : ", sum2)