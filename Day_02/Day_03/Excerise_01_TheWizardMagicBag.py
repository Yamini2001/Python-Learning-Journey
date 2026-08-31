# The Wizard's Magic Bag

bag = ["staff","potion","spellbook"]
bag1 = str(input("Enter the item you want to add to the bag: "))
print("Portal transition activated")
bag.remove("staff")
print(f"Ejected oldest item: staff")
bag.append(bag1)
print(f"Current items in the magic bag: {bag}")
