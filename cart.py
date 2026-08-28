#SHOOPING APP SIMULATOR USING BASIC OOPS

import datetime as dt

date = dt.datetime.now().strftime("%d %b %Y %I:%M:%S")

class Cart:
    def __init__(self):
        self.items = []

    def __str__(self):
        result = ""
        for index, item in enumerate(self.items , 1):
            result += str(index)+"."+item + "\n"
        return f"The items in the cart are:\n{result}"

    def __len__(self):
        return len(self.items)

class Orders:
    def __init__(self,items):
        self.items = items
        self.orderhist = []

    def order_history(self):
        for item in self.items:
            self.orderhist.append(item)
        return self.orderhist

class Store:
    def __init__(self ):
        self.store = {}
    def add_items(self , item , price , category):
        self.store[item] = (price , category)
        return self.store
        
    def __str__(self):
        result = ""
        result += f"{'Product':<10}\t{'Price':10}\t{'Category':<10}\n"
        for item , (price , category) in self.store.items():
            result += f"|{item:<10}\t{price:<10}\t{category:<10}\n"
        return result

    def __len__(self):
        return len(self.store)

    def show_categories(self , category):
        categories = set([self.store[product][1] for product in self.store])
        if category not in categories:
            return "Category does not exist"
        result = f"{category}:\n"
        result += f"{'Product':<10}\t{'Price':10}\n"
        for product in self.store:
            if self.store[product][1] == category:
                result += f"{product:<10}\t{self.store[product][0]:<10}\n"

        return result

    def search(self , item):
        found = False
        for product in self.store:
            if product == item:  
                found = True
        if found:
            return self.store[product][0] 
        else:
            return 0
    def display_search(self , item):
        ans  = self.search(item)
        if ans != 0:
            print(f"{item}:\nPrice:{self.store[item][0]}\nCategory:{self.store[item][1]}")
        else:
            print(f"{item} not present in store")



class User:
    def __init__(self , name , store):
        """
        1.Defines the name of the user
        """
        self.name = name
        self.store = store 
        self.cart = Cart() 
        self.details = {}
        self.wishlist = []

    def add_to_cart(self , item , quantity):
        if item not in self.store.store:
            print("Item not available\nThe available items are:")
            print(self.store.store)
            return
        for _ in range(quantity):
            self.cart.items.append(item)
        self.details[self.name] = {"items" : self.cart.items}

    def remove_from_cart(self , item , quantity):
        item_list = self.cart.items
        valid = item_list.count(item) > quantity and item in item_list
        if valid:
            for _ in range(quantity):
                item_list.remove(item)
            self.details[self.name]["items"] = item_list
        else:
            print("Invalid")

    def add_to_wishlist(self , item):
        self.wishlist.append(item)

    def checkout(self):
        global date 
        order = Orders(self.details[self.name].get("items" , 0))
        if order == 0:
            return "Must buy something to checkout" 
        result = ""
        result += date + ":\n"
        for orders in order.order_history():
            result +=f"{orders}\n"
        self.cart.items.clear()
        return result

class Bill:
    def __init__(self , user , store):
        self.user = user
        self.store = store

    def pay(self):
        total_price = 0 
        for product in user.cart.items:
            total_price += self.store.search(product)*user.cart.items.count(product)
        return total_price



shop = Store()
name = input("Enter Your name: ")
user = User(name , shop)
shoppin = 1234
bill = Bill(user , shop)
hist = False

owner = input("Are you the owner of the shop or a customer?").upper()
if owner!= "OWNER":
    print("<<<MENU>>>")

while owner == "OWNER":
    try:
        pin = int(input("Enter the shop pin: "))
        break
    except ValueError:
        print("Pin must be an intger: ")
        continue
while pin == shoppin:
    print("<<<ADD ITEMS TO THE SHOP>>>")
    item = input("Enter your item:").title()
    try:
        price = float(input(f"Enter the price of {item}:"))
    except ValueError:
        print("Price must be an integer/Float.")
        continue
    category = input(f"Enter the category of {item}:").title()
    shop.add_items(item , price , category)
    more = input("Do you want to continue (Y/N)? ").upper()
    if len(shop) != 0 and more == "N":
        break
    elif len(shop) == 0 :
        print("Shop cannot be empty")
        continue

owner = input("Are you the owner of the shop or a customer?").upper()
if owner!= "OWNER":
    print("<<<MENU>>>")

while owner != "OWNER":
    try:
        choice = int(input("1.Add items to cart\n"\
                    "2.Remove items from cart\n"\
                    "3.Add an item to wishlist\n"\
                    "4.Checkout\n"\
                    "5.Search an item\n"\
                    "6.Show different categories of items\n"\
                    "7.Show order history\n"\
                    "8.Exit\n" ))                           
    except ValueError:
        print("Choice must be an integer:")
        continue
    if choice == 1:
        print(shop)
        print()
        item = input("What item do you want? ").title()
        while True:
            try:
                quantity = int(input(f"How many {item}(s) do you want? "))
                if quantity == 0:
                    raise ValueError
                break
            except ValueError:
                print("Quantity must be a non zero integer")
                continue
        user.add_to_cart(item , quantity)
    if choice == 2:
        print(*user.cart.items , sep = "\n")
        print(f"There are {len(user.cart)} item(s) in your cart.")
        if len(user.cart) == 0:
            print("Add some items to your empty cart!")
            continue
        print()
        item = input("What item do you want to remove? ").title()
        while True:
            try:
                quantity = int(input(f"How many {item}(s) do you want to remove? "))
                if quantity == 0:
                    raise ValueError
                break
            except ValueError:
                print("Quantity must be a non zero integer")
                continue      
        user.remove_from_cart(item , quantity)
        print()
        print("Cart:")
        print(*user.cart.items , sep = "\n")
        print(f"There are {len(user.cart)} item(s) in your cart now.")
    if choice == 3:
        print(shop)
        print()
        item = input("What item do you want to add to the wishlist? ").title()
        user.add_to_wishlist(item)
    if choice == 4:
        while True:
            check = input("Do you want to check out? (Y/N)").upper()
            if check ==  "Y":
                print(f"You need to pay {bill.pay()}")
                try:
                    amount_payed = float(input("Enter the amount:"))
                    if amount_payed == 0 :
                        raise ValueError
                except ValueError:
                    print("Amount must be an non zero float")
                    continue
                if amount_payed == bill.pay():
                    print("Checkout done!")
                    hist = user.checkout()
                    break
                else:
                    print("Not enough money!")
                    continue
            if check == "N":
                break
    if choice == 5:
        print(shop)
        print()
        search_item = input('Enter the item to search: ').title()
        print()
        shop.display_search(search_item)
    if choice == 6:
        print(shop) 
        print()
        category = input("Enter the category you want to search: ").title()
        print()
        print(shop.show_categories(category))
    if choice == 7:
        if not hist:
            print("You have not ordered anything")
            continue
        print(hist)
    if choice == 8:
        break
