import copy

# ==========================================
# Custom Exception Definitions
# ==========================================
class AccountNotFoundError(Exception):
    """Raised when an account ID is missing from the registry."""
    pass


class OverdraftError(Exception):
    """Raised when a withdrawal amount exceeds the account balance."""
    pass


class InvalidTransactionError(Exception):
    """Raised when the transaction type is unrecognized or amounts are non-positive."""
    pass


# ==========================================
# Transaction Processing Function
# ==========================================
def process_transaction_batch(accounts, batch_list, log_path):
    """
    Processes a batch of bank transactions atomically.
    If any transaction fails, rolls back changes and logs a [ROLLBACK] entry.
    If all succeed, applies changes and logs a [SUCCESS] entry.
    """
    # Create a deep copy of the initial state to act as a restore point
    backup_accounts = copy.deepcopy(accounts)

    try:
        # Iterate through batch_list and apply the changes inline
        for tx in batch_list:
            acc = tx.get("acc")
            tx_type = tx.get("type")
            amt = tx.get("amt")

            # 1. Check if the account exists
            if acc not in accounts:
                raise AccountNotFoundError(f"Account '{acc}' not found.")

            # 2. Check if the transaction type is valid
            if tx_type not in ("deposit", "withdraw"):
                raise InvalidTransactionError(f"Invalid transaction type '{tx_type}'.")

            # 3. Check if the amount is strictly positive
            if amt <= 0:
                raise InvalidTransactionError("Transaction amount must be positive.")

            # 4. Handle Withdrawal rules
            if tx_type == "withdraw":
                if accounts[acc] < amt:
                    raise OverdraftError(
                        f"Insufficient funds. Account {acc} has balance {accounts[acc]}, requested {amt}."
                    )
                accounts[acc] -= amt

            # 5. Handle Deposit rules
            elif tx_type == "deposit":
                accounts[acc] += amt

        # --- SUCCESS HANDLING ---
        # If the loop finishes with no exceptions, write to log using context manager
        with open(log_path, "a", encoding="utf-8") as log_file:
            log_file.write(f"[SUCCESS] Batch completed. {len(batch_list)} transaction(s) processed.\n")
        
        return accounts

    except Exception as e:
        # --- EXCEPTION HANDLING & ROLLBACK ---
        # 1. Restore the original dictionary state by clear and update
        accounts.clear()
        accounts.update(backup_accounts)

        # 2. Extract exception class name and message
        error_class_name = e.__class__.__name__
        
        # 3. Open file in append mode safely to log the aborted batch
        with open(log_path, "a", encoding="utf-8") as log_file:
            log_file.write(f"[ROLLBACK] Batch aborted: {error_class_name} - {str(e)}\n")

        # 4. Re-raise the caught exception to notify the caller
        raise e


# ==========================================
# Example Walkthrough Verification
# ==========================================
if __name__ == "__main__":
    import os

    # Setup testing data matching the scenario
    accounts = {"ACC01": 100.0, "ACC02": 50.0}
    log_file = "transactions.log"

    # Reset log file if it exists from previous runs
    if os.path.exists(log_file):
        os.remove(log_file)

    print("Initial Balances:", accounts)
    print("-" * 60)

    # --- Batch 1: Valid transactions ---
    batch_1 = [
        {"acc": "ACC01", "type": "withdraw", "amt": 30.0},
        {"acc": "ACC02", "type": "deposit", "amt": 20.0}
    ]
    
    print("Executing Batch 1 (Valid)...")
    accounts = process_transaction_batch(accounts, batch_1, log_file)
    print("Balances after Batch 1:", accounts)  # Expected: {"ACC01": 70.0, "ACC02": 70.0}
    print("-" * 60)

    # --- Batch 2: Invalid transaction (triggers rollback) ---
    batch_2 = [
        {"acc": "ACC01", "type": "deposit", "amt": 50.0},
        {"acc": "ACC02", "type": "withdraw", "amt": 200.0}  # Overdraft!
    ]
    
    print("Executing Batch 2 (Invalid - Overdraft expected)...")
    try:
        accounts = process_transaction_batch(accounts, batch_2, log_file)
    except OverdraftError as e:
        print(f"Caught expected exception: {e}")

    print("\nVerifying Rollback State:")
    # ACC01 must remain at 70.0 (the deposit of 50.0 must be undone)
    print("Balances after Batch 2 Failure:", accounts) 
    print("-" * 60)

    # --- Display written transaction log ---
    print("Contents of 'transactions.log':")
    with open(log_file, "r", encoding="utf-8") as f:
        print(f.read())
