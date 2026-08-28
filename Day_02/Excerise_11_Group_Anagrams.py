words = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Dictionary to hold sorted strings as keys and lists of anagrams as values
groups = {}

for word in words:
    # Sort the letters of the word to create a common key
    sorted_word = "".join(sorted(word))
    
    # If the sorted key isn't in our dictionary yet, create an empty list for it
    if sorted_word not in groups:
        groups[sorted_word] = []
        
    # Add the original word to its matching group
    groups[sorted_word].append(word)

# Convert the dictionary values into a list of lists
result = list(groups.values())

print(result)