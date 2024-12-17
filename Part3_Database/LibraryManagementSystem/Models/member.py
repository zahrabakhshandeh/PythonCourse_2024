class Member:
    def __init__(self, member_id, first_name, last_name, email, phone, address):
        self.member_id = member_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address

    def __str__(self):
        return f"ID: {self.member_id}, Name: {self.first_name} {self.last_name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}"
