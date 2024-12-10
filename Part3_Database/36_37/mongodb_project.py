from pymongo import MongoClient
from datetime import datetime
import json 
import logging

def read_config():
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
    return config

log_filename = "blog_management.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(log_filename, mode="a"),  
        logging.StreamHandler()                      
    ]
)
logger = logging.getLogger("BlogLogger")

config = read_config()
client = MongoClient(config["connection"])
db = client[config["db_name"]]
users = db[config["users_collection"]]
posts = db[config["posts_collection"]]
logs = db[config["logs"]]
logger.info("Connect to MongoDB.")

def log_to_db(level, msg):
    log_data = {
        "level": level,
        "message": msg,
        "timestamp":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    logs.insert_one(log_data)

#..........Users Operations..............
def register_user():
    username = input("user name: ")
    email = input("Enter Email: ")
    user = users.find_one({"username":username})
    if user:
        logger.warning(f"Failed: Username '{username}' Already Exist!")
        log_to_db("WARNING", f"Failed: Username '{username}' Already Exist!")
        print("username already exist!")
        return 
    user = {
        "username": username,
        "email": email
    }
    result = users.insert_one(user)
    print(f"{result.inserted_id}: Added!")
    logger.info(f"Username '{username}' Added!")
    log_to_db("INFO", f"Username '{username}' Added!")

def view_users():
    print("_"*10 + "Users" + "_"*10)
    all_users = users.find({}, {"_id":0})
    for user in all_users:
        for k, v in user.items():
            print(f"{k} ----> {v}")
        print()
    logger.info("Viewed all users!")
    log_to_db("INFO", "Viewed all users!")


# ------------Post Operations------------
def create_post():
    username = input("username: ")
    user = users.find_one({"username": username})
    if not user:
        logger.warning("user not found!")
        log_to_db("WARNING", "user not found!")
        print("user not found!")
        return
    
    title = input("title: ")
    post = posts.find_one({"title": title})
    if post:
        logger.warning("Title Already exist!")
        log_to_db("WARNING", "Title Already exist!")
        print("Already exist!")
        return
    
    content = input("content: ")
    post = {
        "author": username,
        "title": title,
        "content": content,
        "date": datetime.now()
    }
    result = posts.insert_one(post)
    logger.info(f"POST {result.inserted_id}: Added!")
    log_to_db("INFO", f"POST {result.inserted_id}: Added!")
    print(f"{result.inserted_id}: Added!")

def view_posts():
    print("_"*10 + "POSTS" + "_"*10)
    all_posts = posts.find()
    for post in all_posts:
        for k, v in post.items():
            print(f"{k} ------> {v}")
        print()
    logger.info("Viewed all posts!")
    log_to_db("INFO", "Viewed all posts!")

def update_post():
    title = input("title: ")
    new_title = input("new title: ")
    new_content = input("new content: ")
    result = posts.update_one({"title":title}, 
                     {"$set":{
                         "title": new_title,
                         "content": new_content
                     }})
    if result.matched_count:
        logger.info(f"Post '{title}' Updated!")
        log_to_db("INFO", f"Post '{title}' Updated!")
    else:
        logger.warning(f"Failed: post '{title}' not found!")
        log_to_db("WARNING", f"Failed: post '{title}' not found!")

def delete_post():
    title = input("title: ")
    result = posts.delete_one({"title": title})
    if result.deleted_count:
        logger.info(f"Post '{title}' Removed!")
        log_to_db("INFO", f"Post '{title}' Removed!")
        print("Deleted!")
    else:
        logger.warning(f"Failed: post '{title}' not found!")
        log_to_db("WARNING", f"Failed: post '{title}' not found!")
        print("Post Not Found!")

def remove_user():
    username = input("username: ")
    post_count = posts.delete_many({"author": username}).deleted_count
    result = users.delete_one({"username": username})
    if result.deleted_count:
        logger.info(f"User '{username}' Removed!")
        log_to_db("INFO", f"User '{username}' Removed!")
        print("Deleted!")
    else:
        logger.warning(f"Failed: user '{username}' not found!")
        log_to_db("WARNING", f"Failed: user '{username}' not found!")
        print("User not found!")

# ------------Main----------------
def main_menu():
    while True:
        print("\nBlog Management System")
        print("1. Register user")
        print("2. View users")
        print("3. Create a new post")
        print("4. View all posts")
        print("5. Update a post")
        print("6. Delete a post")
        print("7. Remove User")
        print("8. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            view_users()
        elif choice == '3':
            create_post()
        elif choice == '4':
            view_posts()
        elif choice == '5':
            update_post()
        elif choice == '6':
            delete_post()
        elif choice == '7':
            remove_user()
        elif choice == '8':
            logger.info("Exiting the App.")
            log_to_db("INFO", "Exiting the App.")
            break
        else:
            logger.warning(f"{choice}: Invalid!")
            log_to_db("WARNING", f"{choice}: Invalid!")
            print("Invalid! Please try again.")

if __name__ == "__main__":
    main_menu()