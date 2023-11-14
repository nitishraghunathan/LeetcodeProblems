/* Write your T-SQL query statement below */
SELECT Users.user_id, Users.name, COALESCE(SUM(Rides.distance), 0) AS 'traveled distance' FROM Users LEFT JOIN Rides ON Users.user_id=Rides.user_id GROUP BY  Users.name, Users.user_id