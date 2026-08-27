## Enter the value of year and check whether it is a leap year or not.
year = int(input("Enter the year: "))
if year%4==0 and (year%100!=0 or year%400==0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")