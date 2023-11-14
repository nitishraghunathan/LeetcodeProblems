/* Write your T-SQL query statement below */
SELECT A.email FROM (SELECT email, COUNT(email) AS email_count FROM Person GROUP BY email) AS A WHERE A.email_count>1