-- 코드를 입력하세요
SELECT date_format(SALES_DATE,'%Y-%m-%d') as SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
from online_sale
where sales_date <='2022-03-31' and sales_date >= '2022-03-01'
UNION ALL
SELECT date_format(SALES_DATE,'%Y-%m-%d') as SALES_DATE, PRODUCT_ID, NULL AS USER_ID ,SALES_AMOUNT
from offline_sale
where sales_date <='2022-03-31' and sales_date >= '2022-03-01'
order by SALES_DATE, product_id, user_id
