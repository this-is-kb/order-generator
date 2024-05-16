menu = {
    'coffee': 50,
    'sandwich': 30,
    'pastry' : 20,
    'biscuit' : 10
}

bill = {

}

def main():
    query =input("Do you like to order anything? (Yes/No) ")
    if query == "Yes":
        order_fn()
        query2 = input("Do you like to order anything more? (Yes/No) ")
        while query2 == "Yes":
            order_fn()
            query2 = input("Do you like to order anything more? (Yes/No) ")
        else:
            print_all()
    else:
        print("Thank you for coming. Have a good day.")

def order_fn():
    print("What do you like to order? ")
    order = input("Coffee/sandwich/pastry/biscuit ")
    if order in menu.keys():
        bill.update({order:menu[order]})
    else:
        print(f"The item {order} is not in the menu. Please order soething else.")

def print_all():
    print("Your bill is: ")
    for key, value in bill.items():
        print(f"{key}={value}")
    print(f"Total amount = {sum(bill.values())}")

if __name__=="__main__":
    main()