-- 코드를 입력하세요
SELECT YEAR(os.SALES_DATE) as year, 
MONTH(os.SALES_DATE) as month, 
(count(DISTINCT ui.USER_ID)) as PURCHASED_USERS, 
ROUND(
        (COUNT(DISTINCT os.USER_ID)*1.0) / 
        (SELECT COUNT(USER_ID) FROM USER_INFO WHERE YEAR(JOINED) = 2021), 
        1
    ) as PUCHASED_RATIO
FROM ONLINE_SALE os
left JOIN USER_INFO ui
on os.USER_ID = ui.USER_ID
where YEAR(ui.JOINED) = 2021 and ui.USER_ID is not null
GROUP BY year,month
order by year,month
#DISTINCT 서야함