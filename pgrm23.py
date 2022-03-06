# program to find number divisible by another number

my_list = [25,35,45,55,65,21,48,5,46]


div = list(filter(lambda x: (x % 5 == 0),my_list))
print(f"Numbers that are divisible by 5 in the list is : {div}")
