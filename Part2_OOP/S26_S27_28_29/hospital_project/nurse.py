from person import * 

class Nurse(Person):
    last_id = 1000 # class attr
    def __init__(self, name, age, department):
        n_id = Nurse.gen_id()
        super().__init__(name, age, n_id)
        self.department = department

    @classmethod
    def gen_id(cls):
        # D1000, D1001, D1002
        n_id = "N" + str(cls.last_id)
        cls.last_id += 1 
        return n_id
    
    def __str__(self):
        return f"{super().__str__()}, Department: {self.department}"
    
    def des_role(self):
        print(f"{self.name}: is a nurse!")

    def edit_profile(self, name=None, age=None, 
                     department=None):
        #print(f"name: {name}, age:{age}, department:{depatment}")
        super().edit_profile(name, age)
        self.department = department or self.department

    
if __name__ == "__main__":
    n1 = Nurse("n1", 19, "d1")
    n2 = Nurse("n2", 24, "d2")
    print(n1.__dict__)
    print(n2.__dict__)
    n1.edit_profile(age=30)
    print(n1.__dict__)