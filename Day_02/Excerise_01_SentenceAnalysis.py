## Write a program that enter a sentence and countsthe number of words in the sentence. 
user = str(input("Enter a sentence: "))

print("The number of characters in the sentence is:", len(user))
print("The number of words in the sentence is:", len(user.split()))