# whether a postive integer is a prime number or not
user = int(input("Enter the positive integer: "))
i = 2
if(user<=1):
    print("Not a prime")
else:
    for i in range(1,user,1):
        if(user%i==0):
            print("Prime")
        break
            
