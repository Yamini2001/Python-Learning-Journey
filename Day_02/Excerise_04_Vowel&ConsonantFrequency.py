user = input("Enter the string: ")

# Dictionary to store individual frequency of each vowel
vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
consonants = 0

# Convert string to lowercase to make it case-insensitive
for char in user.lower():
    if char.isalpha():  
        if char in vowels:
            vowels[char] += 1
        else:
            consonants += 1

# Display results
print("Vowel Frequencies:")
for vowel, count in vowels.items():
    print(f"{vowel}: {count}")

print(f"Total Consonants: {consonants}")