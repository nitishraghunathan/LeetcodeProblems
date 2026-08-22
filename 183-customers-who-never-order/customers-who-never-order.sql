-- Write your PostgreSQL query statement below
SELECT A.name AS Customers FROM (SELECT c.name, o.id FROM Customers c FULL JOIN Orders o ON o.customerId=c.id) as A WHERE A.id IS NULL