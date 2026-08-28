date_str = input("Enter date (DD/MM/YYYY): ").strip()

months = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)

try:
    # Step 1: Split string by '/'
    parts = date_str.split("/")
    
    if len(parts) != 3:
        print("Invalid Date")
    else:
        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])

        # Step 2: Validate month range
        if month < 1 or month > 12:
            print("Invalid Date")
        else:
            # Step 3: Check for leap year
            is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

            # Step 4: Find maximum valid days for the month
            if month in [4, 6, 9, 11]:
                max_days = 30
            elif month == 2:
                max_days = 29 if is_leap else 28
            else:
                max_days = 31

            # Step 5: Validate day range
            if day < 1 or day > max_days:
                print("Invalid Date")
            else:
                # Step 6: Convert month number to month name
                month_name = months[month - 1]
                print(f"{month_name} {day:02d}, {year}")

except ValueError:
    print("Invalid Date")