class BankAccount:
    def __init__(self,name,balance):
        self.__balance=balance
        self.name=name
    @property
    def balance(self):
        return self.__balance
    @property
    def detail(self):
        return f"{self.name} your balance is {self.__balance}"
class SavingsAccount(BankAccount):
    def add_interest(self,rate):
        interest=self.balance*rate
        return self.balance + interest

Akash = SavingsAccount("Akash",1000)
print(Akash.detail)
print(Akash.add_interest(0.05))

