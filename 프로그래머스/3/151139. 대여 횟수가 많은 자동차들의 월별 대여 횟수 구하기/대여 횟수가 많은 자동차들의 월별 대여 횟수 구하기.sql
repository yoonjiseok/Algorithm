SELECT MONTH(START_DATE) as MONTH, CAR_ID, IF (count (*) = 0, NULL, count(*)) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where CAR_ID in (select CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where START_DATE >= '2022-08-01' and START_DATE <= '2022-10-31'
                group by CAR_ID
                having count(CAR_ID) >= 5)
and START_DATE >= '2022-08-01' and START_DATE <= '2022-10-31'
group by MONTH(START_DATE), CAR_ID
order by MONTH,car_id desc