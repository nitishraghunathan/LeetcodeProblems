/* Write your T-SQL query statement below */
/*
unique orders, unique customers and for every month
*/

SELECT FORMAT(order_date, 'yyyy-MM') AS month, COUNT(DISTINCT(order_id)) AS order_count,  COUNT(DISTINCT(customer_id)) AS customer_count FROM Orders WHERE invoice > 20 GROUP BY FORMAT(order_date, 'yyyy-MM')