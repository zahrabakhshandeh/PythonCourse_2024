from database import DB
from Models.member import Member
from Models.employee import Employee
from Models.book import Book

def main():
    db = DB("root", "pass", "localhost", "LibraryDB")

    while True:
        print("\nLibrary Management System")
        print("1. Register New Library Member")
        print("2. Remove a Member")
        print("3. Show Member Profile Details")
        print("4. Add New Employee")
        print("5. Show Employee Details")
        print("6. Add New Book")
        print("7. Update Book Information")
        print("8. Search Books by Title")
        print("9. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":  # Register New Library Member
            member_id = int(input("Enter Member ID: "))
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            email = input("Enter Email: ")
            phone = input("Enter Phone Number: ")
            address = input("Enter Address: ")
            member = Member(member_id, first_name, last_name, email, phone, address)
            db.add("Members", 
                   (member.member_id, member.first_name, member.last_name, member.email, member.phone, member.address))
            print("Member added successfully!")

        elif choice == "2":  # Remove a Member
            member_id = int(input("Enter Member ID to Remove: "))
            db.remove("Members", f"MemberID={member_id}")
            print("Member removed successfully!")

        elif choice == "3":  # Show Member Profile Details
            member_id = int(input("Enter Member ID: "))
            member = db.search("Members", f"MemberID={member_id}")
            if member:
                print(Member(*member[0]))
            else:
                print("No member found.")

        elif choice == "4":  # Add New Employee
            employee_id = int(input("Enter Employee ID: "))
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            position = input("Enter Position: ")
            salary = float(input("Enter Salary: "))
            email = input("Enter Email: ")
            employee = Employee(employee_id, first_name, last_name, position, salary, email)
            db.add("Employees", (employee.employee_id, employee.first_name, employee.last_name, employee.position, employee.salary, employee.email))
            print("Employee added successfully!")

        elif choice == "5":  # Show Employee Details
            employee_id = int(input("Enter Employee ID: "))
            employee = db.search("Employees", f"EmployeeID={employee_id}")
            if employee:
                print(Employee(*employee[0]))
            else:
                print("No employee found.")

        elif choice == "6":  # Add New Book
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author: ")
            year = int(input("Enter Publication Year: "))
            genre = input("Enter Genre: ")
            copies = int(input("Enter Copies Available: "))
            book = Book(book_id, title, author, year, genre, copies)
            db.add("Books", (book.book_id, book.title, book.author, book.year, book.genre, book.copies))
            print("Book added successfully!")

        elif choice == "7":  # Update Book Information
            book_id = int(input("Enter Book ID to Update: "))
            column = input("Enter the column to update (Title/Author/Year/Genre/Copies): ")
            new_value = input("Enter the new value: ")
            db.update("Books", {column: new_value}, f"BookID={book_id}")
            print("Book updated successfully!")

        elif choice == "8":  # Search Books by Title
            title = input("Enter part of the book title to search: ")
            books = db.search("Books", f"Title LIKE '%{title}%'")
            if books:
                for book in books:
                    print(Book(*book))
            else:
                print("No books found.")

        elif choice == "9":  # Exit
            print("Exiting Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
