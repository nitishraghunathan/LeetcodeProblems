/* Write your T-SQL query statement below */

SELECT A.NAME, A.BALANCE  FROM (SELECT Users.name AS NAME, SUM(Transactions.amount) AS BALANCE FROM Users JOIN Transactions ON Users.account=Transactions.account GROUP BY Users.name) AS A WHERE A.BALANCE >10000