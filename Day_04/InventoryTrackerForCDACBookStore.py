
def manage_bookstore_inventory(inventory, action, book_title, quantity=0):
    if action == "add":
        if book_title in inventory:
            inventory[book_title] += quantity
        else:
            inventory[book_title] = quantity
            
    elif action == "sell":
        if book_title not in inventory:
            print(f"Error: Book '{book_title}' not found in inventory.")
        elif inventory[book_title] < quantity:
            print(f"Error: Insufficient stock for '{book_title}'. Available: {inventory[book_title]}")
        else:
            inventory[book_title] -= quantity
            if inventory[book_title] == 0:
                del inventory[book_title]
                
    elif action == "lookup":  # Fixed: Shifted outwards to be its own independent branch
        return inventory.get(book_title, 0)
        
    return inventory

inventory = {"Python Basics": 10, "Learning AI": 5}
inventory = manage_bookstore_inventory(inventory, "add", "Python Basics", 5)
print(f"Inventory: {inventory}")

# inventory = {"Python Basics": 10, "Learning AI": 5}
inventory = manage_bookstore_inventory(inventory, "sell", "Data Science 101", 1)
print(f"Error: Book 'Data Science 101' not found in inventory. {inventory}")

inventory = manage_bookstore_inventory(inventory, "sell", "Learning AI", 10)
print(f"Inventory after selling 'Learning AI': {inventory}")

inventory = manage_bookstore_inventory(inventory, "sell", "Learning AI", 5)
print(f"Inventory after selling 'Learning AI': {inventory}")