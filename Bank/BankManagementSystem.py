from data import database


type_user = input("New User or Existing User: ").lower()

if type_user == "existing":
    name = input("Enter your name: ").lower()
    for i in database:
        if database[i]["name"] == name:
            choice = input("Enter what do you want to do\nCheck Balance/Withraw Money/Deposit Money: ").lower()
            if choice == "check":
                print(f"Your Account Balance is: ${database[i]["balance"]}")
                database[i]["free_chances"] -= 1
                if database[i]["free_chances"] <= 0:
                    database[i]["balance"] -= 5
                    print(f"$5 diducted from your account\nCurrent Balance: {database[i]["balance"]}")
                    database[i]["free_chances"] = 5
            elif choice == "withdraw":
                withdraw_amount = float(input("Enter amount to Withdraw: $"))
                if withdraw_amount > database[i]["balance"]:
                    print("Not enough balance in you account!! Gareeb")
                else:
                    database[i]["balance"] -= withdraw_amount
                    print(f"Withdrawed ${withdraw_amount} from your balance\nCurrent Balance: {database[i]["balance"]}")
            elif choice == "deposit":
                deposit_amount = float(input("Enter amount to Deposit: $"))
                database[i]["balance"] += deposit_amount
                print(f"Deposited ${deposit_amount} in your account\nNew Balance: ${database[i]["balance"]}")
            else:
                print("invalid input")
# elif type_user == "new":
