class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def balanceinquiry(self):
        print("Your Balance Is $100")

    def cashwidthdrawal(self, amount):
        new_amount = 100-amount
        print('You Withdrawed  :  ' + str(amount)  +  'Your Remaining Balance Is  :  '  +  str(new_amount))
    
def main():
    name = input("Hello What Is Your Name")
    print('Hello'+name)
    cardnumber = input("Insert your Card Number")
    pin = input("Enter Your Pin")
    new_user=Atm(cardnumber , pin)

    print("Chouse your activity")
    print("1. Balance Inquiry")
    print("2. Cash Withdrawal")
    activity = int(input("Enter activity choice"))

    if(activity == 1):
        new_user.balanceinquiry()
    elif (activity == 2):
        amount= int(input("Enter the Amount"))
        new_user.cashwidthdrawal(amount)
    else:
        print("Enter a vaild number")

main()