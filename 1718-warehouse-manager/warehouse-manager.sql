/* Write your T-SQL query statement below */
SELECT A.warehouse_name, SUM(A.Volume) as volume FROM (SELECT Warehouse.name as warehouse_name, Products.Width*Products.Height*Products.Length*Warehouse.units AS volume FROM Warehouse JOIN Products ON Warehouse.product_id=Products.product_id) as A GROUP BY  A.warehouse_name