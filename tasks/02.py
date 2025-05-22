class BankAccount():
    def __init__ (self,acc_holder,initialbalance):
        self.acc_holder=acc_holder
        self.__initialbalance = initialbalance
    def deposit(self):
        try:
            amount=float(input("Enter the amount u want to deposit : "))
            if amount > 0:
                self.__initialbalance += amount 
                print(f"{self.acc_holder} RS:{amount} are deposited")
            else:
                print("Amount should be positive")
        except ValueError:
            print("Please enter a valid number")
        
    def withdraw(self):
        try:
            amo=float(input("Enter the amount you want to withdraw : "))
            if amo > self.__initialbalance:
                print ("you dont have enough balance in your account")
            elif amo <= 0:
                print("Amount should be positive.")
            else:
                self.__initialbalance -= amo
                print(f"you withdraw RS:{amo} successfully")
                
        except ValueError:
            print("enter valid number")
            
    def get_balance(self):
        return self.__initialbalance
    
    def set_balance(self,new_amount):
        if new_amount >= 0:
            self.__initialbalance = new_amount
            print(f"Balance set to Rs:{new_amount}")
        else:
            print("Invalid amount. Balance must be non-negative.")

        
acc1=BankAccount("Sara",1000)
acc1.deposit()
print (acc1.acc_holder, " your current balance is:",acc1.get_balance())
acc1.withdraw()
print (acc1.acc_holder, " Now your current balance is:",acc1.get_balance())
acc1.set_balance(30000)
print (acc1.acc_holder, " Now your current balance is:",acc1.get_balance())

