

class Bank:
    bank_name= "FaysalBank"
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
        return new_name
    
bank1=Bank
print ("original name:",Bank.bank_name)
Bank.change_bank_name("Meezan")
print("new name:",bank1.bank_name)



