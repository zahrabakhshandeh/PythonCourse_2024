from shop import *
def main():
    manager1 = Shop("shop1")
    #manager2 = Shop("shop2")
    while True:
        cmd = input("add/remove/edit/display/search/detail/exit: ")
        if cmd == "add":
            id_i, name, numbers, price = input("id,name,number,price: ").split(",")
            item1 = manager1.creat_item(id_i, name, 
                                        int(numbers), int(price))
            manager1.add_item(item1)

        elif cmd == "edit":
            id_i = input("id for edit: ")
            manager1.edit_item(id_i)

        elif cmd == "remove":
            id_i = input("id for remove: ")
            manager1.remove_item(id_i)

        elif cmd == "display":
            manager1.display()

        elif cmd == "search":
            name = input("name for search: ")
            manager1.search_item(name)

        elif cmd == "detail":
            manager1.details()
            
        elif cmd == "exit":
            break
        elif cmd == "":
            continue
        else:
            print(f"{cmd}: not found!")
if __name__ == "__main__":
    main()