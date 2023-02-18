
class Bank_Account:
    Bank_Name = "HDFC bank PVT LTD"
    ROI_On_FD = 6.7
    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0

    def CreateAccount(self):
        print("Enter your name :")
        self.Name = input()

        print("Enter your initial Ammount :")
        self.Amount = int(input())

        print("Enter your Address :")
        self.Address = input()

        print("Enter your Account Number :")
        self.AccountNo = int(input())

    def DisplayAccountInfo(self):
        print("__________________Your Account Information is as Below_______________")
        print("Name of Account Holder :",self.Name)
        print("Address of Account Holder :",self.Address)
        print("Account Number :",self.AccountNo)
        print("current Amount in Account :",self.Amount)

    @classmethod
    def DisplayBankInformation(cls):
        print("Welcome to banking consol")
        print("Name of our bank is :",cls.Bank_Name)
        print("Rate of interest we offer on fixed deposite is :",cls.ROI_On_FD)

    @staticmethod
    def DisplayKYCInfo():
        print("Please consider below KYC information")
        print("According to the rules of Govt of India u have to submit below Documents")
        print("1 : clear and recent pass size photo")
        print("2 : Photo of Aadhar")
        print("3 : Photo of PAN card")

    def Deposite(self,value):
        self.Amount = self.Amount + value

    def Withdraw(self,value):
        self.Amount = self.Amount - value
def main():
    Bank_Account.DisplayKYCInfo()

    print("Name of bank:",Bank_Account.Bank_Name)
    print("Rate of Interest on Fixed deposite:",Bank_Account.ROI_On_FD)

    Bank_Account.DisplayBankInformation()

    User1 = Bank_Account()
    User2 = Bank_Account()

    User1.CreateAccount()
    User2.CreateAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()

    User1.Deposite(500)
    User2.Deposite(1200)

    print("Amount of {} after deposite is {} :".format(User1.Name,User1.Amount))
    print("Amount of {}  after deposite is {} :".format(User2.Name,User2.Amount))

    User1.Withdraw(200)
    User2.Withdraw(3000)

    print("Amount of {}  after Withdrawal is {}:".format(User1.Name, User1.Amount))
    print("Amount of {}  after Withdraw is {} :".format(User2.Name, User2.Amount))

if __name__ == "__main__":
    main()