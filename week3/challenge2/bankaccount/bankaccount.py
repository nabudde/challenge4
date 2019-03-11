class Bankaccount: 
    # def __init__(self): 
    def deposit(self,): 
        balance     = input("Enter amount to be Deposited: ")        
        if self.balance == 0:
            print("\n get balance:", amount) 
    def withdraw(self): 
         amount = float(input("Enter amount to be Withdrawed: ")) 
         if self.balance >= amount: 
            self.balance -= amount 
            print("\n You Withdrawed:", amount) 
         else: 
             print("\n Insufficient balance  ") 
    def display(self): 
         print("\n Net Available Balance =", self.balance) 
s=Bankaccount()

s.deposit()
s.withdraw()
s.display()
    
    