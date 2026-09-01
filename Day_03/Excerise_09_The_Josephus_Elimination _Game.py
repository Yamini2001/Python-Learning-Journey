no_of_soldier = int(input("Enter the number of soldiers: "))
elimination_interval = int(input("Enter the elimination interval: "))
no_of_soldier_list = list(range(1,no_of_soldier+1))
print("Soldiers circle initialized:",no_of_soldier_list)
index = 0
while(len(no_of_soldier_list)>1):
    index = (index + elimination_interval -1) % len(no_of_soldier_list)
    eliminated_soldier = no_of_soldier_list.pop(index)
    print(f"Eliminated soldier: {eliminated_soldier} (Remaining: {no_of_soldier_list})")
print(f"The sole survivor is: {no_of_soldier_list[0]}")
