class Item:
    def __init__(self, id_, name, numbers, price):
        self.i_id = id_ 
        self.name = name 
        self.numbers = numbers
        self.price = price 

    def __str__(self):
        return f"ID:{self.i_id}, Name:{self.name}, Numbers:{self.numbers}, Price:{self.price}"

if __name__ == "__main__":  
    id_ = input("id: ")  
    p1 = Item(id_, "P1", 7, 1000)
    print(p1)