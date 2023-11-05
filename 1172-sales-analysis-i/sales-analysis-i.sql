select seller_id from sales 
group by seller_id 
having sum(price) = (
  select top 1 sum(price) as price from sales 
  group by seller_id
  order by price desc 
)