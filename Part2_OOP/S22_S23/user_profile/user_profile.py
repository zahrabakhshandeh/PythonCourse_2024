from datetime import datetime
from custom_erros import EnvalidEmailError
# UserProfile
# usename, password, email, age, is_login
# login, logout, update_email, change_password, display 
class UserProfile:
    user_count = 0
    logged_in_users = 0
    logged_out_users = 0
    def __init__(self, usename, password, email, age):
        self.username = usename
        self.password = password
        self.is_valid_email(email)
        self.email = email 
        self.age = age 
        self.is_login = False 
        self.count_login = 0 
        self.logs = []
        UserProfile.user_count += 1

    @staticmethod
    def is_valid_email(email):
        if "." not in email or "@" not in email or len(email) < 5:
            raise EnvalidEmailError("Invalid Email!")
        return True

    def login(self, username, password):
        if username == self.username and password == self.password:
            self.is_login = True 
            print(f"Welcome {self.username}!")
            msg_log = f"logged in at {datetime.now()}"
            UserProfile.logged_in_users += 1 
            self.count_login += 1
        else:
            msg_log = f"your info is not correct!{datetime.now()}"
            print("your info is not correct!")
        self.logs.append(msg_log)

    def logout(self):
        if self.is_login:
            self.is_login = False 
            UserProfile.logged_in_users -= 1
            UserProfile.logged_out_users += 1
            msg_log = f"logged out at {datetime.now()}"
        else:
            msg_log = f"User is not logges in! {datetime.now()}"
            print("User is not logges in!")
        self.logs.append(msg_log)

    def set_email(self, new_email):
        try:
            self.is_valid_email(new_email)
        except ValueError as e:
            print(e)
            msg_log = f"{e}. {datetime.now()}"
        else:
            self.email = new_email
            msg_log = f"Email updated! {datetime.now()}"
        return msg_log

    def update_email(self, new_email):
        if self.is_login:
            msg_log = self.set_email(new_email)
        else:
            msg_log = f"User is not logges in! {datetime.now()}"
            print("User is not logges in!")
        self.logs.append(msg_log)

    def change_password(self, new_password):
        if self.is_login:
            self.password = new_password 
            msg_log = f"Password updated. {datetime.now()}"
        else:
            msg_log = f"User is not logges in! {datetime.now()}"
            print("User is not logges in!")
        self.logs.append(msg_log)

    def show_logs(self):
        if self.is_login:
            result = "\n".join(self.logs)
            print(result)
            msg_log = f"Show Logs. {datetime.now()}"
        else:
            msg_log = f"User is not logges in! {datetime.now()}"
            print("User is not logges in!")
        self.logs.append(msg_log)

    def show_info(self):
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"IsLogin: {self.is_login}")
        print(10*"-"+"2 last logs"+10*"-")
        result = "\n".join(self.logs[:2])
        print(result)
        msg_log = f"Display: {datetime.now()}"
        return msg_log
    
    def display(self):
        if self.is_login:
            password = input("enter your password: ")
            print(password, self.password)
            if password == self.password:
                msg_log = self.show_info(self)
            else:
                print("Error!")
                msg_log = f"Error! {datetime.now()}"
        else:
            msg_log = f"User is not logges in! {datetime.now()}"
            print("User is not logges in!")
        self.logs.append(msg_log)

    @classmethod
    def number_of_users(cls):
        print(f"Number Of Users: {cls.user_count}")
        print(f"Logged in Users: {cls.logged_in_users}")
        print(f"Logged out Users: {cls.logged_out_users}")


if __name__ == "__main__":
    username = input("username: ")
    password = input("password: ")
    age = int(input("age: "))
    email = input("email: ")
    u1 = UserProfile(username, password, email, age)
    print(u1.__dict__)
    print()
    u1.login("u1", "p1")
    #new_email = input("new email: ")
    #u1.update_email(new_email)
    u1.change_password("new")
    print(20*"-")
    u1.show_logs()
    u1.display()
    u1.number_of_users()
    """print(u1.__dict__)
    print()
    u1.logout()
    print(u1.__dict__)"""

