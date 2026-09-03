# ==========================================
# Custom Exception Definitions
# ==========================================
class ProductNotFoundError(Exception):
    """Raised when a product ID is not present in the catalog."""
    pass


class OutOfStockError(Exception):
    """Raised when the ordered quantity exceeds available stock."""
    pass


# ==========================================
# Order Processing Function
# ==========================================
def process_order(catalog, order):
    """
    Processes an e-commerce order atomically.
    
    Validation Phase: Verifies all items exist and have sufficient stock.
    Execution Phase: Deducts stock and returns total cost only if validation succeeds.
    """
    # --- VALIDATION PHASE ---
    # 1. Check if all ordered products exist in the catalog
    for product_id in order:
        if product_id not in catalog:
            raise ProductNotFoundError(f"Product '{product_id}' not found in store catalog.")

    # 2. Check if the catalog contains sufficient stock for each item ordered
    for product_id, requested_qty in order.items():
        available_stock = catalog[product_id]["stock"]
        if requested_qty > available_stock:
            raise OutOfStockError(
                f"Product '{product_id}' is out of stock. "
                f"Requested: {requested_qty}, Available: {available_stock}."
            )

    # --- EXECUTION PHASE ---
    total_cost = 0.0

    # Since all items passed validation, we can safely update the inventory
    for product_id, requested_qty in order.items():
        # Deduct the ordered quantity from catalog stock
        catalog[product_id]["stock"] -= requested_qty
        
        # Accumulate total cost
        total_cost += catalog[product_id]["price"] * requested_qty

    return total_cost


# ==========================================
# Example Walkthrough / Verification
# ==========================================
if __name__ == "__main__":
    # Initial setup matching the scenario description
    catalog = {
        "P01": {"price": 10.0, "stock": 5},
        "P02": {"price": 20.0, "stock": 10}
    }

    print("Initial Catalog:")
    print(catalog)
    print("-" * 50)

    # 1. Successful Order
    print("Executing Successful Order: {'P01': 2, 'P02': 1}")
    total = process_order(catalog, {"P01": 2, "P02": 1})
    print(f"Returned Total Cost: {total}") 
    print("Catalog after successful order:")
    print(catalog)
    print("-" * 50)

    # 2. Failed Order (Triggers Rollback simulation)
    # Expected: P01 should stay at 3, P02 should stay at 9 despite P01 being valid in isolation.
    print("Executing Failed Order (Insufficient P02 Stock): {'P01': 2, 'P02': 15}")
    try:
        total = process_order(catalog, {"P01": 2, "P02": 15})
    except OutOfStockError as e:
        print(f"Caught Expected Error: {e}")

    print("\nVerifying Catalog Stock after Failure (Atomicity Check):")
    print(f"P01 Stock: {catalog['P01']['stock']} (Must be 3)")
    print(f"P02 Stock: {catalog['P02']['stock']} (Must be 9)")
    print("-" * 50)

    # 3. Failed Order (Product Not Found)
    print("Executing Failed Order (Missing Product ID): {'P99': 1}")
    try:
        total = process_order(catalog, {"P99": 1})
    except ProductNotFoundError as e:
        print(f"Caught Expected Error: {e}")
