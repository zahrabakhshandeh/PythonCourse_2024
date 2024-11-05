from doctor import Doctor
from nurse import Nurse
from patient import Patient
from hospital import Hospital

def main():
    hospital = Hospital("City Hospital")

    while True:
        print("\n--- Hospital Management System ---")
        print("1. Add Doctor")
        print("2. Add Nurse")
        print("3. Add Patient")
        print("4. Display All")
        print("5. Display Specific Type")
        print("6. Edit Profile")
        print("7. Remove Profile")
        print("8. Search")
        print("9: Search by name and age")
        print("10. Exit")

        choice = input("Choose an option (1-9): ")

        if choice == '1':
            name = input("Enter doctor's name: ")
            age = int(input("Enter age: "))
            doctor = Doctor(name, age)
            hospital.add_data(doctor)
            print("Doctor Added!")

        elif choice == '2':
            name = input("Enter nurse's name: ")
            age = int(input("Enter age: "))
            department = input("Enter department: ")
            nurse = Nurse(name, age, department)
            hospital.add_data(nurse)
            print("Nurse Added!")
        
        elif choice == '3':
            name = input("Enter patient's name: ")
            age = int(input("Enter age: "))
            history = input("Enter the history: ")
            patient = Patient(name, age, history)
            hospital.add_data(patient)
            print("patient Added!")
        
        elif choice == '4':
            hospital.display()
        
        elif choice == '5':
            obj_type = input("Enter object type: ")
            hospital.display(obj_type)
        
        elif choice == '6':
            obj_id = input("Enter object id for edit: ")
            name = input("Enter new name: ")
            age = input("Enter new age: ")
            age = int(age) if age else None 
            vars = {"name":name, "age":age}

            if obj_id.startswith("N"):
                extra_file = input("new department: ")
                vars["department"] = extra_file
                
            result = hospital.edit_data(obj_id, **vars)
            print(result)

        elif choice == '7':
            obj_id = input("Enter object id for remove: ")
            result = hospital.remove(obj_id)
            print(result)
        
        elif choice == '8':
            fields = ["name", "age", "department"]
            vars = {}
            for i in fields:
                # i = "name", "age", "department"
                value = input(f"value for {i} or blank: ")
                # value = "a", "15", ""
                if i == "age" and value:
                    vars[i] = int(value) 
                    # {"name":"a", "age":15}
                elif value:
                    vars[i] = value # {"name":"a"}
            
            result = hospital.search2(**vars)
            for obj in result:
                print(obj)

        elif choice == "9":
            name = input("name: ")
            age = input("age: ")
            hospital.search1(name, age)

        elif choice == '10':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
