class Atm(object) :
    def __init__(self,cardNumber,pinNumber) :
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
    def cashWithdrawal(self) :   
        print("Cash Withdrawn")
    def BalanceEnquiry(self) :
        print("Enquiry")
    def cashDeposit(self):
        print("Cash Deposited")
    def refund(self) :
        print("Refunded")
UnionBank = Atm("123", "1801")
print (UnionBank.refund())