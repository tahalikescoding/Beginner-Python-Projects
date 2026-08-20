import json 
import os 
import datetime 

try:
    with open("bank.json" , "x") as f:
        json.dump({} , f , indent = 4)
except FileExistsError:
    pass

def register(username , password , amount = 0): 
    with open("bank.json" , "r") as f:
        bank = json.load(f)
        if username in bank:
            return "ACCOUNT ALREADY EXISTS! SIGN IN"
        bank[username] = {"password":password , "amount":amount}
    with open("bank.json" , "w") as f:
        json.dump(bank , f , indent=4)
    return "REGISTRATION SUCESSFULL!"

def passwordvalidator(password):
    valid = True
    if not len(password)>10:
        print("Length of password must bne greater than 10")
        valid = False
    for i in password:
        if i == " ":
            print("Password must not contain spaces")
            valid  = False
            break
    if password.isdigit():
        print("Password must contain characters and numbers")
        valid = False
    return valid
    
user = None

def sigin(username , password):
    global user
    with open("bank.json" , "r") as f:
        data = json.load(f)
    if username in data:
        if data[username]["password"] == password:
            user = username
            print("<<<ACESS GRANTED>>>")
            print(f"{username}\nBalance:{data[username]["amount"]}")
            return True
        else:
            print("Wrong password try again")
            return False
    else:
        print("Account does not ecist , PLEASE REGISTER")
        
while True:
    print()
    print("<<<USER LOGIN/SIGNUP>>>")
    try:
        print()
        choice = int(input("1.SIGN IN\n2.REGISTER\n"))
        print()
    except ValueError:
        print("Please enter a valid choice")
        continue
    if choice ==1:
        print()
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        print()
        found = sigin(username , password)
        if found:
            break
        else:
            continue
    if choice == 2:
        username = input("Enter your username: ")
        while True: 
            password = input("Enter your password: ")
            ans = passwordvalidator(password)
            if ans:
                amount = float(input("Enter amount (0 if you dont want to deposit anything): "))
                print(register(username , password , amount))
                break
            if not ans:
                continue


def change(amount = 0):
    with open("bank.json" , "r") as f:
        bank = json.load(f)
    if amount<0 and abs(amount)>bank[user]["amount"]:
        return "Withdrawn amount cannot be more than current amount"
    bank[user]["amount"] += amount 
    with open("bank.json" , "w") as f:
        json.dump(bank , f , indent=4)   
    return f"{user}\nAmount in bank: {bank[user]["amount"]}"

    
def deposit(amount):
    if amount<0:
        return "Amount to be deposited must be positive"
    return change(amount)

def withdraw(amount):
    if amount<0 : 
        return "Amount to be withdrawn must be positive"
    return change(-amount)

def deletion(name = user):
    with open("bank.json" , "r") as f:
        bank = json.load(f)
    confirm = input("ARE YOU SURE YOU WANT TO DELETE YOUR ACCOUNT? (Y/N): ")
    password = input("Enter your password: ")
    if confirm.upper() == "Y" and bank[name]["password"] == password:
        money = bank.pop(name)
        with open("bank.json" , "w") as f:
                json.dump(bank , f , indent= 4)
        return f"Account under the username '{name}' deleted , here is your refunded amount: {money["amount"]}"
    else:
        return "Deletion cancelled."
    
    
while True:
    print()
    print("<<<<<BANK MENU>>>>>")
    print()
    try:
        choice = int(input("1.Deposit Money\n2.Withdraw Money\n3.Delete an account\n4.Exit\n"))
    except ValueError:
        print("Please enter an integer")
        continue
    if choice == 1:
        while True:
            try:
                amount = float(input("Enter the amount to be deposited: "))
                print(deposit(amount))
                break
            except ValueError:
                print("Amount to be deposited must be an integer/float")
    if choice ==2:
        while True:
            try:
                amount = float(input("Enter the amount to be withdrawn: "))
                print(withdraw(amount))
                if amount>0:
                    break
            except ValueError:
                print("Amount to be withdrawn must be an integer/float")       
    if choice == 3:
        print(deletion())
        break

    if choice == 4:
        break
