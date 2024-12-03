import mysql.connector
# post: id, title, content, category
class Post:
    def __init__(self, id_, content,
                  title, category):
        self.id_ = id_
        self.content = content
        self.title = title
        self.category = category
    
    def __str__(self):
        data = f"name:{self.title}, content:{self.content}"
        return data 
    
class DB:
    def __init__(self, user, password, 
                 host, database):
        self.user = user 
        self.password = password 
        self.host = host 
        self.databse = database
        self.connect = None 
    
    def connnection(self):
        self.connect = mysql.connector.connect(
            user = self.user,
            password = self.password,
            host = self.host,
            database = self.databse
        )

    def execute_query(self, query, data=None, 
                      fetch=False):
        try:
            self.connnection() 
            mycursor = self.connect.cursor() 
            mycursor.execute(query, data)
        except Exception as e:
            print(e)
        else:
            if fetch:
                data = mycursor.fetchall()
                return data
            affected_rows = mycursor.rowcount
            self.connect.commit()
            return affected_rows
        finally:
            if self.connect.is_connected():
                mycursor.close()
                self.connect.close()

    def add_data(self, post):
        query = "INSERT INTO posts VALUES (%s, %s, %s, %s)"
        data = (post.id_, post.content, post.title, 
                post.category)
        self.execute_query(query, data=data)

    def remove_data(self, p_id):
        query = "DELETE FROM posts WHERE p_id=%s"
        data = (p_id,)
        result = self.execute_query(query, data=data)
        if result:
            print(f"Post with Id {p_id} removed!")
        else:
            print("No record found!")

    def display_posts(self):
        query = "SELECT * FROM posts"
        result = self.execute_query(query, fetch=True)
        print(result)

    def update_data(self, id_p, data_column, name_column):
        query = f"""
                    UPDATE posts 
                    SET {name_column}=%s
                    WHERE p_id=%s
                """
        data = (data_column, id_p)
        result = self.execute_query(query, data=data)
        if result:
            print(f"Post with Id {id_p} updated!")
        else:
            print("No record found!")


if __name__ == "__main__":
    obj1 = DB("root", "pass", "localhost", 
              "DBblog")
    post1 = Post("1", "content1", "title1", "c1")
    obj1.add_data(post1)
    #print(obj1.connect.is_connected())
    #obj1.remove_data("1")
    obj1.display_posts()
    obj1.update_data("1", "title5", "title")
    obj1.display_posts()
