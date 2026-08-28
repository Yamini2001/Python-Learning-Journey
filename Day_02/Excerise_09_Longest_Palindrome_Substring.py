text = input("Enter a string: ")

longest = ""

# Loop through every possible starting position
for i in range(len(text)):
    # Loop through every possible ending position
    for j in range(i + 1, len(text) + 1):
        
        # Cut out a piece of the string
        sub = text[i:j]
        
        # Check if this piece reads the same forwards and backwards
        if sub == sub[::-1]:
            # If it is a palindrome AND longer than our previous best, save it
            if len(sub) > len(longest):
                longest = sub

print(longest)