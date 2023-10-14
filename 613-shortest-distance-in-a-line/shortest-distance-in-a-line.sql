/* Write your T-SQL query statement below */
SELECT MIN(ABS(T1.x - T2.x)) AS SHORTEST FROM Point as T1, Point as T2  WHERE T1.x != T2.x