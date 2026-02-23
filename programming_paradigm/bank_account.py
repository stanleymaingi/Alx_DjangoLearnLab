class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional starting balance."""
        self.__account_balance = initial_balance  # private attribute

    def deposit(self, amount):
        """Add the specified amount to the balance."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deduct the amount if sufficient funds are available."""
        if amount > 0:
            if self.__account_balance >= amount:
                self.__account_balance -= amount
                return True
            else:
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """Print the current balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
