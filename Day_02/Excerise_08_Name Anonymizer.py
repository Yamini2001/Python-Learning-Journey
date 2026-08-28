name = input("Enter full name: ")

# Split the full name into a list of words
parts = name.split()

# If the name is just a single word, print it as-is
if len(parts) <= 1:
    print(name)
else:
    # Get the first letter of every word except the last one
    initials = []
    for word in parts[:-1]:
        initials.append(word[0].upper() + ".")
        
    # Get the last word (the full last name)
    last_name = parts[-1]
    
    # Combine the initials and the last name with a space
    result = " ".join(initials) + " " + last_name
    print(result)