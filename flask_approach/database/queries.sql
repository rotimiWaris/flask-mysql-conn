-- Get All Products in a Specific Category

SELECT Product.ProductID, Product.ProductName, Product.Price, Category.CategoryName
FROM Product
INNER JOIN Category ON Product.CategoryID = Category.CategoryID
WHERE Category.CategoryID = 1;

-- Insert Sample Data

INSERT INTO Customer (FirstName, LastName, Email, PhoneNumber, Address, Password)
VALUES 
('John', 'Doe', 'john.doe@example.com', '1234567890', '123 Main St', 'password123'),
('Jane', 'Smith', 'jane.smith@example.com', '0987654321', '456 Elm St', 'password456');

INSERT INTO Category (CategoryName, Description)
VALUES 
('Electronics', 'Devices and gadgets'),
('Clothing', 'Apparel and accessories');

INSERT INTO Product (ProductName, Description, Price, StockQuantity, CategoryID)
VALUES 
('Smartphone', 'Latest model smartphone', 699.99, 50, 1),
('Laptop', 'High-performance laptop', 1299.99, 30, 1),
('T-Shirt', 'Cotton t-shirt', 19.99, 100, 2);

























-- Retrieve all columns and rows from the table.
SELECT * FROM Student;

-- Retrieve only specific columns from the table
SELECT FirstName, LastName, Email FROM Student;-

-- Retrieve rows that meet a specific condition
SELECT * FROM Student WHERE Department = 'Computer Science';

-- Sort the results in ascending order.
SELECT * FROM Student ORDER BY LastName;

-- Sort the results in descending order
SELECT * FROM Student ORDER BY DateOfBirth DESC;

-- Retrieve the first 5 students
SELECT * FROM Student LIMIT 5;

/*  Use AND, OR, and NOT to combine conditions */
-- Students in Computer Science or Electrical Engineering
SELECT * FROM Student 
WHERE Department = 'Computer Science' OR Department = 'Electrical Engineering';

-- Students with an email containing 'gmail.com'
SELECT * FROM Student WHERE Email LIKE '%gmail.com%';

/*
-- Count the total number of students
SELECT COUNT(*) AS TotalStudents FROM Student;
*/

-- Find the oldest student's birth date
SELECT MIN(DateOfBirth) AS OldestStudent FROM Student;

/*
-- Count the number of students in each department
SELECT Department, COUNT(*) AS NumberOfStudents FROM Student GROUP BY Department;
*/

/*
-- Update the department of a specific student
UPDATE Student SET Department = 'Electrical Engineering' WHERE StudentID = 1;
*/

/*
-- Delete a specific student
DELETE FROM Student 
WHERE StudentID = 1;

-- Delete all students in a specific department
DELETE FROM Student 
WHERE Department = 'Mechanical Engineering';
*/

/*
-- Insert a new student
INSERT INTO Student (FirstName, LastName, DateOfBirth, Email, Department)
VALUES ('John', 'Doe', '2000-01-15', 'john.doe@example.com', 'Computer Science');
*/

/*
-- Delete an entire table from the database.
DROP TABLE Course;
*/