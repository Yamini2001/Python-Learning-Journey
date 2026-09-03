def calculate_cafeteria_bill(base_price, *items, tax_rate=0.05, discount=0.0, delivery_fee=0.0):
    """
    Calculates the final cafeteria bill using variable positional arguments 
    for side items and keyword-only parameters for taxes, discounts, and fees.
    """
    # Step 1: Calculate raw subtotal by adding main meal and all side items
    raw_subtotal = base_price + sum(items)
    
    # Step 2: Apply the discount percentage to the raw subtotal
    discount_multiplier = 1 - (discount / 100)
    discounted_subtotal = raw_subtotal * discount_multiplier
    
    # Step 3: Calculate tax based on the new discounted subtotal
    tax_amount = discounted_subtotal * tax_rate
    
    # Step 4: Add everything together (discounted subtotal + tax + delivery flat fee)
    final_total = discounted_subtotal + tax_amount + delivery_fee
    
    # Step 5: Round to 2 decimal places and return the value
    return round(final_total, 2)


# ==========================================
# Verification Checks (Using your test cases)
# ==========================================
if __name__ == "__main__":
    print("--- Running Test Case 1 ---")
    # Standard meal, no sides, default tax, no discount, no delivery
    total1 = calculate_cafeteria_bill(100.0)
    print(f"Test 1 Result: {total1}")  # Expected: 105.0
    
    print("\n--- Running Test Case 2 ---")
    # Meal with sides, custom tax rate, 10% discount, flat delivery fee
    total2 = calculate_cafeteria_bill(100.0, 20.0, 30.0, tax_rate=0.08, discount=10.0, delivery_fee=15.0)
    print(f"Test 2 Result: {total2}")  # Expected: 160.8
