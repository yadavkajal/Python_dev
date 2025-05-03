class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
    def debit(self,amount):
        self.balance-=amount
        print("RS. ", amount, "is debited from your account ",self.account_no)
        print("total balance = ",self.getbalance())
    def credit(self,amount):
        self.balance+=amount
        print("RS. ", amount, "is credited to your account ",self.account_no)
        print("total balance = ",self.getbalance())
    def getbalance(self):
        return self.balance
acc=Account(10000,12345)
acc.debit(2000)
acc.credit(1300)
acc.credit(5000)
acc.debit(200)
