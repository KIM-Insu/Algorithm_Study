-- 코드를 입력하세요
SELECT car_type, count(1) as cars
from car_rental_company_car
where options like "%시트%"
group by 1
order by 1