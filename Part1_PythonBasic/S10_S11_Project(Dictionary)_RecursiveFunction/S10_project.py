inventory = {} # key ---> id, value ----> dict --> name, price, quantity

def display_menu():
    menu = """
    Inventory Management System:
    1. Add Product
    2. Update Product
    3. Delete Product
    4. Search Product
    5. Display All Products
    6. Exit
    """
    print(menu)

def add_product():
    p_id = input("product id: ").strip()
    if p_id in inventory:
        print("Id is already exist!")
        return 
    p_name = input("product name: ")
    quantity = int(input("quantity: "))
    price = int(input("price: "))
    product = {
        "name": p_name,
        "quantity": quantity,
        "price": price
    }    
    inventory[p_id] = product
    print("Added!")

def remove(p_id):
    if p_id in inventory:
        inventory.pop(p_id)
        print("Removed!") 
        return
    print("Not found")

def update_product(p_id):
    # inventory = {"1":{"name":"p1", "price":200, "quantity":4}}
    # p_id = "1"
    if p_id not in inventory: # False
        print("Not found")
        return
    
    new_name = input("new name: ") # p2
    new_price = input("price: ") # ""
    new_quantity = input("quantity: ") # "12"
    inventory[p_id]["name"] = new_name or inventory[p_id]["name"]
    inventory[p_id]["price"] = int(new_price or inventory[p_id]["price"])
    inventory[p_id]["quantity"] = int(new_quantity or inventory[p_id]["quantity"])
    # inventory = {"1":{"name":"p2", "price":200, "quantity":12}}
    print("Updated!")

def display_product(product):
    for k, v in product.items():
        print(f"{k}: {v}")

def search_by_id(p_id):
    if p_id in inventory:
        product = inventory[p_id]
        display_product(product)
    else:
        print("Not Found!")
    
def search_by_name(name):
    not_found = True
    """inventory = 
    {"1":{"name":"p1", "price":200, "quantity":4},
    {"2":{"name":"p2", "price":200, "quantity":4},
    {"3":{"name":"p3", "price":200, "quantity":4}
    }"""
    for p in inventory.values():
        # name = 'p3'
        # p = {"name":"p1", "price":200, "quantity":4}
        # p = {"name":"p2", "price":200, "quantity":4}
        # p = {"name":"p3", "price":200, "quantity":4}
        if p["name"] == name:
            not_found = False
            display_product(p)
            print()
    if not_found:
        print("Not found!")
            
def search_by_price(start_price=0, end_price=float('inf')):
    not_found = True
    for p in inventory.values():
        if start_price <= p["price"] <= end_price:
            not_found = False
            display_product(p)
            print()
    if not_found:
        print("Not found!")    

def search_product():
    s_option = input("1: id, 2: name, 2: price range: ").strip()
    if s_option == "1":
        p_id = input("product id: ")
        search_by_id(p_id)
    elif s_option == "2":
        name = input("name: ")
        search_by_name(name)
    elif s_option == "3":
        search_by_price(end_price=400)
    else:
        print("Not found!")
    

def display_all_products():
   if not inventory:
       print("Empty")

   for key, value in inventory.items(): # inventory
       print(5*"*"+key+5*"*") #key
       display_product(value)

def main():

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_product()

        elif choice == "2":
            p_id = input("id for edit: ")
            update_product(p_id)

        elif choice == "3":
            p_id = input("id for remove: ")
            remove(p_id)

        elif choice == "4":
            search_product()
        elif choice == "5":
            display_all_products()
        elif choice == "6":
            break
        elif choice == "":
            continue
        else:
            print("Invalid option. Please try again.")


main()