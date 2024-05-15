menu = {
    'coffee': 50,
    'sandwich': 30,
    'pastry' : 20,
    'biscuit' : 10
}

def main():
    print("What would you like to order? ")
    order = input(print("coffee/sandwich/pastry/biscuit "))
    if order in menu.items():
        order_amount += 