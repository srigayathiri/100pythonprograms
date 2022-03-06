# program to print armstrong number in an interval

start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))


for num in range(start, end+1):
    temp = num
    sum1 = 0
    order = len(str(num))
    while temp > 0:
        digit = temp % 10
        sum1 = sum1 + digit ** order
        temp = temp // 10
    if num == sum1:
        print(sum1)



