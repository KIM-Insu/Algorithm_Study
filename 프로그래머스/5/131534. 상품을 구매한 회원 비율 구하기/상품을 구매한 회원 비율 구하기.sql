
with joined_2021 as (select user_id 
                     from user_info 
                     where year(joined) = 2021)

select year(o.sales_date) as year, month(o.sales_date) as month,
count(distinct o.user_id) as purchased_users, 
round(count(distinct o.user_id) / (select count(user_id) from joined_2021), 1) 
as purchased_ratio
from joined_2021 j inner join online_sale o on j.user_id = o.user_id
group by 1,2
order by 1,2

# WITH USER_T AS (SELECT USER_ID
#                 FROM USER_INFO
#                 WHERE YEAR(JOINED)=2021)
# SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH,
# COUNT(DISTINCT(USER_ID)) PUCHASED_USERS,
# ROUND(COUNT(DISTINCT USER_ID)/(SELECT COUNT(USER_ID) FROM USER_T),1) AS PUCHASED_RATIO
# FROM ONLINE_SALE O
# WHERE O.USER_ID IN (SELECT * FROM USER_T)
# GROUP BY YEAR(SALES_DATE), MONTH(SALES_DATE)
# ORDER BY 1, 2 ASC;