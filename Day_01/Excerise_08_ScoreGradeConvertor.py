## Create a program which make the score grade convertor. The program should take the marks as input and print the grade 
marks = int(input("Enter the marks: "))
if(marks >=90):
    print(f"Grade A")
elif(marks>=80):
    print(f"Grade B")
elif(marks>=70):
    print(f"Grade C")
elif(marks>=60):
    print("Grade D")
else:
    print("Grade F")