from posts import *

def main(obj1):
    while True:
        print("\nSelect an option:")
        print("1. Add Post")
        print("2. Remove Post")
        print("3. List Posts")
        print("4. Update Post")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            try:
                id_ = int(input("Enter Post ID: "))
                title = input("Enter Post Title: ")
                content = input("Enter Post Content: ")
                category = input("Enter Post Category: ")
                post = Post(id_, content, title, category)
                obj1.add_data(post)
            except ValueError:
                print("Invalid input! Please try again.")
        
        elif choice == "2":
            try:
                p_id = int(input("Enter Post ID to remove: "))
                obj1.remove_data(p_id)
            except ValueError:
                print("Invalid input! Please try again.")
        
        elif choice == "3":
            posts = obj1.display_posts()
            if posts:
                for post in posts:
                    print(f"ID: {post[0]}, Title: {post[1]}, Content: {post[2]}, Category: {post[3]}")
            else:
                print("No posts found.")
        
        elif choice == "4":
            try:
                id_p = int(input("Enter Post ID to update: "))
                column = input("Enter the column to update (title/content/category): ")
                new_value = input("Enter the new value: ")
                obj1.update_data(id_p, new_value, column)
            except ValueError:
                print("Invalid input! Please try again.")
        
        elif choice == "5":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    obj1 = DB("root", "pass", "localhost", "DBblog")
    main(obj1)