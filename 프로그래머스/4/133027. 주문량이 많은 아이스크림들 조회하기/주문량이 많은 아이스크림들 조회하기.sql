-- 코드를 입력하세요
SELECT A.flavor
from (select flavor, sum(total_order) as total from first_half group by flavor) A 
left join      
     (select flavor, sum(total_order) as total from july group by flavor) B
on A.flavor = B.flavor
group by A.flavor 
order by (A.total + B.total) desc
limit 3