class Employee:
    def __init__(self, employee_id, first_name, last_name, position, salary, email):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.salary = salary
        self.email = email

    def __str__(self):
        return f"ID: {self.employee_id}, Name: {self.first_name} {self.last_name}, Position: {self.position}, Salary: {self.salary}, Email: {self.email}"
