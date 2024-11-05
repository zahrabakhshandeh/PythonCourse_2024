from person import * 

class Patient(Person):
    last_id = 1000
    def __init__(self, name, age, histoty):
        p_id = Patient.gen_id()
        super().__init__(name, age, p_id)
        self.__histoy = histoty   # private

    @property
    def history(self):
        return self.__histoy
    
    @history.setter
    def history(self, new_history):
        if new_history != None and isinstance(new_history, str):
            self.__histoy = new_history
        else:
            raise ValueError("Invalid!")

    @classmethod
    def gen_id(cls):
        # D1000, D1001, D1002
        p_id = "P" + str(cls.last_id)
        cls.last_id += 1 
        return p_id
    
    def des_role(self):
        print(f"{self.name}: is a patient!")

if __name__ == "__main__":
    p1 = Patient("p1", 18, "h1")
    p2 = Patient("p2", 29, "h2")
    print(p1.__dict__)
    print(p2.__dict__)
    print(p1.history)
    print(p1.name)
    p1.name = "new name"
    print(p1.__dict__)
    p1.history = "new history"
    print(p1.__dict__)
