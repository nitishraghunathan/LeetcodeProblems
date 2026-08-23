-- Write your PostgreSQL query statement below
DELETE FROM Person p1 USING Person P2 WHERE p1.email=p2.email AND p1.id > p2.id