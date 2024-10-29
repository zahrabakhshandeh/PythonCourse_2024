from doctor import * 
from patient import *
from nurse import * 

class Hospital:
    def __init__(self, name):
        self.name = name 
        self.objects = { # nurss
            "doctors":{},
            "nurses":{},
            "patients":{}
        }

    def add_data(self, obj):
        type_obj = type(obj).__name__.lower() + "s"
        self.objects[type_obj][obj.id_] = obj
        print("Added!")

    @staticmethod
    def show_info(data, obj_type):
        print("\n"+"_"*10 + obj_type + "_"*10)
        for v in data.values(): # {"D1000":obj1}
            print(v)
        if not data:
            print("empty")


    def display(self, obj_type=None):
        if obj_type:
            obj_type += "s"
            #data = self.objects[obj_type]
            #data = self.objects.get(obj_type, "Not Found")
            try:
               data = self.objects[obj_type]
            except:
                print("Not Found!") 
            else:
                self.show_info(data, obj_type)
        else:
            for k, data in self.objects.items(): # 3
                self.show_info(data, k)

    def remove(self, obj_id):
        for group in self.objects.values():
            if obj_id in group:
                del group[obj_id]
                return f"{obj_id}: removed"
        return "Not Found!"
    
    def search(self, **var):
        result = []
        for group in self.objects.values(): # 3
            for obj in group.values(): # name=n1, age=28
                flag = True
                for attr, value in var.items():
                    # {name:"n2", "age":18}
                    # name ====> n1
                    #obj."name" == "Ali"
                    if getattr(obj, attr, None) != value:
                        flag = False
                        break
                if flag:
                    result.append(obj)
        return result


if __name__ == "__main__":
    d1 = Doctor("d1", 29)
    d2 = Doctor("d2", 29)
    h1 = Hospital("h1")
    h1.add_data(d1)
    h1.add_data(d2)
    #h1.display() # None
    #h1.display("doctor")
    result = h1.remove("D1007")
    #print(result)
    #print(40*"*")
    #h1.display("doctor")
    h1.search(name="d1", age=17)
    """print(h1.objects) # dict
    print(h1.objects["doctors"]) # dict
    print(h1.objects["doctors"]["D1000"]) # object ===> Doctor
    print(h1.objects["doctors"]["D1000"].__dict__)"""
