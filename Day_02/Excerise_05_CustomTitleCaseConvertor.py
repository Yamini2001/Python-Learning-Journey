## Create a program accepts a string from the user and converts it into title case. 
user = input("Enter a string: ")

# Step 1: Split the sentence into individual words
words = user.split()

title_cased_words = []

# Step 2: Loop through each word and format it
for word in words:
    # Capitalize 1st letter, lowercase the rest using slicing
    formatted_word = word[0].upper() + word[1:].lower()
    title_cased_words.append(formatted_word)

# Step 3: Join the formatted words back with spaces
result = " ".join(title_cased_words)

print(result)