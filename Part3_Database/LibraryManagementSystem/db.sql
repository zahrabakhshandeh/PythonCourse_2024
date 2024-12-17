-- Create the LibraryDB database
CREATE DATABASE IF NOT EXISTS LibraryDB;

-- Use the created database
USE LibraryDB;

-- Create the Members table
CREATE TABLE Members (
    MemberID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    PhoneNumber VARCHAR(15),
    Address TEXT
);

-- Create the Employees table
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Position VARCHAR(50),
    Salary DECIMAL(10, 2),
    Email VARCHAR(100) NOT NULL UNIQUE
);

-- Create the Books table
CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(100) NOT NULL,
    Author VARCHAR(100) NOT NULL,
    PublicationYear INT,
    Genre VARCHAR(50),
    CopiesAvailable INT DEFAULT 1
);
