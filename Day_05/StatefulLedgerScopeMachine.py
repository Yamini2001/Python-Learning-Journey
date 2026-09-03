AUDIT_TRANSACTION_COUNT = 0


def create_bank_account(owner_name, initial_balance):

    # Local variables
    balance = float(initial_balance)

    history = [
        f"Account created with {balance}"
    ]


    # Nested function: Deposit
    def deposit(amount):

        nonlocal balance
        nonlocal history
        global AUDIT_TRANSACTION_COUNT

        balance += amount

        history.append(f"deposit {amount}")

        AUDIT_TRANSACTION_COUNT += 1


    # Nested function: Withdraw
    def withdraw(amount):

        nonlocal balance
        nonlocal history
        global AUDIT_TRANSACTION_COUNT

        if balance >= amount:

            balance -= amount

            history.append(f"withdraw {amount}")

            AUDIT_TRANSACTION_COUNT += 1

        else:

            raise ValueError("Insufficient balance")


    # Nested function: Get Statement
    def get_statement():

        return (
            owner_name,
            balance,
            history.copy()
        )


    # Return dictionary containing functions
    return {
        "deposit": deposit,
        "withdraw": withdraw,
        "statement": get_statement
    }