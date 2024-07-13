-- 코드를 작성해주세요
select year(DIFFERENTIATION_DATE) as YEAR, (MAX(SIZE_OF_COLONY) OVER (PARTITION BY YEAR(DIFFERENTIATION_DATE)) - SIZE_OF_COLONY) AS YEAR_DEV, ID
from ecoli_data
order by year, year_dev