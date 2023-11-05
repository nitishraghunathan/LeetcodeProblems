/* Write your T-SQL query statement below */
-- SELECT A.mark - A.eng AS salary_difference FROM (SELECT MAX(salary) AS mark FROM Salaries WHERE department="Marketing" UNION
-- SELECT MAX(salary) AS eng FROM Salaries WHERE department="Engineering") AS A
 
SELECT Abs(
    (SELECT MAX(salary) AS mark FROM Salaries WHERE department='Marketing')-
    (SELECT MAX(salary) AS eng FROM Salaries WHERE department='Engineering'
)) AS salary_difference;

