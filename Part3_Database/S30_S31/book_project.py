import requests
# Book ====> title, authors, genre, img_link 
class Book:
    def __init__(self, title, authors, genre, img_link ):
        self.title = title
        self.authors = authors
        self.genre = genre
        self.img_link = img_link

    def __str__(self):
        # ["A", "B"] =====> "A, B"
        names = ", ".join(self.authors)
        return f"{self.title} by {names}\n{self.genre}{self.img_link}"
    
class BookFetcher:
    def __init__(self, url):
        self.url = url 

    def requests_book_api(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        return []
    
    @staticmethod
    def read_data(book):
        name = book['volumeInfo'].get("title", "No Title!")
        authors = book['volumeInfo'].get("authors",
                                            ['Unknown'])
        genre = book['volumeInfo'].get("categories",
                                        ['Unknown'])[0]
        img_link = book['volumeInfo'].get("imageLinks",
                                            "No Link")
        return name, authors, genre, img_link
        
    def create_book_object(self):
        data = self.requests_book_api()
        if not data:
            print("Not Found!")
            return
        book_items = data["items"]
        books = []
        for book in book_items:
            name, authors, genre, img_link = self.read_data(book)
            book_obj = Book(name, authors, genre, img_link)
            books.append(book_obj)
        return books


if __name__ == "__main__":
    url = "https://www.googleapis.com/books/v1/volumes?q=linux"
    obj1 = BookFetcher(url)
    books = obj1.create_book_object()
    print(books)


