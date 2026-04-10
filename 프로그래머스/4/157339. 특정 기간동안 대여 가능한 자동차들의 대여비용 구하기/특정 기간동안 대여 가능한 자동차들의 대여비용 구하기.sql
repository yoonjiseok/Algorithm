-- 코드를 입력하세요
SELECT ccc.CAR_ID, ccc.CAR_TYPE, FLOOR((ccc.DAILY_FEE * 30)*(((100-ccdp.DISCOUNT_RATE))/ 100)) as FEE
FROM CAR_RENTAL_COMPANY_CAR ccc
join CAR_RENTAL_COMPANY_DISCOUNT_PLAN ccdp
on ccc.car_type = ccdp.car_type
where ccc.car_id not in (select car_id from
                        CAR_RENTAL_COMPANY_RENTAL_HISTORY
                        WHERE START_DATE <= '2022-11-30' AND END_DATE >= '2022-11-01') and 
((ccc.DAILY_FEE * 30)*(((100-ccdp.DISCOUNT_RATE))/ 100)) >= 500000 and
((ccc.DAILY_FEE * 30)*(((100-ccdp.DISCOUNT_RATE))/ 100)) < 2000000 and
ccdp.DURATION_TYPE LIKE '30%' and
(ccc.car_type LIKE 'SUV' or ccc.car_type LIKE '세단')
order by FEE DESC,ccc.car_type asc,ccc.CAR_ID desc