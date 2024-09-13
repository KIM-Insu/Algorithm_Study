-- 코드를 입력하세요
select distinct (milk.cart_id)
from 
(SELECT CART_ID
FROM CART_PRODUCTS
WHERE NAME = 'Milk') milk inner join 
(SELECT CART_ID
FROM CART_PRODUCTS
WHERE NAME = 'Yogurt') yogurt
on milk.cart_id = yogurt.cart_id