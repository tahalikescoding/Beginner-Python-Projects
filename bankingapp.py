import json
import random
from abc import ABC , abstractmethod
import datetime as dt

class PasswordError(Exception):
    pass

class Bank:
    def __init__(self):
        self._username = None
        self._password = None
        self.details = {}

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self , value):
        if not isinstance(value , str):
            raise ValueError("Username must be str")
        for letter in value:
            if letter.isdigit():
                raise ValueError("Username cant have digits")
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,value:str):
        upper = False
        lower = False
        digit = False
        special = False
        whitespace = False
        for letter in value:
            if letter.isupper():
                upper = True 
            if letter.islower():
                lower = True
            if letter.isdigit():
                digit = True
            if letter in "!@#$%^&*_-=+/*?><.,:;|":
                special = True
            if letter.isspace():
                whitespace = True
        lenvalid = len(value) >10 and len(value)<20 
        if upper and lower and digit and special and lenvalid and not whitespace:
            self._password = value
        if not upper or not lower:
            raise PasswordError("Password must contain both upper and lower case letters")
        if not digit:
            raise PasswordError("Password must contain a digit.")
        if not special:
            raise PasswordError("Password must contain a special character")
        if whitespace:
            raise PasswordError("Password must not contain any spaces")
        if not lenvalid:
            raise PasswordError("Password must be at least 10 chars long and less than 20 chars.")

    def strong_password_generator(self):
        letters = "abcdefghijklmnopqrstuvwxyz"
        alphabets = letters + letters.upper()
        numbers = "1234567890"
        special = "!@#$%^&*_-=+/*?><.,:;|"
        allchars = alphabets+numbers+special
        password = random.choice(letters) + random.choice(letters.upper()) + random.choice(numbers) + random.choice(special)
        for _ in range(10):
            password += random.choice(allchars)
        return password

    def register(self , username , password):
        try:
            with open("userinfo.json" , "r") as f:
                details = json.load(f)
                for user in details:
                    if user == username:
                        return "Account already exists. Please sigh in."
        except FileNotFoundError:
            details = {}
        details[username] = password
        with open("userinfo.json" , "w") as f:
            json.dump(details , f , indent = 4)
        return f"{username} registered sucessfully!"

    def signin(self , username:str, password:str):
        siginedin = False
        try:
            with open("userinfo.json" , "r") as f:
                details = json.load(f)
        except FileNotFoundError:
            print("Bank is empty , please register!")
            return siginedin
        if username not in details:
            print("User not found")
        if username in details:
            if details[username] == password:
                siginedin = True
            if details[username] != password:
                siginedin = "Incorrect"
        return siginedin

    def __str__(self):
        try:
            with open("userinfo.json" , "r") as f:
                details = json.load(f)
        except FileNotFoundError:
            return "Bank empty"
        result = "<<<USERS>>>\n"
        for user in details:
            result+= user + "\n"
        return result

    def change_password(self , username , newpassword):
        with open("userinfo.json" , "r") as f:
            details = json.load(f)
        details[username] = newpassword
        with open("userinfo.json" , "w")  as f:
            json.dump(details , f ,indent=4)

bank = Bank()
access = True

while True:
    print("1.SIGN IN\n" \
            "2.REGISTER\n" \
            )
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please input an appropriate choice.")
        continue
    if choice == 1:
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()
        status = bank.signin(username , password)
        if status and status != "Incorrect":
            print("SIGN IN SUCESSFULL!\n" \
            "ACESS GRANTED\n")
            user = username
            access = True
            break
        if status == "Incorrect":
            choice = input("Password Incorrect! , Do you want to change your password?(Y/N)")
            if choice.upper() == "N":
                continue
            if choice.upper() == "Y":
                while True:
                    newpassword = input('Enter your new password: ')
                    try:
                        bank.password = newpassword
                    except PasswordError as e:
                        print(e)
                        continue
                    confirm = input("Confirm the password: ")
                    if confirm != newpassword:
                        print("Confirmed password not the same as new password")
                        continue
                    if confirm == newpassword:
                        bank.change_password(username , newpassword)
                        print("Password Changed sucessfully!")
                        break
            else:
                print("Please input a valid choice!")
    if choice == 2:
        username = input("Enter your name: ")
        while True:
            try:
                ask = int(input("1.Do you want to enter your own password\n" \
                "2.Create a strong password\n"))
                if ask<1 or ask>2:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid choice.")
        if ask == 1:
            print("<<<<PASSWORD RULES>>>>\n1.Password must contain but uppercase and lowercase letters\n" \
            "2.Password must contain a digit\n" \
            "3.Password must contain a special character\n" \
            "4.Password must not contain any spaces")
            while True:
                try:
                    password = input("Enter Your Password: ")
                    bank.password = password
                    print(bank.register(username , password))
                    print('Registered sucessfully , login to access.')
                    break
                except PasswordError as e:
                    print(e)
                    cont = input("Do you want to continue or make a strong password? (Y/N):").upper()
                    if cont == "Y":
                        continue
                    if cont == "N":
                        ask = 2
                        break
                    else:
                        print("Please input a valid value.")
                        continue
        if ask == 2:
            password = bank.strong_password_generator()
            print(bank.register(username , password))
            print('Registered sucessfully , login to access.')

class User:
    def __init__(self , username:str):
        self.username = username

    def load(self):
        try:
            with open(f"{self.username.lower()}.json" , "r") as f:
                details = json.load(f)
        except FileNotFoundError:
            details = {}
        return details

    def writing(self , details = None):
        if details is None:
            details = {}
        with open(f"{self.username.lower()}.json" , "w") as f:
            json.dump(details , f , indent= 4 )

    def __str__(self):
        details = self.load()
        result = "<<<<ACCOUNT DETAILS>>>\n"
        for key , value in details.items():
            result += f"{key}:{value}\n"
        return result

    def see_accounts(self):
        result = ""
        details = self.load()
        for account , amount in details.items():
            if "_" in account or account == "FD":
                continue
            result+=(f"{account}:{amount}AED\n")
        return result      

    def check_premium(self):
        if "Premium" in self.load():
            return True
        return False

class Account:
    def __init__(self, username , account_type):
        self.user = User(username)
        self.account_type = account_type
        self.account_list = ["Current" , "Saving" , "Premium" , "FD"]

    def create_account(self):
        details = self.user.load()
        details.setdefault(self.account_type , 0)
        self.user.writing(details)

    def deposit(self , amount):
        if not isinstance(amount , (int , float)):
            return "Amount to be added must be an integer/float"
        if amount<=0:
            return "Amount to be added must be greater than 0."
        details = self.user.load()
        details[self.account_type] = details.get(self.account_type , 0) + amount
        self.user.writing(details)
        return f"{amount} deposited sucessfully!"

    def withdraw(self , amount):
        if not isinstance(amount , (int , float)):
            return "Amount to be withdrawn must be an integer/float"
        if amount<=0:
            return "Amount to be withdrawn must be greater than 0."
        if amount> self.get_funds():
            return f"Amount to be withdraw must be less than total amount {self.get_funds()}"
        details = self.user.load()
        details[self.account_type] = details.get(self.account_type , 0) - amount
        self.user.writing(details)
        return f"{amount} withdrawn sucessfully!"

    def get_funds(self):
        details = self.user.load()
        return details.get(self.account_type , 0)

    def transfer(self , other:Account , amount):
        if other.account_type in self.account_list and other.account_type != self.account_type:
            transfer_amount = amount
            details = self.user.load()
            if other.account_type in details:
                if amount>details[self.account_type]:
                    return f"Not enough money in {self.account_type}"
                details[other.account_type] = details.get(other.account_type , 0) + transfer_amount
                details[self.account_type] = details.get(self.account_type , 0) - transfer_amount
                self.user.writing(details)
                return f"Transaction sucessfull!\n{self.account_type} Account: {details[self.account_type]}\n{other.account_type}: {details[other.account_type]}\n"
        elif other.account_type == self.account_type:
            return f"You are currently in {self.account_type} account"
        else:
            return f"{other.account_type} does not exist"

        
class SavingAccount(Account):
    def __init__(self , username ):
        self.account_type = "Saving"
        super().__init__(username , self.account_type)
        self.date_create = dt.datetime.now().isoformat()
        details = self.user.load()
        self.rate = 0.03
        details.setdefault("start_saving_intrest_date" , self.date_create)
        self.user.writing(details)

    def apply_intrest(self):
        now = dt.datetime.now()
        details = self.user.load()
        start = dt.datetime.fromisoformat(details["start_saving_intrest_date"])
        months_elapsed = (now.year - start.year)*12 + (now.month - start.month)
        if months_elapsed<=0:
            return "No intrest due yet."
        amount_after_intrest = details[self.account_type]*(1+self.rate/12)**months_elapsed
        details[self.account_type] = amount_after_intrest
        details["start_saving_intrest_date"] = now.isoformat()
        self.user.writing(details)
        return f"Intrest collected , new amount is {details[self.account_type]}AED"

    def withdraw_limits(self):
        details = self.user.load()
        details["Number_of_withdrawals_from_savings"] = details.get("Number_of_withdrawals_from_savings" , 0)
        details.setdefault("Last_resetted_date" , dt.datetime.now().isoformat())
        self.user.writing(details)
        max_withdrawal = 5
        current = dt.datetime.now()
        if current >= dt.datetime.fromisoformat(details["Last_resetted_date"]) + dt.timedelta(days=30):
            details["Number_of_withdrawals_from_savings"] = 0 
            details["Last_resetted_date"] = dt.datetime.now().isoformat()
            self.user.writing(details)
        if details["Number_of_withdrawals_from_savings"] >= max_withdrawal:
            return False
        return True

    def increment_limit(self):
        details = self.user.load()
        details["Number_of_withdrawals_from_savings"] = details.get("Number_of_withdrawals_from_savings" , 0)+1
        self.user.writing(details)


class PremiumSavingAccount(SavingAccount):
    
    def __init__(self , username):
        super().__init__(username)
        self.account_type = "Premium"
        self.rate = 0.05

    def create_prem(self):
        details = self.user.load()
        if "Saving" in details:
            amount = details.pop("Saving")
        details["Premium"] = amount
        self.user.writing(details)

class FixedDeposit(Account):
    def __init__(self , username):        
        super().__init__(username , "FD")

    def create_fd(self , amount, year , account:Account):
        if amount<1000:
            raise ValueError("Amount must be atleast 1000")
        details = self.user.load()
        details["fixed_deposit_start_date"] = dt.datetime.now().isoformat()
        if details.get(account , 0) <amount:
            return "Not suffiecient funds!"
        if details.get(account , 0) == amount:
            return "You cannot transfer all your funds to the FD"
        details[account] = details.get(account , 0 ) - amount
        td = dt.timedelta(days = year*365)
        details["fixed_deposit_end_date"] = (dt.datetime.now() + td).isoformat()
        details["FD"] = amount
        details["FD_year"] = year
        self.user.writing(details)


    def deposit(self):
        return "Can only deposit a fixed amount."

    def calc_intrest(self):
        details = self.user.load()
        year = details["FD_year"]
        amount = details["FD"]
        return amount*(1+0.07/12)** (12*year)


    def withdraw(self , account):
        details = self.user.load()
        if dt.datetime.now() <= dt.datetime.fromisoformat(details["fixed_deposit_end_date"]):
            td = dt.datetime.fromisoformat(details["fixed_deposit_end_date"]) - dt.datetime.now()
            return f"FD time period has not ended.\nTime left: {td}" 
        else:
            amount = self.calc_intrest()
            details = self.user.load()
            details[account] = details.get(account , 0) + amount
            details.pop("FD")
            details.pop("fixed_deposit_start_date")
            details.pop("fixed_deposit_end_date")
            details.pop("FD_year")
            self.user.writing(details)
            return amount


sacc = None
pacc= None
fd = None
while True:
    try:
        choice = int(input(
        "1.Deposit into current account\n" \
        "2.Withdraw From current account\n" \
        "3.Create a savings account\n" \
        "4.Deposit into a savings account\n" \
        "5.Withdraw from savings account\n" \
        "6.Create a premium savings account\n" \
        "7.Deposit into premium savings account\n" \
        "8.Withdraw from premium savings account\n" \
        "9.Check current accounts\n" \
        "10.Transfer money\n" \
        "11.Check intrest on savings account\n" \
        "12.Check intrest on Premium savings account\n"
        "13.Make a Fixed deposit\n" \
        "14.Withdraw fixed deposit\n" \
        "15.Exit\n"))
        if choice>15:
            raise ValueError
    except ValueError:
        print("Please input a valid choice.")
        continue
    acc = Account(user , "Current")
    acc.create_account()
    if choice == 1:
        while True:
            try:
                amount = float(input("Enter the amount you want to deposit in curretn account: "))
                break
            except ValueError:
                print("Amount must be an integer or a float")
                continue
        print(acc.deposit(amount))
    if choice == 2:
        while True:
            try:
                amount = float(input("Enter the amount you want to withdraw from current account: "))
                break
            except ValueError:
                print("Amount must be an integer or a float")
                continue
        print(acc.withdraw(amount))

    if choice == 3:
        while True:
            if "Saving" not in User(user).load():
                if User(user).check_premium():
                    print("You have a premium account!")
                    break
                
                print("Pay 1000 to create a savings account and deposit atleast 1000 into your savings account.\n")
                try:
                    pay = int(input("Pay 1000 Aed: "))
                    if pay!=1000:
                        raise ValueError
                    depo = float(input("Deposit a minimum of 1000AED: "))
                    if depo<1000:
                        raise ValueError
                except ValueError:
                    print("Please input a valid amount.")
                    continue
                if "withdrawn sucessfully!" in acc.withdraw(pay+depo):
                    sacc = SavingAccount(user)
                    sacc.deposit(depo)
                    break
                else:
                    print("Not enough to create a savings account!")
                    break
            elif "Saving" in User(user).load():
                print("You already have a savings account!")
                break


    details = User(user).load()
    savings = "Saving" in details
    if savings and sacc is None: 
        sacc = SavingAccount(user)#if account exixts in file but i have not defined the object yet so we wll create an object
    if choice == 4:
        while True:
            if User(user).check_premium():
                print("You have a premium account!")
                break
            try:
                amount = float(input("Deposit to savings account: "))
                break 
            except ValueError:
                print("Please input a valid amount.")      
                continue
        if savings:
            sacc.deposit(amount)
            print("Money deposited sucessfully!")
        else:
            print("Make a savings account first.")

    if choice == 5:
        if savings and not User(user).check_premium():
            can_withdraw = sacc.withdraw_limits()
            if can_withdraw:
                while True:
                    try:
                        amount = float(input("Amount to withdraw: "))
                        break 
                    except ValueError:
                        print("Please input a valid amount.")      
                        continue
                check = sacc.withdraw(amount)

                if "withdrawn sucessfully!" in check:
                    sacc.increment_limit()
                else:
                    print("Not enough amount.")
            else:
                print('Withdrawal limit reached!')
        elif User(user).check_premium():
            print("You have premium account!")
        else:
            print("Create a savings account first!")

    if choice == 6:
        while True:
            if "Premium" not in User(user).load():
                try:
                    pay = int(input("Pay 2000AED for opening a premium savings account:"))
                    if pay!=2000:
                        raise ValueError
                except ValueError:
                    print("pay the correct ammount!")
                    continue
                check = acc.withdraw(2000)
                if "withdrawn sucessfully!" in check:
                    print('Premium saving account created sucessfully!')
                    pacc = PremiumSavingAccount(user)
                    pacc.create_prem()
                    break
                else:
                    print("Transaction failed.")
                    break
    prem = "Premium" in User(user).load()
    if prem and pacc is None: 
        pacc = PremiumSavingAccount(user)#if account exixts in file but i have not defined the object yet so we wll create an object
    if choice == 7:
        if prem:
            while True:
                try:
                    amount = float(input("Enter amount to deposit in Premium saving account: "))
                    if amount<=0:
                        raise ValueError
                    break
                except ValueError:
                        print("Enter a valid amount")
                        continue
            pacc.deposit(amount)
        else:
            print("You do not have a premium savings account.")

    if choice == 8:
        if prem:
            can_withdraw = pacc.withdraw_limits()
            if can_withdraw:
                while True:
                    try:
                        amount = float(input("Amount to withdraw: "))
                        break 
                    except ValueError:
                        print("Please input a valid amount.")      
                        continue
                check = pacc.withdraw(amount)
                if "withdrawn sucessfully!" in check:
                    pacc.increment_limit()
                else:
                    print("Not enough amount.")
            else:
                print('Withdrawal limit reached!')
        else:
            print("You do not hace a premium account!")

    if choice ==9:
        print(User(user).see_accounts())

    if choice == 10:
        while True:
            try:
                account = int(input("Enter the account you want to transfer FROM\n1.Current\n2.Savings\n3.Premium Savings\n:"))
                if account not in [1,2,3]:
                    raise ValueError
                if account == 1:
                    account_obj = acc
                if account ==2:
                    if savings:
                        if sacc.withdraw_limits():
                            account_obj = sacc
                        else:
                            print("You have reached maximum withdrawal limit for the month")
                            account_obj = acc                            
                    else:
                        print("You do not have a savings account")
                        account_obj = acc
                if account ==3:
                    if prem:
                        if pacc.withdraw_limits():
                            account_obj = pacc
                    
                        else:
                            print("You have reached maximum withdrawal limit for the month")
                            account_obj = acc
                    else:
                        print("You do not have a savings account")
                        account_obj = acc
                toaccount = int(input("Enter the account you want to transfer TO\n1.Current\n2.Savings\n3.Premium Savings\n:"))
                if toaccount not in [1,2,3]:
                        raise ValueError
                if toaccount == 1:
                    to_obj = acc
                if toaccount == 2:
                    if savings:
                        to_obj = sacc
                    else:
                        print("Savings account does not exist")
                        raise ValueError
                if toaccount == 3:
                    if prem:
                        to_obj = pacc
                    else:
                        print("Premium account does not exist")
                        raise ValueError
                amount = float(input("Enter amount to transfer: "))
                if amount<=0:
                    raise ValueError
                break
            except ValueError:
                print("Please input a valid choice.")
                continue
    
        check = account_obj.transfer(to_obj , amount)
        if "Transaction sucessfull" in check:
            if account_obj == sacc:
                sacc.increment_limit()
            elif account_obj == pacc:
                pacc.increment_limit()
        print(check)
    if choice == 11:
        if savings:
            print(sacc.apply_intrest())
        else:
            print('You do not have a savings account!')

    if choice == 12:
        if prem:
            print(pacc.apply_intrest())
        else:
            print("You do not have a premium savings account!")

    if choice == 13:
        while True:
            try:
                amount = float(input("Enter the amount to FD: "))
                if amount<=0:
                    raise ValueError
                year = int(input("Enter the number of years you want to keep the FD: "))
                if year<=1:
                    raise ValueError
                choice = int(input("Which account do you want the transfer the money from?\n1.Current\n2.Savings\n3.Premium Savings\n"))
                if choice not in [1,2,3]:
                    raise ValueError
                if choice == 1:
                    if acc.get_funds()>amount:
                        account = "Current"
                    else:
                        account = False
                if choice == 2:
                    
                    if savings:
                        if sacc.get_funds() >amount and sacc.withdraw_limits():
                            account = "Saving"
                        else:
                            print("You do not hae a savings account!")
                            account = False
                if choice == 3:
                    if prem:
                        if pacc.get_funds()>amount and pacc.withdraw_limits():
                            account = "Premium"
                        else:
                            print("You do not hae a premium savings account!")
                            account = False
                if not account:
                    print("Please choose an appropriate account")
                    raise ValueError
                fd = FixedDeposit(user)
                print(fd.create_fd(amount , year , account))
                break
            except ValueError:
                print("Please input a valid value.")
                continue

    isfd = "FD" in User(user).load()
    if isfd and fd is None:
        fd = FixedDeposit(user)

    if choice == 14:
        if isfd:
            while True:
                try:
                    choice = int(input("Which account do you want the transfer the money to?\n1.Current\n2.Savings\n3.Premium Savings\n"))
                    if choice not in [1,2,3]:
                        raise ValueError
                    if choice == 1:
                        account = "Current"
                    if choice == 2:
                        if savings:
                            account = "Saving"
                        else:
                            print("Savings account does not exist , sending to current account...")
                            account = "Current"
                    if choice == 3:
                        if prem:
                            account = "Premium"
                        else:
                            print("Premium sacvings account does not exist , sending to current account...")
                            account = "Current"
                    break
                except ValueError:
                    print("Please input a valid choice")
                    continue

            print(fd.withdraw(account))

    if choice == 15:
        print("Exiting...")
        break

            
                    
                
        
        




    


