# whether a postive integer is a prime number or not
n = int(input("Enter a positive integer: "))
if n>1:
    for i in range(2,n):
        if(n%i==0):
            print(f"{n} is not a prime number")
            break
        else:
            print(f"{n} is a prime number")
            break