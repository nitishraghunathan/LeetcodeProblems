/* Write your T-SQL query statement below */
SELECT Sales.product_id, SUM(Sales.quantity) AS total_quantity FROM Sales JOIN Product ON Sales.product_id = Product.product_id
GROUP BY Sales.product_id