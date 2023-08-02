#We need to create a class, for each individual account to keep track of
#balances, as there could be hundreds of accounts. 
class BankAccount:
    #This is called after the object has existed (it is the object itself), 
    #however, it initializes, by setting an account number and a balance.
    #we can then call self.balance and self.account_balance as variables for the
    #object in this class. 
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    #display the balance by calling it with the 
    def display_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance}")
    #deposit funds into an account by adding an amount declared, to a balance. 
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount} into account {self.account_number}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount} from account {self.account_number}")
        else:
            print("Insufficient balance!")

def banking_application():
    #easy way of keeping track of the accounts, we can start an account system.
    accounts = {}
    #initialize it for the first user.
    account_counter = 1

    #Greet the user.
    print("Hey!, welcome for using our nifty bank application, we hope it satisfies your needs!")
    #Have a while loop for the user, only exit when choice is 5. 
    while True:
    #give the user a list of options.
        print("\n1. Create a new bank account")
        print("2. Display account balance")
        print("3. Deposit funds")
        print("4. Withdraw funds")
        print("5. Exit")
        #recieve user's choice.
        choice = input("Enter your choice: ")

        #Create an elif for choices. 
        if choice == "1":
            #recieve an initial balance for the user to start account
            initial_balance = float(input("Enter initial balance: "))
            #create an account number. to intialize accounts. 
            account_number = str(account_counter)
            accounts[account_number] = BankAccount(account_number, initial_balance)
            print(f"Account created successfully! Your account number is {account_number}.")
            account_counter += 1

        elif choice == "2":
            account_number = input("Enter account number: ")
            if account_number in accounts:
                accounts[account_number].display_balance()
            else:
                print("Account not found!")

        elif choice == "3":
            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter amount to deposit: "))
                accounts[account_number].deposit(amount)
            else:
                print("Account not found!")

        elif choice == "4":
            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter amount to withdraw: "))
                accounts[account_number].withdraw(amount)
            else:
                print("Account not found!")

        elif choice == "5":
            break

        else:
            print("Invalid choice!")

    print("Thank you for using the banking application!")

banking_application()
