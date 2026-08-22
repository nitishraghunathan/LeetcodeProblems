-- Write your PostgreSQL query statement below
SELECT c.name as Customers FROM Customers c FULL JOIN Orders o ON o.customerId=c.id WHERE o.id IS NULL