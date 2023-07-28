class Atm:

    def __init__(self):
        self.__pin = ""
        self.__balance = 0
        
        self.menu()
    def menu(self):
        user_input = input("""
                      hi!....how can i help u?
                      1. Enter 1 for pin 
                      2. Enter 2 for withdrawal
                      3. Enter 3 for deposit
                      4. Enter 4 to check balance
                      5. Enter 5 for exit
                      """)
        if user_input == "1":
            self.create_pin()
                
        elif user_input =="2":
            self.withdrawal
                
        elif user_input == "3":
            self.deposit()
                
        elif user_input == "4":
            self.check_balance()
                
        else:
            print ("bye")
        
        
    def create_pin(self):
        self.__pin = input("Enter your pin")
        print ("pin set successfully")
            
    def deposit(self):
        a =input("Enter your pin")
        if a == self.__pin:
            amount = int(input("enter your amount"))
            self.__balance = self.__balance + amount
            print("deposit successfully")
        else:
            print("invalid pin")
                
                
    def withdrawal(self):
        a =input("Enter your pin")
        if a == self.__pin:
            amount = int(input("enter the amount"))
            if amount<self.__balance:
                self.__balance = self.__balance - amount
                print("withdrawal successfully")
            else:
                print("paisa daal gaarib")
                                 
        else:
            print("wrong pin")
                
                
    def check_balance(self):
        a =input("Enter your pin")
        if a == self.__pin:
            print( self.__balance)
                
        else:
            print("wrong pin")
                
                
            
            
        