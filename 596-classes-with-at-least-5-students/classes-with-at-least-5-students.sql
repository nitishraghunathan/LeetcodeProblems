-- Write your PostgreSQL query statement below
SELECT Courses.class FROM Courses Group By Courses.class Having Count(Courses.student) >= 5 