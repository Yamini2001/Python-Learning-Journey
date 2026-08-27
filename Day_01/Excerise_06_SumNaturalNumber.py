## Create a program generate the input from the user and calculate sum of n natural number
n = int(input("Enter the value of n: "))
sum = 0
for i in range(1,n+1):
    sum+=i
print(f"The sum of {n} natural number is {sum}")