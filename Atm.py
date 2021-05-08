class Atm:
    def __init__(self, atm_card_number, pin_number):
        self.atm_card_number = atm_card_number
        self.pin_number = pin_number
    
    def check_balance(self):
        print("Your balnce is 50,000")

    def CashWithDrawal(self, amount):
        new_amount = 50000 - amount
        print("You have withdrawn amount is " + str(amount))
        print(" Your remaining balance is " + str(new_amount))


def main():
    atm_card_number = input("Insert your card number; ")
    pin_number = input("Enter your pin number: ")    
    new_user = Atm(atm_card_number, pin_number)
    print("Choose your activity: ")
    print("1. Balance inquiry 2. Widthdrwal")
    activity = int(input("Enter activity number: "))
    
    if activity == 1:
        new_user.check_balance()
    elif activity == 2:
        amount = int(input("Enter the amount: "))
        new_user.CashWithDrawal(amount)
    else:
        print("Enter a valid number.")

if __name__ == "__main__":
    main()
