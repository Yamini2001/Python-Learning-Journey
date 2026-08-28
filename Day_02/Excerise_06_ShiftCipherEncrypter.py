## Write a program that prompts the user for a text string and a shift integer, and encrypts the text using a Caesar cipher.

text = input("Enter text: ")
shift = int(input("Enter shift: "))

ans = ""

for c in text:
    if c.isupper():
        # Shift uppercase letters
        new_c = chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        ans += new_c
    elif c.islower():
        # Shift lowercase letters
        new_c = chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        ans += new_c
    else:
        # Keep spaces and symbols unchanged
        ans += c

print(ans)