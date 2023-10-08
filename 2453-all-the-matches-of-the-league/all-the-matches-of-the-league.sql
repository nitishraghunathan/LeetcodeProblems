/* Write your T-SQL query statement below */
SELECT A.team_name AS home_team, B.team_name AS away_team FROM Teams A JOIN Teams B ON A.team_name!=B.team_name