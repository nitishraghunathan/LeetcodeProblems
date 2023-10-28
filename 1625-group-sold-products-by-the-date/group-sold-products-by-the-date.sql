# Write your MySQL query statement below
SELECT sell_date, COUNT(DISTINCT(product), sell_date) as num_sold, GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',') AS products FROM Activities GROUP BY 1
