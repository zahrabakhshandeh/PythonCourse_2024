# Part 3 — APIs & Databases

Working with REST APIs, MySQL, and MongoDB through real projects.

## Sessions

| Sessions | Topic | Project |
|----------|-------|---------|
| S30 – S31 | REST APIs & `requests` | Google Books API Client |
| S32 – S33 | MySQL basics | — |
| S34 – S35 | MySQL with Python (`mysql-connector`) | Blog Post Manager |
| S36 – S37 | MongoDB with Python (`pymongo`) | Blog Management System |
| —  | Capstone | Library Management System |

## Projects

**Google Books API Client** (`S30_S31/book_project.py`)
> Fetches and parses book data from the Google Books API using OOP.

**Blog Post Manager** (`S34_S35/`)
> MySQL-backed CLI to create, read, update, and delete posts.

**Blog Management System** (`36_37/mongodb_project.py`)
> MongoDB-backed app with user registration, post CRUD, and dual logging (file + DB).

**Library Management System** (`LibraryManagementSystem/`)
> Full MySQL project with separate models for `Book`, `Member`, and `Employee`. Generic `DB` class handles all queries.

```
LibraryManagementSystem/
├── database.py       # Generic DB class (add, remove, update, search)
├── main.py
└── Models/
    ├── book.py
    ├── member.py
    └── employee.py
```

## Requirements

```bash
pip install mysql-connector-python pymongo requests
```
