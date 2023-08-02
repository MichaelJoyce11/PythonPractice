#function to create an account (send the account function and counter.)
def create_account(accounts, account_counter):
    #Have initial balance from user, and set an account number with the account number.
    initial_balance = float(input("Enter initial balance: "))
    account_number = str(account_counter)
    accounts[account_number] = initial_balance
    print(f"Account created successfully! Your account number is {account_number}.")
    account_counter += 1 #increase account number for next user. 
    return account_counter #return account counter so we can continue using it. 

#display balance function. 
def display_balance(accounts):
    #get the account from the user. 
    account_number = input("Enter account number: ")
    #if this account is in accounts, the array, we can then display a balance. 
    if account_number in accounts:
        balance = accounts[account_number]
        print(f"Account {account_number} balance: ${balance}")
    else:
        print("Account not found!")

#lets create a deposit funds account. 
def deposit_funds(accounts):
    #input the account number, and if in accounts, we can deposit.
    account_number = input("Enter account number: ")
    if account_number in accounts:
        #deposit an amount into the desired account. 
        amount = float(input("Enter amount to deposit: "))
        accounts[account_number] += amount
        print(f"Deposited ${amount} into account {account_number}")
    else:
        #if no account, dont do anything.
        print("Account not found!")

#withdraw funds function. 
def withdraw_funds(accounts):
    #input the account number, and if in accounts, we can withdraw.
    account_number = input("Enter account number: ")
    if account_number in accounts:
        #withdraw an amount from the desired account. 
        amount = float(input("Enter amount to withdraw: "))
        #if there is enough money, withdraw the amount, and subtract from total, otherwise insufficient balance.
        if accounts[account_number] >= amount:
            accounts[account_number] -= amount
            print(f"Withdrew ${amount} from account {account_number}")
        else:
            print("Insufficient balance!")
    else:
        #if no account, dont do anything.
        print("Account not found!")

def banking_application():
    #initialize the accounts array
    accounts = {}
    #initialize the counter. 
    account_counter = 1

    #display the options, and keep the options going until the user decides to quit. 
    print("Welcome to our nifty bank application, thank you for using it!")
    while True:
        print("\n1. Create a new bank account")
        print("2. Display account balance")
        print("3. Deposit funds")
        print("4. Withdraw funds")
        print("5. Exit")

        #recieve the user choices. 
        choice = input("Enter your choice: ")

        #do an elif for the user choices. 
        if choice == "1":
            #with returning the account counter, it keeps place of how many accounts have been made.
            account_counter = create_account(accounts, account_counter)
        
        elif choice == "2":
            display_balance(accounts)

        elif choice == "3":
            deposit_funds(accounts)

        elif choice == "4":
            withdraw_funds(accounts)
        #if choice 5, break from the loop, and thank the user for using the program.
        elif choice == "5":
            break

        else:
            print("Invalid choice!")

    print("Thank you for using the banking application!")

banking_application()
