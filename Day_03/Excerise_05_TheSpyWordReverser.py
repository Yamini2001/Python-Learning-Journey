# The Spy Word Reverser
sentence = str(input("Enter the sentence you want to reverse: "))
sentence1 = sentence.split()
print(sentence1)
reverse_word = [word[::-1] for word in sentence1]
print(reverse_word)
sentence2 = " ".join(reverse_word)
print(sentence2)

    
