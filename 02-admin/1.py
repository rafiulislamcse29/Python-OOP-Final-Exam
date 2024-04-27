# Can create an account            

import random
class Bank:
  account_types=["savings","current"]
  def __init__(self,name) -> None:
    self.name=name
    self.accounts={}
    self.loan_features_enabled=True
    self.__bank_balance=1000
  
  def create_account(self,name,email,address,account_type):
    account_number=random.randint(200000, 900000)
    if account_type.lower() in self.account_types:
      self.accounts[account_number]=User(name,email,address,account_type,account_number)
      print("account create Successfull")
    else:
       print("account must savings or current type!!!!")
    return account_number
  
  #getter
  @property
  def get_bank_balance(self):
    return self.__bank_balance

  #setter
  @get_bank_balance.setter
  def get_bank_balance(self,amount):
     self.__bank_balance+=amount


class User:
  def __init__(self,name,email,address,account_type,account_number) -> None:
    self.name=name
    self.email=email
    self.address=address
    self.account_type=account_type
    self.account_number=account_number
    self.__balance=0
    self.transaction_history = []
    self.loans_taken=0
  
  def deposit(self,amount,bank):
    self.__balance+=amount
    bank.get_bank_balance=amount
    self.transaction_history.append(("Deposit",amount))
    print("Deposti successfull")
  
  def withdraw(self,amount,bank):
    if self.__balance>amount:
      if bank.get_bank_balance>amount:
        self.__balance-=amount
        bank.get_bank_balance=-amount
        self.transaction_history.append(("Withdraw",-amount))
        print(f"withdraw successfull account balance {self.__balance}")
      else:
        print("bank is bankrupt.")
    else:
      print("Withdrawal amount exceeded ")
  
  def check_balance(self):
    print(f'Available balance : {self.__balance}')

  def check_transactions(self):
    print("Transaction History")
    for key,value in self.transaction_history:
      print(key,"<<<<------>>>>",value)

  def take_loan(self,amount,bank):
    if not bank.loan_features_enabled:
      print("Loan features is currently disabled..")
    elif self.loans_taken>=2:
      print("Maximum Loan limit 2 times")
    else:
      self.__balance+=amount
      bank.get_bank_balance=-amount
      self.loans_taken+=1
      self.transaction_history.append(("Loan successfull",amount))
      print("Loan Successful done")
      
    
  def balance_transfer(self,amount,other_account,bank):
    if other_account not in bank.accounts:
      print("Account does not exits")
    elif amount>self.__balance:
      print("Insufficient balance")
    else:
      self.__balance-=amount
      bank.accounts[other_account].__balance+=amount
      self.transaction_history.append((f"Transfer balance  account number({other_account})", amount))
      print("balance transfer successful")


class Admin:
  def __init__(self,bank) -> None:
    self.bank=bank
  
  def create_user_account(self,name,email,address,account_type):
    account_number=self.bank.create_account(name,email,address,account_type)
    print(f"Account create successfully with number {account_number}")
  




dbbl=Bank("DBBL")

account_num1=dbbl.create_account("rafiul", "rafiul@gmail.com", "Pabna", "Savings")
account_num=dbbl.create_account("rafi", "rafi@gmail.com", "Kustia", "Current")
rafi=dbbl.accounts[account_num]
rafiul=dbbl.accounts[account_num1]

rafi.deposit(1000,dbbl)
rafi.withdraw(999,dbbl)
rafi.check_balance()


rafi.balance_transfer(1,account_num,dbbl)
rafi.check_transactions()

rafiul.deposit(1000,dbbl)
rafiul.withdraw(500,dbbl)
rafiul.take_loan(1500,dbbl)
rafiul.withdraw(500,dbbl)
rafiul.check_balance()
rafiul.check_transactions()

admin=Admin(dbbl)
admin.create_user_account("shohel", "sohel@gmail.com", "Natore", "Savings")


print(dbbl.get_bank_balance)
