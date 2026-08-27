## code on fibonnaci sequence generator
n = int(input("Enter the value of n:"))
a ,b=0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
