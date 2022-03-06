# program to print prime numbers in a interval

start = int(input("Enter the starting range : "))
end = int(input("Enter the ending range : "))

for num in range(start,end+1):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)

