-- Write your PostgreSQL query statement below
SELECT DISTINCT e.email FROM Person e JOIN Person m ON e.email=m.email WHERE e.id !=m.id
