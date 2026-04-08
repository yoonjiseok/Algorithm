-- 코드를 입력하세요
SELECT fo.PRODUCT_ID , fp.PRODUCT_NAME, sum((fp.PRICE) * fo.AMOUNT) as TOTAL_SALES
FROM FOOD_PRODUCT fp
join FOOD_ORDER fo on
fp.product_id = fo.product_id
where YEAR(fo.PRODUCE_DATE) = 2022 and MONTH(fo.PRODUCE_DATE) = 5
group by fo.PRODUCT_ID
order by TOTAL_SALES desc, fp.PRODUCT_ID asc