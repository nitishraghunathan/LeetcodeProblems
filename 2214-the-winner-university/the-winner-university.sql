with ny_score as (

    select count(*) NY_score from  NewYork WHERE score >= 90
)

, ca_score as (

    select count(*) CA_score from  California WHERE score >= 90
)

select 
case when NY_score > CA_score THEN 'New York University'
     when NY_score < CA_score THEN 'California University'
     ELSE 'No Winner'
     END as winner
    from ny_score, ca_score
