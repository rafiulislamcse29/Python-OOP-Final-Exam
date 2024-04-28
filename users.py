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
    if self.__balance>=amount:
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
    print("\nActions\t\t\tAmount")
    for key,value in self.transaction_history:
      print(f"{key}\t\t\t{value}")

  def take_loan(self,amount,bank):
    if not bank.loan_feature_enabled:
      print("Loan features is currently disabled..")
    elif self.loans_taken>=2:
      print("Maximum Loan limit 2 times")
    else:
      self.__balance+=amount
      bank.get_bank_balance=-amount
      self.loans_taken+=1
      bank.total_loans += amount
      self.transaction_history.append(("Loan",amount))
      print("Loan Successful done")
      
    
  def balance_transfer(self,amount,other_account,bank):
    if other_account not in bank.accounts:
      print("Account does not exits")
    elif amount>self.__balance:
      print("Insufficient balance")
    else:
      self.__balance-=amount
      bank.accounts[other_account].__balance+=amount
      self.transaction_history.append((f"Transfer ({other_account})", -amount))
      bank.accounts[other_account].transaction_history.append((f"Received ({self.account_number})", +amount))
      print("balance transfer successful")

