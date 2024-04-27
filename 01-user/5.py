# Can check transaction history.

import random
class Bank:
  account_types=["savings","current"]
  def __init__(self,name) -> None:
    self.name=name
    self.accounts={}
  
  def create_account(self,name,email,address,account_type):
    account_number=random.randint(200000, 900000)
    if account_type.lower() in self.account_types:
      self.accounts[account_number]=User(name,email,address,account_type,account_number)
      print("account create Successfull")
    else:
       print("account must savings or current type!!!!")
    return account_number


class User:
  def __init__(self,name,email,address,account_type,account_number) -> None:
    self.name=name
    self.email=email
    self.address=address
    self.account_type=account_type
    self.account_number=account_number
    self.__balance=0
    self.transaction_history = []
  
  def deposit(self,amount):
    self.__balance+=amount
    self.transaction_history.append(("Deposit",amount))
    print("Deposti successfull")
  
  def withdraw(self,amount):
    if self.__balance>amount:
      self.__balance-=amount
      self.transaction_history.append(("Withdraw",-amount))
      print(f"withdraw successfull account balance {self.__balance}")
    else:
      print("Withdrawal amount exceeded ")
  
  def check_balance(self):
    print(f'Available balance : {self.__balance}')

  def check_transactions(self):
    print("Transaction History")
    for key,value in self.transaction_history:
      print(key,value)



dbbl=Bank("DBBL")
account_num1=dbbl.create_account("rafiul", "rafiul@gmail.com", "Pabna", "Savings")
account_num=dbbl.create_account("rafi", "rafi@gmail.com", "Kustia", "Current")
rafi=dbbl.accounts[account_num]
rafiul=dbbl.accounts[account_num1]

rafi.deposit(3413)
rafi.withdraw(2000)
rafi.check_balance()
rafi.check_transactions()

rafiul.deposit(1000)
rafiul.withdraw(500)
rafiul.check_transactions()

