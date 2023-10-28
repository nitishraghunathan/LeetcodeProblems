/* Write your T-SQL query statement below */
SELECT A.player_id, MIN(A.event_date) AS first_login FROM Activity AS A JOIN Activity AS B ON A.player_id=B.player_id GROUP BY A.player_id