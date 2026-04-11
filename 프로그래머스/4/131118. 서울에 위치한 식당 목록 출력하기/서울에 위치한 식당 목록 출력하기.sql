-- 코드를 입력하세요
SELECT ri.REST_ID, ri.REST_NAME, ri.FOOD_TYPE, ri.FAVORITES, ri.ADDRESS, round((avg(rr.review_score)),2) as SCORE
FROM REST_REVIEW rr
join REST_INFO ri
on rr.rest_id = ri.rest_id
where ri.address like '서울%'
group by rr.rest_id
order by SCORE DESC, ri.FAVORITES DESC