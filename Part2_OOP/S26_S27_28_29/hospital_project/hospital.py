from doctor import * 
from patient import *
from nurse import * 

class Hospital:
    def __init__(self, name):
        self.name = name 
        self.objects = { # nurses
            "doctors":{},
            "nurses":{},
            "patients":{}
        }

    def add_data(self, obj):
        type_obj = type(obj).__name__.lower() + "s"
        self.objects[type_obj][obj.id_] = obj

    @staticmethod
    def show_info(data, obj_type):
        print("\n"+"_"*10 + obj_type + "_"*10)
        for v in data.values(): # {"D1000":obj1}
            print(v)
        if not data:
            print("empty")


    def display(self, obj_type=None): #obj_type="doctor"
        if obj_type:
            obj_type += "s" # doctors
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
    
    def search1(self, name, age):
        result = []
        for group in self.objects.values():
            for obj in group.values():
                if obj.name == name and obj.age == age:
                    result.append(obj)
        return result
    
    def search2(self, **var):
        # {"name":"A", "age":19}
        result = []
        for group in self.objects.values():
            for obj in group.values():
                flag = True
                for attr, value in var.items():
                    # obj.name
                    # obj."name"
                    if getattr(obj, attr, None) != value:
                        flag = False
                        break
                if flag:
                    result.append(obj)
        return result
    
    def edit_data(self, obj_id, **args):
        print(args) # {'name': 'New Name', 'age': 51}
        for group in self.objects.values():
            if obj_id in group:
                obj = group[obj_id]
                print(obj)
                obj.edit_profile(**args)
                return f"{obj_id} updated!"
        return f"{obj_id} not found!"


if __name__ == "__main__":
    d1 = Doctor("d1", 49)
    d2 = Doctor("d1", 29)
    n1 = Nurse("n1", 19, "d1")
    h1 = Hospital("h1")
    hospital2 = Hospital("new")
    hospital2.add_data(d2)
    h1.add_data(d1)
    h1.add_data(d2)
    h1.add_data(n1)
    #h1.display() # None
    #h1.display("doctor")
    result = h1.remove("D1007")
    #print(result)
    #print(40*"*")
    #h1.display("doctor")
    result = h1.search2(name="d1")
    #for obj in result:
    #    print(obj)
    print(n1)
    result = h1.edit_data("N1000", name="New Name",
                           age=50, department="d3")
    print(result)
    print(n1)
    #result = h1.search1("d1", 29)
    #print(result)
    """print(h1.objects) # dict
    print(h1.objects["doctors"]) # dict
    print(h1.objects["doctors"]["D1000"]) # object ===> Doctor
    print(h1.objects["doctors"]["D1000"].__dict__)"""
