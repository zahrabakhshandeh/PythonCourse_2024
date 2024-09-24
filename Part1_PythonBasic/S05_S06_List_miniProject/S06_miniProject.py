product_names = []
product_is_bought = []
product_prices = []

def add(name):
    if name not in product_names:
        product_names.append(name)
        product_is_bought.append(False)
        product_prices.append(None)
        print("Added!")
    else:
        print("Already Exist!") 

def display():
    for i, name in enumerate(product_names):
        print(i+1, name, product_is_bought[i], product_prices[i])   

def edit(name):
    if name in product_names:
        new_name = input("new name: ").lower()
        if new_name not in product_names:
            i = product_names.index(name)
            product_names[i] = new_name
            print("Edited!")
        else:
            print("Already Exist!")
    else:
        print("not found!")

def remove(name):
    if name in product_names:
        i = product_names.index(name)
        product_names.pop(i)
        product_is_bought.pop(i)
        product_prices.pop(i)
        print("Removed!")
    else:
        print("Not found!")  

def search(name):
    if name in product_names:
        i = product_names.index(name)
        status = product_is_bought[i]
        price = product_prices[i]
        print(f"Status: {status}, Price: {price}")
    else:
        print("Not found!") 

def details():
    numbers = len(product_names)
    not_purchased = product_is_bought.count(False)
    #purchased = product_is_bought.count(True)
    purchased = sum(product_is_bought)
    #sum_price = sum(product_prices)
    print(f"number of products: {numbers}")
    print(f"Purchased: {purchased}")
    print(f"NOt Purchased: {not_purchased}")
    #print(f"total price: {sum_price}")
    prices = []
    for p in product_prices:
        if p: # bool(50) True, bool(None) False
            prices.append(p)
    sum_price = sum(prices)
    print(f"total price: {sum_price}")

def buy(name):
    if name in product_names:
        i = product_names.index(name)
        #if product_is_bought[i] == False:
        if not product_is_bought[i]:
            price = float(input(f"price of {name}: "))
            product_is_bought[i] = True
            product_prices[i] = price
            print("Done!")
        else:
            print("Invalid!")
    else:
        print("Not Found!")

# main
while True:
    answer = input("add, display, edit, remove, search, details, buy, exit: ")
    answer = answer.lower()
    if answer == "add":
        name = input("product name: ").lower()
        add(name)

    elif answer == "display":
        display()

    elif answer == "edit":
        name = input("name for edit: ").lower()
        edit(name)

    elif answer == "remove":
        name = input("name for remove: ").lower()
        remove(name)

    elif answer == "search":
        name = input("name for search: ").lower()
        search(name)

    elif answer == "buy":
        name = input("name for buy: ").lower()
        buy(name)

    elif answer == "details":
        details()

    elif answer == "exit":
        break

    elif answer == "":
        continue

    else:
        print(f"{answer}: Command not found!")