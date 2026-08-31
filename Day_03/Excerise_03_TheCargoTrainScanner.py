# The Cargo Train Scanner

resources = ["coal", "iron", "gold", "coal", "timber", "coal"]
resources_type = str(input("Enter a resource type: "))
value = resources.count(resources_type)
print(f"Number of coal wagons:{value}")
if resources_type in resources:
    value1 = resources.index(resources_type)
    print(f"First coal wagon is at index: {value1}")
else:
    print("Resource not found on train!")