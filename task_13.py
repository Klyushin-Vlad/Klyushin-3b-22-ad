class BankAccount:
    def __init__(self, name, account_number):
        self.balance = 0
        self.name = name
        self.account_number = account_number

    def top_up(self, number):
        self.balance += number

    def withdrawals(self, number):
        self.balance -= number