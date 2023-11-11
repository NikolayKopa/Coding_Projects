class Bank():
    def __init__(self, fname, lname, access_code, balance):
        self.fname = fname
        self.lname = lname
        self.__access_code = access_code
        self.balance = int(balance)

    @property
    def full_name(self):
        return(self.fname + " " + self.lname)

    @full_name.setter
    def full_name(self, fn):
        first_name, last_name = fn.split(" ")
        self.fname = first_name
        self.lname = last_name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 100:
            raise Exception ("You can't withdraw from a bank account with less than 100 dollars.")
        else:
            self._balance = value

    def Withdrawal(self, inputted_ac):
        if inputted_ac == self.__access_code:
            withdrawal_amount = int(input("What amount would you like to withdraw?: $"))
            self._balance -= withdrawal_amount
            return "The balance after your withdrawal is (${}): ${}".format(withdrawal_amount, self.balance)
        else:
            return "You can't withdraw from a bank account that is not yours."

person1 = Bank("Nikolay", "Kopaliani", 6092, 430)
print(person1.fname)
print(person1.lname)
print(person1.full_name)

print(person1.balance)
print(person1.Withdrawal(320))
