import sys
import copy
import time


# Make the class of costumer order
class pizza_order():
    def __init__(self):
        self.pickup = True
        self.name = ""
        self.address = None
        self.phone = None
        self.n_pizza = 0
        self.pizzas = []
        self.cost = 0

# Create the list of dictionaries containing pizzas names and prices
pizzas_available = [
    {"name": "Big Tony's",           "price": 11},
    {"name": "Tequila Pie",          "price": 11},
    {"name": "Pepperoni",            "price": 9},
    {"name": "Meat OMG",             "price": 12},
    {"name": "Texas Boy",            "price": 10.5},
    {"name": "Frikin Chicken",       "price": 10.5},
    {"name": "The V2",               "price": 9.5},
    {"name": "Spanish Virgin",       "price": 9},
    {"name": "Brooklyn",             "price": 6},
    {"name": "Cetral Park",          "price": 9.5},
    {"name": "Nduja",                "price": 8.5},
    {"name": "New York",             "price": 7.5},
    {"name": "Margarita",            "price": 7.5},
    {"name": "Cheky Cow",            "price": 14},
    {"name": "Vee Free",             "price": 9.5},
    {"name": "5th Avenue",           "price": 9.5},
    {"name": "The BRONX",            "price": 10.5},
]
# settting the delivery price
delivery_price = 2
# list of all orders
all_orders = []


# defining the exception when order is canceled
class CancelOrder(Exception):
        pass


# function for user input, checks if user want to cancel or quit
def user_input(message=None):
    u_input = input(str(message))
    lower = u_input.lower()
    if lower == "qq":
        print("Exiting the program")
        sys.exit()
    elif lower == "cc":
        print("Your order was canceled")
        raise CancelOrder()
    else:
        return u_input


# function for printing the menu
def print_menu():
    for i, pizza in enumerate(pizzas_available):
            print(" {}:{}, Price: {} ".format(str(i+1), pizza["name"], str(pizza["price"]) + "€"))


# function for printing the receipt of order
def order_receipt(order):
    header = u"\t{0:<10}{1:>10}{2:>10}{3:>10}".format("Amount", "Pizza", "Price", "Subtotal")
    print("|Costumer Name:{}".format(user_order.name))
    if not user_order.pickup:
        print("|Delivery address:{}".format(user_order.address))
        print("|Phone number:{}".format(user_order.phone))
    print(header)
    print('--'*len(header))
    for pizza in user_order.pizzas:
        print("\t{0:<10}{1:>10}{2:>10}€{3:>10}€".format(pizza["amount"], pizza["name"], pizza["price"], pizza["amount"]*pizza["price"]))
    print('--'*len(header))
    if not user_order.pickup:
        print("Delivery cost {}€".format(delivery_price))
    print("\t Total:{}€".format(user_order.cost))


# function to calculate total price of the order
def total_price():
    user_order.cost = sum(pizza["price"]*pizza["amount"] for pizza in user_order.pizzas)
    if not user_order.pickup:
        user_order.cost += delivery_price


print("====Welcome to Paulius Pizzas====")
print("We are ready to take your order")
print("If you want to quit press 'QQ' or if you wish to cancel your order press 'CC'")
# get user name
while True:
    user_order = pizza_order()
    try:
        # Get the name of user. Make sure it only contains alphabetic characters
        while True:
            menu = copy.deepcopy(pizzas_available)
            print("\n Starting new order")
            time.sleep(0.5)
            user_name = user_input("Write your name :")
            if user_name.isalpha():
                user_order.name = user_name
                break
            else:
                print("Name can only contain alphabetic characters")
        # get number of pizzas user wants to order. Make sure it only contains numeric characters and is >0
        while True:
            time.sleep(0.5)
            n_pizza = user_input("How many pizzas you would like to order:")
            try:
                val = int(n_pizza)
                if val > 0:
                    user_order.n_pizza = val
                    break
                else:
                    print("You should order at least one pizza")
            except ValueError:
                print("You must enter the number")
        # show the menu
        time.sleep(0.5)
        print("\n Here are our selection of pizzas avialable")
        print_menu()
        time.sleep(0.5)
        print("\n Please enter Your choice for each pizza you would like to order")
        print("\n Our choice must correspond to the pizza number in the menu")
        # ask to user to choose pizzas. Make sure it corresponds to numbers in the menu
        for i in range(user_order.n_pizza):
            while True:
                time.sleep(0.5)
                string = "Pizza number {} of {}".format(i+1, user_order.n_pizza)
                u_input = user_input(string + ":")
                try:
                    val = int(u_input)
                    if val == 0:
                        raise IndexError
                    to_add = menu[int(u_input)-1]
                    print(to_add["name"]+" " + "was added to our order\n")
                    # if pizzas is already in user order just add amout, else add new pizza
                    for o_pizza in user_order.pizzas:
                        if to_add["name"] in o_pizza["name"]:
                            o_pizza["amount"] += 1
                            break
                    else:
                        user_order.pizzas.append(to_add)
                        user_order.pizzas[-1]["amount"] = 1
                    break
                except (IndexError, ValueError):
                  print("Your choice of pizza number must correspond to the numbers in the menu\n")
        # Ask the user if he wants delivery. Make sure the entry is d or p
        while True:
            delivery = user_input("Will you pickup or would like your pizzas to be delivered.Type P for pickup, D for delivery:\n")
            if delivery.lower() not in ("d", "p"):
                print("You must type either P or D")
            elif delivery.lower() == "d":
                user_order.pickup = False
            else:
                break
            # if user wants delivery, ask for the address.Make sure it only contains alphanumeric characters
            if not user_order.pickup:
                while True:
                    address = user_input("Write down delivery address:")
                    if address.isalnum():
                        user_order.address = address
                        break
                    else:
                        print("Delivery address must contain alphanumeric characters only")
                # if user wants delivery, ask for the phone number.Make sure it only contains numeric characters
                while True:
                    phone = user_input("Write down your phone number:")
                    if phone.isnumeric():
                        user_order.phone = phone
                        break
                    else:
                        print("The phone number must contain numbers only")
                break
        # calculate total price
        total_price()
        print("Here is our order\n\n")
        time.sleep(0.5)
        # print the order receipt
        order_receipt(user_order)
        while True:
            # ask if user wants to submmit the order.Make sure the entry contains only y or n
            time.sleep(0.5)
            submission = user_input("Would you like to submit your order? [Y/N]:")
            if not submission.lower() in ("y", "n"):
                print("You should enter 'Y' or 'N'")
            elif submission.lower() == "y":
                time.sleep(0.5)
                print("\nYour order was submitted")
                all_orders.append(user_order)
                while True:
                    # ask if user wants to take another order. Make sure the entry contains only y or n
                    time.sleep(0.5)
                    another_order = user_input("\nWould you like to take another order? [Y/N]:")
                    if not another_order.lower() in ("y", "n"):
                        print("You should enter 'Y' or 'N'")
                    # if user doesn't want to take another order exit the program
                    elif another_order.lower() == "n":
                        time.sleep(0.5)
                        print("\nThank you for buying. See you next time")
                        sys.exit()
                    else:
                        break
                break
            # if user doesn't want to submit, ask what he wants to do. Make sure the entry corresponds to the options available
            elif submission.lower() == "n":
                time.sleep(0.5)
                print("So what would you like to do?")
                while True:
                    time.sleep(0.5)
                    options = user_input('''1.Quit(press qq)\n2.Cancel your order and startover(press cc)\n3.Change your order(press ch)\n4.Add pizza(press a)\n:''')
                    if not options.lower() in ("qq", "cc", "ch", "a"):
                        print("Your choice must corespond to the options")
                    # if user want to add pizza print the menu
                    elif options.lower() == "a":
                        time.sleep(0.5)
                        print_menu()
                        menu = copy.deepcopy(pizzas_available)
                        while True:
                            # ask for pizza which he wants to add. Make sure it corresponds to numbers in the menu
                            time.sleep(0.5)
                            addition = user_input("Which pizza you would like to add:")
                            try:
                                x = int(addition)
                                if x == 0:
                                    raise IndexError
                                addition2 = menu[int(addition)-1]
                                print(addition2["name"]+" " + "was added to our order\n")
                                # if pizzas was already order just add amount else add new pizza
                                for pizza in user_order.pizzas:
                                    if addition2['name'] in pizza['name']:
                                        pizza["amount"] += 1
                                        break
                                else:
                                    user_order.pizzas.append(addition2)
                                    user_order.pizzas[-1]["amount"] = 1
                                break
                            except(ValueError, IndexError):
                                print("Your choice of pizza must corespond to the numbers in menu")
                        total_price()
                        time.sleep(0.5)
                        order_receipt(user_order)
                        break
                    elif options.lower() == "ch":
                        # if user whats to change pizza. Print the pizzas he has ordered
                        time.sleep(0.5)
                        print("Here is your ordered pizzas")
                        for i, pizza in enumerate(user_order.pizzas):
                            print(i + 1, pizza["name"])
                        while True:
                            # ask which one of ordered pizzas he would likw to change. Make sure it corresponds to the numbers in order
                            time.sleep(0.5)
                            change_pizza = user_input('''Which one you would like to change?Type the number:''')
                            try:
                                val = int(change_pizza)
                                if val not in range(len(user_order.pizzas)+1):
                                    raise IndexError
                                to_change = user_order.pizzas[int(change_pizza)-1]
                                print(to_change["name"]+" " + "is ready to be changed")
                                index = user_order.pizzas.index(to_change)
                                break
                            except(IndexError, ValueError):
                                print("You must enter the number of the pizza you would like to change")
                        time.sleep(0.5)
                        # print the menu
                        print("What is your new pizza?")
                        print_menu()
                        while True:
                            # ask the the user to choose which pizza should be added instead of old one. Make sure it corresponds to the number in the menu
                            menu = copy.deepcopy(pizzas_available)
                            time.sleep(0.5)
                            replace = user_input("Enter the number of pizza:")
                            try:
                                val = int(replace)
                                if val == 0:
                                    raise IndexError
                                to_replace = menu[int(replace)-1]
                                time.sleep(0.5)
                                print(to_change["name"] + " " + "was replaced by" + " " + to_replace["name"])
                                # if replacment pizza has already been order. Delete the old pizza and add amount to the new.Else replace the olds' pizzas name and price with the news'
                                for p in user_order.pizzas:
                                    if to_replace['name'] in p['name']:
                                        del user_order.pizzas[index]
                                        p['amount'] += 1
                                        break
                                else:
                                    user_order.pizzas[index]['name'] = to_replace['name']
                                    user_order.pizzas[index]['price'] = to_replace['price']
                                break
                            except(IndexError, ValueError):
                                print("Your choice of pizza must corespond to the numbers in menu")
                        total_price()
                        time.sleep(0.5)
                        order_receipt(user_order)
                        break
    except CancelOrder:
        pass