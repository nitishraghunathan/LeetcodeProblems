# Write your MySQL query statement below
SELECT COUNT(DISTINCT(customer_id)) as rich_count FROM Store WHERE Store.amount > 500 