# Grading on a curve 

test_scores = input("Enter the test scores separated by spaces: ").split()
integers = [int(score) for score in test_scores]
curved_scores = [
    min(100,score+10) if score < 50 else min(100,score+5)
    for score in integers
]
print("Original scores:",integers)
print("Curved:",curved_scores)
