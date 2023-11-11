import datetime
class Bank():
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.__balance = int(balance)
        self.banktransactions = []
    def Transaction_Details(self, amount, transaction_type):
        transaction_date = datetime.datetime.now().strftime("%c")
        self.banktransactions.extend([transaction_date, amount, transaction_type])
    def Withdrawal(self, withdrawal_amount, given_account):
        self.Transaction_Details(withdrawal_amount, "Deposit")
        if int(given_account) == int(self.account_number):
            self.__balance -= int(withdrawal_amount)
            return "Account Balance After Withdrawal (${}): ${}".format(withdrawal_amount, self.__balance)
        else:
            return "You are not allowed to withdraw from this account since it is not yours."
    def Deposit(self, deposit_amount):
        self.Transaction_Details(deposit_amount, "Withdraw")
        self.__balance += int(deposit_amount)
        return "Account Balance After Deposit (${}): ${}".format(deposit_amount, self.__balance)

person = Bank("Nick", "1024", "250")
print(person.Withdrawal("50", "1024"))
print(person.Deposit("70"))
print(person.Deposit("800"))
print(person.Withdrawal("325", "1024"))
print("Transaction Details: \n", person.banktransactions)
