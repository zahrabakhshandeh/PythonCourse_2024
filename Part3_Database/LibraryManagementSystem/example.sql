-- Create the Database and Tables
CREATE DATABASE UniversitySystem_1;

USE UniversitySystem_1;

-- Students Table
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DateOfBirth DATE,
    Email VARCHAR(100)
);

-- Courses Table
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100),
    Instructor VARCHAR(50)
);

-- Enrollments Table
CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    EnrollmentDate DATE,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

-- Insert data into Students table
INSERT INTO Students (StudentID, FirstName, LastName, DateOfBirth, Email)
VALUES
(1, 'Ali', 'Ara', '2000-01-15', 'Ali.Ara@example.com'),
(2, 'Sara', 'karimi', '1999-12-10', 'Sara.karimi@example.com'),
(3, 'Diana', 'salehi', '2001-05-22', 'Diana.salehi@example.com');

-- Insert data into Courses table
INSERT INTO Courses (CourseID, CourseName, Instructor)
VALUES
(101, 'Introduction to Java', 'Prof. A'),
(102, 'Advanced Python Programming', 'Dr. B'),
(103, 'Database Management', 'Dr. C');

-- Insert data into Enrollments table
INSERT INTO Enrollments (EnrollmentID, StudentID, CourseID, EnrollmentDate)
VALUES
(1, 1, 101, '2024-01-01'),
(2, 1, 102, '2024-01-02'),
(3, 2, 103, '2024-01-03'),
(4, 3, 101, '2024-01-04'),
(5, 3, 102, '2024-01-05');

-- Example: Using GROUP BY
-- Find the number of courses each instructor is teaching
SELECT 
    Instructor,
    COUNT(CourseID) AS NumberOfCourses
FROM 
    Courses
GROUP BY 
    Instructor;

-- Query to Find Students and Course Counts
SELECT 
    s.FirstName,
    s.LastName,
    COUNT(e.CourseID) AS NumberOfCourses
FROM 
    Students s
LEFT JOIN 
    Enrollments e ON s.StudentID = e.StudentID
GROUP BY 
    s.StudentID, s.FirstName, s.LastName;

-- Remove Students Enrolled in Less Than 2 Courses
-- Step 1: Create a temporary table to store StudentIDs
CREATE TEMPORARY TABLE TempStudentIDs AS
SELECT 
    s.StudentID
FROM 
    Students s
LEFT JOIN 
    Enrollments e ON s.StudentID = e.StudentID
GROUP BY 
    s.StudentID
HAVING 
    COUNT(e.CourseID) < 2;

-- Step 2: Delete associated rows from the Enrollments table
DELETE FROM Enrollments
WHERE StudentID IN (SELECT StudentID FROM TempStudentIDs);

-- Step 3: Delete students from the Students table
DELETE FROM Students
WHERE StudentID IN (SELECT StudentID FROM TempStudentIDs);

-- Step 4: Drop the temporary table (optional)
DROP TEMPORARY TABLE TempStudentIDs;

-- Update Courses with "Java" to "Python"
UPDATE Courses
SET CourseName = REPLACE(CourseName, 'Java', 'Python')
WHERE CourseName LIKE '%Java%';

-- Confirm the Update
SELECT * FROM Courses;