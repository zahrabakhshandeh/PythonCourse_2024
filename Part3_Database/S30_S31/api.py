import requests
url = "https://www.googleapis.com/books/v1/volumes?q=linux"
response = requests.get(url)
#print(response.status_code)
#print(response.ok)
if response.status_code == 200:
    data = response.json()
else:
    print(f"{response.status_code}:Failed!")

#print(data["totalItems1"])
print(data.get("totalItems1", "Not Found"))
books = data["items"]
print(type(books))
"""print(books[0]["volumeInfo"].keys())

for book in books:
    print(book["volumeInfo"]["title"])"""