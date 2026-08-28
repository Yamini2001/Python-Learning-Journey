main_str = input("Enter main string: ")
sub_str = input("Enter substring: ")

count = 0
main_len = len(main_str)
sub_len = len(sub_str)

# Loop through the main string
for i in range(main_len - sub_len + 1):
    # Slice a piece of main_str that is the same size as sub_str
    if main_str[i : i + sub_len] == sub_str:
        count += 1

print(count)