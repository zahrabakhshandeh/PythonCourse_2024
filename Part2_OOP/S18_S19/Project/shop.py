from item import *
class Shop:
    def __init__(self, name):
        self.name = name 
        self.items = {}

    def creat_item(self, i_id, name, numbers, price):
        new_item = Item(i_id, name, numbers, price)
        return new_item

    def add_item(self, item):
        if item.i_id not in self.items:
            self.items[item.i_id] = item
            print("Added!")
        else:
            print("Exist!")

    def remove_item(self, i_id):
        if i_id in self.items:
            del self.items[i_id]
            print("removed")
        else:
            print("Not Found!") 

    def edit_item(self, i_id):
        if i_id in self.items:
            new_name = input("new name: ") 
            new_price = input("new price: ")
            new_number = input("new number: ")
            item = self.items[i_id]
            item.name = new_name or item.name
            item.price = int(new_price or item.price)
            item.numbers = int(new_number or item.numbers)
            print(item)
        else:
            print("Not Found!")

    def display(self):
        if not self.items:
            print("Empty!")
        for item in self.items.values():
            print(item) 

    def search_item(self, name):
        flag = True
        for item in self.items.values():
            if item.name == name:
                flag = False
                print(item)
        if flag:
            print("Not Found!")

    def details(self):
        number_of_items = len(self.items)
        """total_price = []
        for item in self.items.values():
            total_price.append(item.price)"""
        total_price = [item.price for item in self.items.values()]
        sum_price = sum(total_price)
        max_price, min_price = max(total_price), min(total_price)
        avg = sum_price / number_of_items
        print(f"Number of items: {number_of_items}")
        print(f"Sum:{sum_price}, Min:{min_price}, Max:{max_price}, Avg:{avg}")

if __name__ == "__main__":  
    shop1 = Shop("Shop1")
    item1 = shop1.creat_item("1", "p1", 2, 200)
    item2 = shop1.creat_item("2", "p2", 6, 200)
    shop1.add_item(item1) # obj ------> class Item
    shop1.add_item(item2)
    shop1.search_item("p3")
    #shop1.edit_item("1")
    shop1.details()
    #shop1.display()
    #print(10*"-")
    #shop1.remove_item("2")
    #shop1.display()