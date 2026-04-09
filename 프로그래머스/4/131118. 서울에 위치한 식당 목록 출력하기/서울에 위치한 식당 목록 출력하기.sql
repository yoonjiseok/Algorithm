-- 코드를 입력하세요
SELECT 
rr.REST_ID, 
ri.REST_NAME,
ri.FOOD_TYPE, 
ri.FAVORITES, 
ri.ADDRESS, 
round(AVG(rr.REVIEW_SCORE),2) as SCORE
FROM REST_REVIEW rr
join REST_INFO ri
on rr.rest_id = ri.rest_id
where ri.ADDRESS LIKE '서울%'
group by rr.REST_ID
order by SCORE DESC, ri.FAVORITES DESC