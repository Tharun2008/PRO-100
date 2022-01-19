class Atm(object):
    def __init__(self,cardNumber,pinNumber,nameOnCard):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber
        self.nameOnCard=nameOnCard
    def CashWithdrawl(self):
        print("withdrawing cash")
    def BalanceEnquiry(self):
        print("***** is the amount in your account")

ATM=Atm("7689 7889 8372","3551","Tharun sundram annamallai")
print(ATM.cardNumber)
print(ATM.pinNumber)
print(ATM.nameOnCard)

ATM.CashWithdrawl()
ATM.BalanceEnquiry()


