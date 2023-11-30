class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

class ATM:
    def __init__(self, user_account):
        self.user_account = user_account

    def withdraw(self, amount):
        if amount > 0 and amount <= self.user_account.balance:
            self.user_account.balance -= amount
            return f"Withdrawal successful. Remaining balance: {self.user_account.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds."

    def deposit(self, amount):
        if amount > 0:
            self.user_account.balance += amount
            return f"Deposit successful. New balance: {self.user_account.balance}"
        else:
            return "Invalid deposit amount."

    def check_balance(self):
        return f"Current balance: {self.user_account.balance}"

# Example Usage:
user_account = BankAccount(balance=1000)
atm_machine = ATM(user_account)

print(atm_machine.check_balance())  # Output: "Current balance: 1000"
print(atm_machine.withdraw(500))    # Output: "Withdrawal successful. Remaining balance: 500"
print(atm_machine.deposit(200))     # Output: "Deposit successful. New balance: 700"
print(atm_machine.check_balance())  # Output: "Current balance: 700"
print(atm_machine.withdraw(1000))   # Output: "Invalid withdrawal amount or insufficient funds."
