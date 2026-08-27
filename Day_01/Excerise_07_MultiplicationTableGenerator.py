## Create a program generate the input from the user and print the multiplication table of that number
n = int(input("Enter the value of n: "))
for i in range(1,n+1):
    print(f"{n} * {i} = {n*i}")