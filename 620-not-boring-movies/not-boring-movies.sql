/* Write your T-SQL query statement below */

SELECT A.id, A.movie, A.description, A.rating FROM Cinema AS A JOIN Cinema AS B ON A.id=B.id WHERE A.description!='boring' AND A.id%2=1 ORDER BY A.rating DESC