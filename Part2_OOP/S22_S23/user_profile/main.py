from user_profile import *
def main():
    # Create a user profile instance
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    age = int(input("Enter your age: ").strip())
    email = input("Enter your email: ").strip()

    user_profile = UserProfile(username, password, email, age)
    print(f"User {username} created successfully!\n")

    while True:
        print("\nSelect an option:")
        print("1. Login")
        print("2. Logout")
        print("3. Update Email")
        print("4. Change Password")
        print("5. Show Logs")
        print("6. Display User Info")
        print("7. Show Number of Users")
        print("Type 'exit' to quit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            uname = input("Enter your username: ").strip()
            pwd = input("Enter your password: ").strip()
            user_profile.login(uname, pwd)

        elif choice == "2":
            user_profile.logout()

        elif choice == "3":
            new_email = input("Enter new email: ").strip()
            user_profile.update_email(new_email)

        elif choice == "4":
            new_password = input("Enter new password: ").strip()
            user_profile.change_password(new_password)

        elif choice == "5":
            user_profile.show_logs()

        elif choice == "6":
            user_profile.display()

        elif choice == "7":
            UserProfile.number_of_users()

        elif choice.lower() == "exit":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()

