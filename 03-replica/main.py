from users import User
from bank import Bank
from admin import Admin

dbbl = Bank("dbbl")
admin = Admin(dbbl)
users = {}

def admin_menu():
    while True:
        print("\nAdmin Menu")
        print("1. Create User Account")
        print("2. Delete User Account")
        print("3. View All Accounts")
        print("4. View Total Bank Balance")
        print("5. View Total Loans Given")
        print("6. Toggle Loan Feature")
        print("7. Exit")
        ch = int(input("Enter choice : "))

        if ch == 1:
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = input("Enter account type (Savings/Current): ")
            admin.create_user_account(name, email, address, account_type)
        elif ch==2:
            account_number = int(input("Enter account number : "))
            admin.delete_user_account(account_number)
        elif ch==3:
            admin.view_all_accounts()
        elif ch==4:
            admin.view_total_bank_balance()
        elif ch==5:
            admin.view_total_loans()
        elif ch==6:
            admin.loan_feature()
        elif ch==7:
            break
        else:
            print("invalid input")



def user_menu():
    while True:
        print("\nUser Menu")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Check Transaction History")
        print("5. Take Loan")
        print("6. Transfer Money")
        print("7. Exit")
        ch = int(input("Enter choice : "))

        if ch==1:
            amount = float(input("Enter amount to deposit: "))
            user.deposit(amount,dbbl)
        elif ch==2:
            amount = float(input("Enter amount to withdraw: "))
            user.withdraw(amount,dbbl)
        elif ch==3:
            user.check_balance()
        elif ch==4:
            user.check_transactions()
        elif ch==5:
            amount = float(input("Enter amount to loan: "))
            user.take_loan(amount,dbbl)
        elif ch==6:
            amount = float(input("Enter amount to transfer: "))
            other_account = int(input("Enter recipient account number: "))
            user.balance_transfer(amount,other_account,dbbl)
        elif ch==7:
            break
        else:
            print("Invalid Input")


while True:
        print("\nBank Management System")
        print("1. Admin Login")
        print("2. User Login")
        print("3. User Registration")
        print("4. Exit")
        ch = int(input("Enter choice : "))
        if ch == 1:
           admin_menu()
        elif ch == 2:
            account_number = int(input("Enter your account number : "))
            if account_number in dbbl.accounts:
                user = dbbl.accounts[account_number]
                user_menu()
            else:
                print("Account number incorret!!.")
        elif ch==3:
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = input("Enter account type (Savings/Current) : ")
            account_number=dbbl.create_account(name, email, address, account_type)
            print(f"Your account number  {account_number}")
        elif ch==4:
            break
        else:
            print("Invalid input")


