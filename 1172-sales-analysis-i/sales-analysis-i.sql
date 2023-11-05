WITH A AS
(
SELECT seller_id, DENSE_RANK() OVER (ORDER BY SUM(price) DESC) as rank
FROM sales
GROUP BY SELLER_id
)

SELECT seller_id
FROM A
WHERE rank = 1