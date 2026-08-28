text = input("Enter a string: ")

# Handle empty input
if not text:
    print("")
else:
    ans = ""
    count = 1

    # Loop through string starting from the second character
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            # Same character as before, increase count
            count += 1
        else:
            # Different character, save previous character and its count
            ans += text[i - 1] + str(count)
            count = 1

    # Add the last character and its count
    ans += text[-1] + str(count)

    # Print compressed version only if it is shorter than original
    if len(ans) < len(text):
        print(ans)
    else:
        print(text)