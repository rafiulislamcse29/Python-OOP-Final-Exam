# Can create an account with his/her name, email, address and account Type(Mainly Two Types: Savings & Cuurent).	

class Bank:
  account_types=["savings","current"]
  def __init__(self,name) -> None:
    self.name=name
    self.accounts={}
  
  def create_account(self,name,email,address,account_type):
    if account_type.lower() in self.account_types:
      self.accounts[name]=User(name,email,address,account_type,)
      print("account create Successfull")
    else:
       print("account must savings or current type!!!!")

class User:
  def __init__(self,name,email,address,account_type) -> None:
    self.name=name
    self.email=email
    self.address=address
    self.account_type=account_type
  


dbbl=Bank("DBBL")
dbbl.create_account("rafiul", "rafiul@gmail.com", "Pabna", "Savings")
dbbl.create_account("rafi", "rafi@gmail.com", "Kustia", "Current")
print(dbbl.accounts)
