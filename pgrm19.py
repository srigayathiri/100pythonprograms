# program to check whether a number is armstrong number

num = int(input("Enter a number : "))

sum = 0
temp = num
order = len(str(temp))

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** order
    temp = temp//10

if num == sum:
    print("It is a amstrong number")
else:
    print("It is not an amstrong number")
