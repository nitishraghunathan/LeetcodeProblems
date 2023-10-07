/* Write your T-SQL query statement below */
SELECT Employee.employee_id, a.team_size FROM Employee JOIN (
SELECT team_id, COUNT(Employee.employee_id) AS team_size FROM
Employee GROUP BY Employee.team_id) AS a ON Employee.team_id=a.team_id
