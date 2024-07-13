-- 코드를 입력하세요
SELECT flavor
from (select f.flavor, sum(f.total_order) + sum(j.total_order) as total
      from first_half f inner join july j on f.flavor = j.flavor
      group by 1) total    
order by total desc
limit 3