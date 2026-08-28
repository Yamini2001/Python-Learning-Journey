## Write a program that enter an email address and extracts the domain name from it.
user = str(input("Enter an email address:"))


if(user.count('@')==1):
    parts = user.split('@')
    domain = parts[1]
    
    # Optional check: Ensure the domain isn't empty (e.g., "user@")
    if domain != "":
        print(domain)
    else:
        print("Invalid Email")
else:
    print("Invalid Email")
