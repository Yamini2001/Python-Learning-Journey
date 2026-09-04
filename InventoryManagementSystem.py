products = []
next_id = 1


# ---------------- ADD PRODUCT ----------------

def add_product():

    global next_id

    while True:

        name = input("Enter product name: ").strip()

        if name != "":
            break

        print("Name cannot be empty!")

    while True:

        category = input("Enter product category: ").strip()

        if category != "":
            break

        print("Category cannot be empty!")

    while True:

        try:

            price = float(input("Enter product price: "))

            if price > 0:
                break

            print("Price must be greater than 0!")

        except ValueError:

            print("Invalid input! Enter a valid price.")

    while True:

        try:

            quantity = int(input("Enter product quantity: "))

            if quantity >= 0:
                break

            print("Quantity cannot be negative!")

        except ValueError:

            print("Invalid input! Enter a valid quantity.")

    product = {

        "id": next_id,
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity

    }

    products.append(product)

    print("Product added successfully!")

    next_id += 1


# ---------------- VIEW PRODUCT ----------------

def view_products():

    if not products:

        print("No products available!")
        return

    print("\n----- ALL PRODUCTS -----")

    for product in products:

        print(f"ID: {product['id']}")
        print(f"Name: {product['name']}")
        print(f"Category: {product['category']}")
        print(f"Price: {product['price']}")
        print(f"Quantity: {product['quantity']}")

        print("-" * 30)


# ---------------- SEARCH PRODUCT ----------------

def search_product():

    print("\n1. Search by ID")
    print("2. Search by Name")

    choice = input("Enter your choice: ")

    if choice == "1":

        try:

            product_id = int(input("Enter product ID: "))

            for product in products:

                if product["id"] == product_id:

                    print("\nProduct Found!")
                    print(product)

                    return

            print("Product not found!")

        except ValueError:

            print("Invalid ID!")

    elif choice == "2":

        name = input("Enter product name: ").strip().lower()

        found = False

        for product in products:

            if name in product["name"].lower():

                print("\nProduct Found!")
                print(product)

                found = True

        if not found:

            print("Product not found!")

    else:

        print("Invalid choice!")


# ---------------- UPDATE PRODUCT ----------------

def update_product():

    try:

        product_id = int(input("Enter product ID to update: "))

    except ValueError:

        print("Invalid ID!")

        return

    for product in products:

        if product["id"] == product_id:

            while True:

                name = input("Enter new name: ").strip()

                if name != "":

                    product["name"] = name

                    break

                print("Name cannot be empty!")

            while True:

                category = input("Enter new category: ").strip()

                if category != "":

                    product["category"] = category

                    break

                print("Category cannot be empty!")

            while True:

                try:

                    price = float(input("Enter new price: "))

                    if price > 0:

                        product["price"] = price

                        break

                    print("Price must be greater than 0!")

                except ValueError:

                    print("Invalid price!")

            while True:

                try:

                    quantity = int(input("Enter new quantity: "))

                    if quantity >= 0:

                        product["quantity"] = quantity

                        break

                    print("Quantity cannot be negative!")

                except ValueError:

                    print("Invalid quantity!")

            print("Product updated successfully!")

            return

    print("Product not found!")


# ---------------- DELETE PRODUCT ----------------

def delete_product():

    try:

        product_id = int(input("Enter product ID to delete: "))

    except ValueError:

        print("Invalid ID!")

        return

    for product in products:

        if product["id"] == product_id:

            products.remove(product)

            print("Product deleted successfully!")

            return

    print("Product not found!")


# ---------------- MAIN MENU ----------------

while True:

    print("\n==========================================")
    print("   PRODUCT INVENTORY MANAGEMENT SYSTEM")
    print("==========================================")

    print("1. Add Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_product()

    elif choice == "2":

        view_products()

    elif choice == "3":

        search_product()

    elif choice == "4":

        update_product()

    elif choice == "5":

        delete_product()

    elif choice == "6":

        print("\nThank you for using Product Inventory Management System!")
        break

    else:

        print("Invalid choice! Please enter a number between 1 and 6.")