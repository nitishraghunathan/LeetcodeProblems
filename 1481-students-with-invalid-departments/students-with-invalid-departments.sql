/* Write your T-SQL query statement below */
SELECT id, name FROM Students WHERE Students.department_id NOT IN(
SELECT Departments.id FROM Departments
) 