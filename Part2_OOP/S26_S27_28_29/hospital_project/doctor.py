from person import * 

class Doctor(Person):
    last_id = 1000 
    def __init__(self, name, age):
        d_id = Doctor.gen_id()
        super().__init__(name, age, d_id)

    @classmethod
    def gen_id(cls):
        # D1000, D1001, D1002
        d_id = "D" + str(cls.last_id)
        cls.last_id += 1 
        return d_id
    
    def des_role(self):
        print(f"{self.name}: is a doctor!")

    
    
if __name__ == "__main__":
    d1 = Doctor("n1", 39)
    d2 = Doctor("n2", 28)
    print(d1.__dict__)
    print(d2.__dict__)