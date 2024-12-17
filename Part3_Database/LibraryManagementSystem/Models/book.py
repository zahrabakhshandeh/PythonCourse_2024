class Book:
    def __init__(self, book_id, title, author, year, genre, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.copies = copies

    def __str__(self):
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Year: {self.year}, Genre: {self.genre}, Copies: {self.copies}"
