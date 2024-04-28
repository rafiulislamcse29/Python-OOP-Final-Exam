class Admin:
  def __init__(self,bank) -> None:
    self.bank=bank
  
  def create_user_account(self,name,email,address,account_type):
    account_number=self.bank.create_account(name,email,address,account_type)
    print(f"account number {account_number}")
  def delete_user_account(self,account_number):
    return self.bank.delete_account(account_number)
  
  def view_all_accounts(self):
    return self.bank.account_list()
  
  def view_total_loans(self):
    print(f"Total Loan Amount {self.bank.total_loans}")
  
  def loan_feature(self):
    return self.bank.loan_feature_toggle()
  
  def view_total_bank_balance(self):
     print(f"Total Bank Balance {self.bank.get_bank_balance}")
   
