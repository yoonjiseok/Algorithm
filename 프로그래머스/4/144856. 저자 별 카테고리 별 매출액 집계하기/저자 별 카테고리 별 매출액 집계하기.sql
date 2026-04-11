-- 코드를 입력하세요
SELECT b.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY,  SUM(SALES* b.price) as TOTAL_SALES
from BOOK b
join AUTHOR a
on b.author_id = a.author_id
join BOOK_SALES bs
on b.book_id = bs.book_id
where bs.sales_date like '2022-01%'
group by b.author_id, b.category
order by b.author_id asc, b.category desc